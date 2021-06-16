---
Order: 3
Area: other
TOCTitle: Unity
ContentId: 75CD2FA6-2F91-428A-A88D-880611AE75A0
PageTitle: Visual Studio Code and Unity
DateApproved: 5/2/2017
MetaDescription: Visual Studio Code can replace MonoDevelop as the editor for Unity
---
# Unity Development with VS Code

Visual Studio Code can be a great companion to Unity for editing and debugging C# files.  All of the [C#](/docs/languages/csharp.md) features are supported and more.  In the screen below, you can see code colorization, bracket matching, IntelliSense, CodeLens and that's just the start.

![Unity Example](images/unity/wow.gif)

Read on to find out how to configure Unity and your project to get the best possible experience.

## Prerequisites

From [Using .NET Core in Visual Studio Code](/docs/languages/dotnet.md):

1. Install [.NET Core](https://dotnet.microsoft.com/download), which includes the `dotnet` command.

1. [Windows only] Logout or restart Windows to allow changes to `%PATH%` to take effect.

1. [macOS only] To avoid seeing "Some projects have trouble loading. Please review the output for more details", make sure to install the latest stable [Mono](https://www.mono-project.com/download/) release.

   **Note**: This version of Mono, which is installed into your system, will not interfere with the version of MonoDevelop that is installed by Unity.

1. Install the [C# extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.csharp) from the VS Code Marketplace.

## Setup VS Code as Unity Script Editor

Open up **Unity Preferences**, **External Tools**, then browse for the Visual Studio Code executable as **External Script Editor**.

![Unity Preferences](images/unity/Unity_Preferences_External_Script_Editor.gif)

> The Visual Studio Code executable can be found at `/Applications/Visual Studio Code.app` on macOS, `C:\users\{username}\AppData\Local\Programs\Microsoft VS Code\Code.exe` on Windows by default.

**Unity has built-in support for opening scripts in Visual Studio Code** as an external script editor on Windows and macOS. Unity will detect when Visual Studio Code is selected as an external script editor and pass the correct arguments to it when opening scripts from Unity. Unity will also set up a default `.vscode/settings.json` with file excludes, if it does not already exist (from [Unity 5.5 Release notes](https://unity3d.com/unity/whats-new/unity-5.5.0)).

## Editing Evolved

With the solution file selected, you are now ready to start editing with VS Code. Here is a list of some of the things you can expect:

* Syntax Highlighting
* Bracket matching
* IntelliSense
* Snippets
* CodeLens
* Peek
* Go-to Definition
* Code Actions/Lightbulbs
* Go to symbol
* Hover

Two topics that will help you are [Basic Editing](/docs/editor/codebasics.md) and [C#](/docs/languages/csharp.md). In the image below, you can see VS Code showing hover context, peeking references and more.

![editing evolved example](images/unity/peekreferences.png)

## Unity Extensions

The community is continually developing more and more valuable extensions for Unity. Here are some popular extensions that you might find useful. You can search for more extensions in the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/search?term=Unity&target=VSCode).

<div class="marketplace-extensions-unity"></div>

The extensions shown above are dynamically queried. Click on an extension tile above to read the description and reviews to decide which extension is best for you. See more in the [Marketplace](https://marketplace.visualstudio.com/vscode).

## Enabling code completion (For recent versions of Unity)

If you are installing VS Code for the first time, you might be missing targeting packs required for Unity's code-completion (IntelliSense) in VS Code.

Targeting pack download links:

* [Windows: .NET Framework 4.6 Targeting Pack](https://www.microsoft.com/download/details.aspx?id=48136)
* [macOS: Download .NET SDK](https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial#macos)

Steps:

1. Stop VS Code or Unity running.
2. Download and install the targeting pack for your targeted framework version / preferred version from one of the above links.
3. Start Unity.
4. Create and/or open an existing script in VS Code, through Unity, and you should now see code completions.

## Next steps

Read on to learn more about:

* [Basic Editing](/docs/editor/codebasics.md) - Learn about the powerful VS Code editor.
* [Code Navigation](/docs/editor/editingevolved.md) - Move quickly through your source code.
* [Debugging](/docs/editor/debugging.md) - how to use the debugger with your project
* [C#](/docs/languages/csharp.md) - learn about the C# support in VS Code

## Common questions

### I don't have IntelliSense

You need to ensure that your solution is open in VS Code (not just a single file).  Open the folder with your solution and you usually will not need to do anything else.  If for some reason VS Code has not selected the right solution context, you can change the selected project by clicking on the OmniSharp flame icon on the status bar.

![OmniSharp Flame on the Status Bar](images/unity/omnisharp.png)

Choose the `-CSharp` version of the solution file and VS Code will light up.

![Choose Solution](images/unity/selectsln.png)

### How can I change the file exclusions?

Unity creates a number of additional files that can clutter your workspace in VS Code.  You can easily hide these so that you can focus on the files you actually want to edit.

To do this, add the following JSON to your [workspace settings](/docs/getstarted/settings.md).

```json
    // Configure glob patterns for excluding files and folders.
    "files.exclude": {
        "**/.git": true,
        "**/.DS_Store": true,
        "**/*.meta": true,
        "**/*.*.meta": true,
        "**/*.unity": true,
        "**/*.unityproj": true,
        "**/*.mat": true,
        "**/*.fbx": true,
        "**/*.FBX": true,
        "**/*.tga": true,
        "**/*.cubemap": true,
        "**/*.prefab": true,
        "**/Library": true,
        "**/ProjectSettings": true,
        "**/Temp": true
    }
```

As you can see below this will clean things up a lot...

Before|After
------|-----
![Unfiltered files](images/unity/unfilteredfiles.png)|![filtered files](images/unity/filteredfiles.png)

### How can I debug Unity?

Install the [Debugger for Unity](https://marketplace.visualstudio.com/items/Unity.unity-debug) extension. And check out [Debugging with VS Code](/docs/editor/debugging.md) to learn more about VS Code debugging support.
