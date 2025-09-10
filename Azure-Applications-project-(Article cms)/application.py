"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import create_app

# Create the Flask app using the factory function
app = create_app()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    # Run the app with SSL context for HTTPS (adhoc generates a self-signed cert)
    app.run(host=HOST, port=PORT, ssl_context='adhoc', debug=True)

