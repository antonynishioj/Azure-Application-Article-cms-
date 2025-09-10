# Article CMS (FlaskWebProject)

## Overview
This project demonstrates how to deploy a Content Management System (CMS) using Microsoft Azure services.  
The system allows users to log in, create, and view articles. Each article has a title, author, body, and image.  

The app uses:
- **Azure SQL Database** for storing users and articles.
- **Azure Blob Storage** for storing article images.
- **Azure App Service** for deployment of the Python Flask app.
- **Azure Active Directory (Entra ID)** for Microsoft login authentication.

---

## Features
- User authentication (local admin and Microsoft Login).
- Articles with text and image support.
- Secure image storage in Azure Blob.
- SQL Database integration with `users` and `articles` tables.
- Logging for both successful and failed login attempts.

---

## Deployment Steps
1. **Resource Group**  
   Create a resource group named `cms`.

2. **SQL Database**  
   - Create Azure SQL server and database.  
   - Run scripts in `sql_scripts/` to create `users` and `articles` tables with sample data.  

3. **Blob Storage**  
   - Create a Storage Account with a container named `images`.  
   - Upload and serve article images from here.  

4. **Authentication**  
   - Register the app in Azure Active Directory.  
   - Configure Redirect URI: `https://<yourapp>.azurewebsites.net/getAToken`  

5. **Deployment**  
   - Use Azure App Service to deploy the Flask app.  
   - Add environment variables for SQL, Blob, and AD credentials.  

6. **Logging**  
   - Implemented in `__init__.py` and `views.py`.  
   - Shows successful and failed login attempts.  

---

## Screenshots Required for Submission
- Article created with title **"Hello World!"** and image.  
- Resource Group showing all resources.  
- SQL Database with tables populated.  
- Blob Storage container endpoint.  
- Azure AD Redirect URI screenshot.  
- Logs showing successful and failed login attempts.  

---

## Choice: VM vs App Service

### Azure VM
- Higher cost, requires OS setup and maintenance.  
- Manual scaling.  
- Flexible but more management overhead.  

### Azure App Service
- Cost-effective (free tier available).  
- Autoscaling built-in.  
- Simple GitHub deployment.  
- Managed security and availability.  

**Decision**: I used **Azure App Service** because it reduces setup overhead, scales automatically, and fits the needs of this CMS project.

---

## Cleanup
After completion, delete resources to avoid charges:

```bash
az group delete --name cms --yes --no-wait
