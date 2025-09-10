

## Project Overview
This project demonstrates how to deploy a Content Management System (CMS) using Microsoft Azure services.  
The system uses:
- **Azure SQL Database** for storing users and articles.
- **Azure Blob Storage** for storing images.
- **Azure Active Directory (Entra ID)** for authentication.
- **Azure App Service** for hosting the Flask web application.

The project shows how cloud services can be combined to build a scalable and secure application.

---

## Screenshots (Submission Evidence)
1. ✅ **Article Page**: "Hello World!" by Jane Doe displayed with uploaded image and visible URL.  
2. ✅ **Resource Group**: Contains Azure SQL, Blob Storage, App Service, and App Registration.  
3. ✅ **SQL Database**: Populated with Users and Articles tables.  
4. ✅ **Blob Storage**: Container endpoint and uploaded image shown.  
5. ✅ **Azure AD**: Redirect URIs page for the registered app.  
6. ✅ **Logs**: Screenshot of App Service logs showing successful login and failed login attempt.  
7. ✅ **Code Files**: Updated `__init__.py` and `views.py`.

---

## Comparison: Azure VM vs Azure App Service

### Azure VM
- **Cost**: Higher because you pay for the whole VM (CPU, memory, storage) regardless of usage.
- **Scalability**: Requires manual scaling and load balancing setup.
- **Availability**: High availability needs multiple VMs + load balancer.
- **Workflow**: Requires manual OS setup, Python/Flask installation, firewall management, etc.

### Azure App Service
- **Cost**: Cheaper with pay-as-you-go and free tier options.
- **Scalability**: Built-in autoscaling based on demand.
- **Availability**: Microsoft-managed, 99.95% uptime SLA.
- **Workflow**: Simplified. Code can be deployed directly from GitHub or local CLI with minimal configuration.

---

## My Choice
I chose **Azure App Service** for deployment because:
- It reduces operational overhead (no OS or server maintenance).
- Deployment is seamless with GitHub integration.
- Scaling and monitoring are built-in.
- It is cost-effective for student and demo projects.

This choice allows me to focus on **application logic** rather than infrastructure management.

---

## Outcomes Achieved
- Successfully deployed a Flask CMS application to **Azure App Service**.
- Configured **Azure SQL Database** and populated with sample user/article data.
- Set up **Azure Blob Storage** for storing and serving images.
- Configured **Azure AD authentication** for secure login.
- Implemented **logging** to track successful and failed logins.
- Produced screenshots demonstrating all requirements for submission.

---

## Cleanup
After project completion, I removed all Azure resources using:
```bash
az group delete --name cms --yes --no-wait
