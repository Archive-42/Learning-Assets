---
Order: 3
Area: docker
TOCTitle: Create the image
PageTitle: Create the image
MetaDescription: Node.js Deployment to Azure App Services with Visual Studio Code
DateApproved: 1/11/2018
---
# Create your Node.js application image

Next, use the Docker extension to add the necessary files to create an image for your app, build the image, and push it to a registry.

> **Tip:** If you don't already have an app for this walkthrough, follow the [Node.js tutorial](/docs/nodejs/nodejs-tutorial.md).

## Add Docker files

Open the **Command Palette** (`kb(workbench.action.showCommands)`) and type `add docker files to workspace` to run the **Docker: Add Docker files to workspace** command. This command will create the necessary Docker files. Choose your application type - **Node.js** in this tutorial - along with the port that your application listens on.

> **Tip:** Be sure that the port you select matches the port your app listens on. If you used the Express generator, set this to 3000.

This will add a `Dockerfile` along with some configuration files for Docker compose and a `.dockerignore`.

> **Tip**: VS Code has great support for Docker files. See the [Working with Docker](/docs/azure/docker.md) topic to learn about rich language features like smart suggestions, completions, and error detection.

## Build a Docker image

The files you just added, specifically, `Dockerfile`, describe the environment for your app including the location of the source files and the command to start the app within a container.

> **Tip:** Containers versus images: A container is an instance of an image.

Open the **Command Palette** (`kb(workbench.action.showCommands)`) and run **Docker: Build Image** to build the image. Choose the `Dockerfile` that was just created then give the image a name. It's important that you specify a couple of things here, the format is as follows:

`[registry or username]/[image name]:[tag]`

This tutorial uses the Azure Container Registry so for my example:

`fiveisprime.azurecr.io/myexpressapp:latest`

![tag docker image](images/docker-extension/tag-image.png)

If you are using Docker Hub, use your Docker Hub username, for example:

`fiveisprime/myexpressapp:latest`

Once completed, the Terminal panel will open and the Docker command will be executed. This is a good way to get an understanding of the commands required to do the same steps directly from the terminal. You'll also see each step, or layer, that makes up the app environment.

Once built, the image will show up in the **DOCKER** explorer under **Images**.

![Docker Image](images/docker-extension/image-list.png)

## Push the image to a registry

Open the **Command Palette** (`kb(workbench.action.showCommands)`) and run **Docker: Push** and choose the image you just built to push the image to the registry. This will also execute the Docker command in the Terminal panel to show the status of the operation. Once completed, expand the **Images** node in the Docker extension explorer to see your image.

![Image in ACR](images/docker-extension/image-in-acr.png)

Next, you'll deploy your image to Azure.

----

<a class="tutorial-next-btn" href="/tutorials/docker-extension/deploy-container">I've created an image for my application</a> <a class="tutorial-feedback-btn" onclick="reportIssue('docker-extension', 'containerize-app')" href="javascript:void(0)">I ran into an issue</a>
