---
Order: 2
Area: docker
TOCTitle: Container registries
PageTitle: Container registries
MetaDescription: Node.js Deployment to Azure App Services with Visual Studio Code
DateApproved: 1/11/2018
---
# Using Container Registries

You need a container registry to push your app image to once the image is built. Once your image is available in a container registry, you will deploy directly from that registry.

## Using Azure Container Registry

[Azure Container Registry](https://azure.microsoft.com/en-us/services/container-registry/) (ACR) is a private, secure, hosted registry for your images. ACR is used in this tutorial, however ACR uses all the same tools and processes as other registry options so the steps are consistent regardless.

Create an Azure Container Registry by signing in to the [Azure portal](https://portal.azure.com) then selecting **Create a resource** > **Containers** > **Container Registry**.

![Dashboard](images/docker-extension/qs-portal-01.png)

Enter values for **Registry name** and **Resource group**. The registry name must be unique within Azure and contain 5-50 alphanumeric characters. For this tutorial select **'Basic'** for the **SKU**. Select **Create** to deploy the ACR instance.

![Creation](images/docker-extension/qs-portal-03.png)

Once the Registry is created, click **Access Keys** from the left menu and **Enable** the Admin User option.

![Creation](images/docker-extension/auth-portal-01.png)

With the admin user account enabled, log into your registry from the Docker CLI using the following command.

```bash
$ docker login <registryname>.azurecr.io  # Copy from "Login Server"
Username:   # Copy from "Username"
Password:   # Copy from "Password"
Login Succeeded
```

## Using Docker Hub

Docker Hub is Docker's own hosted registry that provides a free way of sharing images. Sign up for a Docker ID on [Docker Hub](https://hub.docker.com/) then login to the Docker CLI using your Docker ID credentials.

## Prerequisite Check

Ensure that the registry endpoint that you just setup is visible under **Registries** in the **DOCKER** explorer.

![Registries](images/docker-extension/registries.png)

----

<a class="tutorial-next-btn" href="/tutorials/docker-extension/containerize-app">I've Created a Registry</a>
<a class="tutorial-feedback-btn" onclick="reportIssue('docker-extension', 'getting-started')" href="javascript:void(0)">I ran into an issue</a>
