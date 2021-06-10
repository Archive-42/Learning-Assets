---
Order: 3
Area: appservicetools
TOCTitle: Deploy the website
PageTitle: Deploy the website
MetaDescription: Node.js Deployment to Azure App Services with Visual Studio Code
DateApproved: 12/18/2017
---
# Deploy the Website

In this step, you deploy your Node.js website using VS Code and the Azure App Service extension. This tutorial uses the most basic deployment model where your app is zipped and deployed to an Azure Web App on Linux.

## Deploy using Azure App Service

In the **AZURE APP SERVICE** explorer, click the blue up arrow icon to deploy your app to Azure.

![Deploy to Web App](images/app-service-extension/deploy.png)

> **Tip:** You can also deploy from the **Command Palette** (`kb(workbench.action.showCommands)`) by typing 'deploy to web app' and running the **Azure App Service: Deploy to Web App** command.

1. Choose **Create New Web App**.

2. Type a globally unique name for your Web App and press `kbstyle(Enter)`. Valid characters for an app name are 'a-z', '0-9', and '-'.

3. Choose a location in a [region](https://azure.microsoft.com/en-us/regions/) near you or near other services you may need to access.

4. Choose your **Node.js version**, LTS is recommended.

  The notification channel shows the Azure resources that are being created for your app.

5. Choose the directory that you currently have open, `myExpressApp`.

  Click **Yes** when prompted to update your configuration to run `npm install` on the target server. Your app is then deployed.

  ![Configured deployment](images/app-service-extension/server-build.png)

Once the deployment starts, you're prompted to update your workspace so that all subsequent deploys automatically target the same App Service Web App. Choose **Yes** to ensure your changes are deployed to the correct app.

![Configured deployment](images/app-service-extension/save-configuration.png)

> **Tip:** Be sure that your application is listening on the port provided by the PORT environment variable: `process.env.PORT`.

## Browse the website

Once the deployment completes, click **Browse Website** in the prompt to view your freshly deployed website.

## Troubleshooting

Are you seeing the error **"You do not have permission to view this directory or page."**? If so, the application probably failed to start correctly. Head to the next step and view the log output to find and fix the error. If you aren't able to fix it, contact us by clicking the **I ran into an issue** button below. We're happy to help!

## Updating the website

You can deploy changes to this app by using the same process and choosing the existing app rather than creating a new one.

----

<a class="tutorial-next-btn" href="/tutorials/app-service-extension/tailing-logs">My site is on Azure</a> <a class="tutorial-feedback-btn" onclick="reportIssue('node-deployment-azureappservice', 'deploy-app')" href="javascript:void(0)">I ran into an issue</a>
