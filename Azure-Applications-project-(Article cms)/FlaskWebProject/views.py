import msal
import uuid
import os
from flask import render_template, redirect, url_for, request, session, current_app, flash
from FlaskWebProject import app, db
from FlaskWebProject.forms import LoginForm, PostForm
from FlaskWebProject.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# MSAL helpers
def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache

def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    authority = os.environ.get("AUTHORITY", "https://login.microsoftonline.com/common")
    return msal.ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
        token_cache=cache
    )

def _build_auth_url(scopes=None, state=None):
    msal_app = _build_msal_app()
    return msal_app.get_authorization_request_url(
        scopes or ["User.Read"],
        state=state,
        redirect_uri=url_for("authorized", _external=True)
    )

# --- existing routes unchanged until login() ---

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("home")
        return redirect(next_page)

    # MSAL login
    session["state"] = str(uuid.uuid4())
    auth_url = _build_auth_url(scopes=["User.Read"], state=session["state"])
    return render_template("login.html", title="Sign In", form=form, auth_url=auth_url)

@app.route("/getAToken")
def authorized():
    if request.args.get("state") != session.get("state"):
        return redirect(url_for("home"))

    if "error" in request.args:
        return render_template("auth_error.html", result=request.args)

    if request.args.get("code"):
        cache = _load_cache()
        msal_app = _build_msal_app(cache=cache)
        result = msal_app.acquire_token_by_authorization_code(
            request.args["code"],
            scopes=["User.Read"],
            redirect_uri=url_for("authorized", _external=True)
        )
        if "error" in result:
            return render_template("auth_error.html", result=result)

        session["user"] = result.get("id_token_claims")
        user = User.query.filter_by(username="admin").first()
        login_user(user)
        _save_cache(cache)

    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    logout_user()
    if session.get("user"):  # MSAL logout
        session.clear()
        return redirect(
            "https://login.microsoftonline.com/common/oauth2/v2.0/logout"
            + "?post_logout_redirect_uri="
            + url_for("login", _external=True)
        )
    return redirect(url_for("login"))
