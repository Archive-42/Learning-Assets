# Create React App Readme



## Create React App [![Build Status](https://camo.githubusercontent.com/ba48d404e53a630d688e2a593446b037cd2fec00e40548e3dc3d0e0b028f0a88/68747470733a2f2f6465762e617a7572652e636f6d2f66616365626f6f6b2f6372656174652d72656163742d6170702f5f617069732f6275696c642f7374617475732f66616365626f6f6b2e6372656174652d72656163742d6170703f6272616e63684e616d653d6d6173746572)](https://dev.azure.com/facebook/create-react-app/_build/latest?definitionId=1&branchName=master) [![PRs Welcome](https://camo.githubusercontent.com/accfb94480ba6689dde8dbeaf481411bbd41f1fbb13cb17e55e0846f11ce1cd5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d677265656e2e737667)](https://github.com/facebook/create-react-app/blob/master/CONTRIBUTING.md)

[![Logo](https://camo.githubusercontent.com/5ebc638bb3e5113c5a87a5462197c35f40f7185ea9940e7723846b6e403f8a6b/68747470733a2f2f6372656174652d72656163742d6170702e6465762f696d672f6c6f676f2e737667)](https://camo.githubusercontent.com/5ebc638bb3e5113c5a87a5462197c35f40f7185ea9940e7723846b6e403f8a6b/68747470733a2f2f6372656174652d72656163742d6170702e6465762f696d672f6c6f676f2e737667)

Create React apps with no build configuration.

* [Creating an App](https://github.com/facebook/create-react-app/blob/master/README.md#creating-an-app) – How to create a new app.
* [User Guide](https://facebook.github.io/create-react-app/) – How to develop apps bootstrapped with Create React App.

Create React App works on macOS, Windows, and Linux.  
If something doesn’t work, please [file an issue](https://github.com/facebook/create-react-app/issues/new).  
If you have questions or need help, please ask in [GitHub Discussions](https://github.com/facebook/create-react-app/discussions).

### Quick Overview

```text
npx create-react-app my-app
cd my-app
npm start
```

If you've previously installed `create-react-app` globally via `npm install -g create-react-app`, we recommend you uninstall the package using `npm uninstall -g create-react-app` or `yarn global remove create-react-app` to ensure that npx always uses the latest version.

_\(_[_npx_](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) _comes with npm 5.2+ and higher, see_ [_instructions for older npm versions_](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f)_\)_

Then open [http://localhost:3000/](http://localhost:3000/) to see your app.  
When you’re ready to deploy to production, create a minified bundle with `npm run build`.

[![npm start](https://camo.githubusercontent.com/b275c108e1c9e2d1c732a66ca1e0b6ecb1ae260824fb5d6ca4c4e46ee85d1ca0/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f66616365626f6f6b2f6372656174652d72656163742d61707040323762343261633765666130313866323534313135336162333064363331383066356661333965302f73637265656e636173742e737667)](https://camo.githubusercontent.com/b275c108e1c9e2d1c732a66ca1e0b6ecb1ae260824fb5d6ca4c4e46ee85d1ca0/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f66616365626f6f6b2f6372656174652d72656163742d61707040323762343261633765666130313866323534313135336162333064363331383066356661333965302f73637265656e636173742e737667)

#### Get Started Immediately

You **don’t** need to install or configure tools like webpack or Babel.  
They are preconfigured and hidden so that you can focus on the code.

Create a project, and you’re good to go.

### Creating an App

**You’ll need to have Node 10.16.0 or later version on your local development machine** \(but it’s not required on the server\). We recommend using the latest LTS version. You can use [nvm](https://github.com/creationix/nvm#installation) \(macOS/Linux\) or [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) to switch Node versions between different projects.

To create a new app, you may choose one of the following methods:

#### npx

```text
npx create-react-app my-app
```

_\(_[_npx_](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) _is a package runner tool that comes with npm 5.2+ and higher, see_ [_instructions for older npm versions_](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f)_\)_

#### npm

```text
npm init react-app my-app
```

_`npm init <initializer>` is available in npm 6+_

#### Yarn

```text
yarn create react-app my-app
```

[_`yarn create <starter-kit-package>`_](https://yarnpkg.com/lang/en/docs/cli/create/) _is available in Yarn 0.25+_

It will create a directory called `my-app` inside the current folder.  
Inside that directory, it will generate the initial project structure and install the transitive dependencies:

```text
my-app
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
    └── setupTests.js
```

No configuration or complicated folder structures, only the files you need to build your app.  
Once the installation is done, you can open your project folder:

```text
cd my-app
```

Inside the newly created project, you can run some built-in commands:

#### `npm start` or `yarn start`

Runs the app in development mode.  
Open [http://localhost:3000](http://localhost:3000/) to view it in the browser.

The page will automatically reload if you make changes to the code.  
You will see the build errors and lint warnings in the console.

[![Build errors](https://camo.githubusercontent.com/70bc7b8fa4e291e60f41abf75f392fa9bd42a24ae6cd8e0a1420c0ef73540a7b/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f6d6172696f6e65626c2f6372656174652d72656163742d61707040396636323832363731633534663038373461666433376137326636363839373237623536323439382f73637265656e636173742d6572726f722e737667)](https://camo.githubusercontent.com/70bc7b8fa4e291e60f41abf75f392fa9bd42a24ae6cd8e0a1420c0ef73540a7b/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f6d6172696f6e65626c2f6372656174652d72656163742d61707040396636323832363731633534663038373461666433376137326636363839373237623536323439382f73637265656e636173742d6572726f722e737667)

#### `npm test` or `yarn test`

Runs the test watcher in an interactive mode.  
By default, runs tests related to files changed since the last commit.

[Read more about testing.](https://facebook.github.io/create-react-app/docs/running-tests)

#### `npm run build` or `yarn build`

Builds the app for production to the `build` folder.  
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.  


Your app is ready to be deployed.

### User Guide

You can find detailed instructions on using Create React App and many tips in [its documentation](https://facebook.github.io/create-react-app/).

### How to Update to New Versions?

Please refer to the [User Guide](https://facebook.github.io/create-react-app/docs/updating-to-new-releases) for this and other information.

### Philosophy

* **One Dependency:** There is only one build dependency. It uses webpack, Babel, ESLint, and other amazing projects, but provides a cohesive curated experience on top of them.
* **No Configuration Required:** You don't need to configure anything. A reasonably good configuration of both development and production builds is handled for you so you can focus on writing code.
* **No Lock-In:** You can “eject” to a custom setup at any time. Run a single command, and all the configuration and build dependencies will be moved directly into your project, so you can pick up right where you left off.

### What’s Included?

Your environment will have everything you need to build a modern single-page React app:

* React, JSX, ES6, TypeScript and Flow syntax support.
* Language extras beyond ES6 like the object spread operator.
* Autoprefixed CSS, so you don’t need `-webkit-` or other prefixes.
* A fast interactive unit test runner with built-in support for coverage reporting.
* A live development server that warns about common mistakes.
* A build script to bundle JS, CSS, and images for production, with hashes and sourcemaps.
* An offline-first [service worker](https://developers.google.com/web/fundamentals/getting-started/primers/service-workers) and a [web app manifest](https://developers.google.com/web/fundamentals/engage-and-retain/web-app-manifest/), meeting all the [Progressive Web App](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app) criteria. \(_Note: Using the service worker is opt-in as of `react-scripts@2.0.0` and higher_\)
* Hassle-free updates for the above tools with a single dependency.

Check out [this guide](https://github.com/nitishdayal/cra_closer_look) for an overview of how these tools fit together.

The tradeoff is that **these tools are preconfigured to work in a specific way**. If your project needs more customization, you can ["eject"](https://facebook.github.io/create-react-app/docs/available-scripts#npm-run-eject) and customize it, but then you will need to maintain this configuration.

### Popular Alternatives

Create React App is a great fit for:

* **Learning React** in a comfortable and feature-rich development environment.
* **Starting new single-page React applications.**
* **Creating examples** with React for your libraries and components.

Here are a few common cases where you might want to try something else:

* If you want to **try React** without hundreds of transitive build tool dependencies, consider [using a single HTML file or an online sandbox instead](https://reactjs.org/docs/try-react.html).
* If you need to **integrate React code with a server-side template framework** like Rails, Django or Symfony, or if you’re **not building a single-page app**, consider using [nwb](https://github.com/insin/nwb), or [Neutrino](https://neutrino.js.org/) which are more flexible. For Rails specifically, you can use [Rails Webpacker](https://github.com/rails/webpacker). For Symfony, try [Symfony's webpack Encore](https://symfony.com/doc/current/frontend/encore/reactjs.html).
* If you need to **publish a React component**, [nwb](https://github.com/insin/nwb) can [also do this](https://github.com/insin/nwb#react-components-and-libraries), as well as [Neutrino's react-components preset](https://neutrino.js.org/packages/react-components/).
* If you want to do **server rendering** with React and Node.js, check out [Next.js](https://nextjs.org/) or [Razzle](https://github.com/jaredpalmer/razzle). Create React App is agnostic of the backend, and only produces static HTML/JS/CSS bundles.
* If your website is **mostly static** \(for example, a portfolio or a blog\), consider using [Gatsby](https://www.gatsbyjs.org/) or [Next.js](https://nextjs.org/). Unlike Create React App, Gatsby pre-renders the website into HTML at build time. Next.js supports both server rendering and pre-rendering.
* Finally, if you need **more customization**, check out [Neutrino](https://neutrino.js.org/) and its [React preset](https://neutrino.js.org/packages/react/).

All of the above tools can work with little to no configuration.

If you prefer configuring the build yourself, [follow this guide](https://reactjs.org/docs/add-react-to-an-existing-app.html).

### React Native

Looking for something similar, but for React Native?  
Check out [Expo CLI](https://github.com/expo/expo-cli).

### Contributing

We'd love to have your helping hand on `create-react-app`! See [CONTRIBUTING.md](https://github.com/facebook/create-react-app/blob/master/CONTRIBUTING.md) for more information on what we're looking for and how to get started.

### Supporting Create React App

Create React App is a community maintained project and all contributors are volunteers. If you'd like to support the future development of Create React App then please consider donating to our [Open Collective](https://opencollective.com/create-react-app).

### Credits

This project exists thanks to all the people who [contribute](https://github.com/facebook/create-react-app/blob/master/CONTRIBUTING.md).  
[![](https://camo.githubusercontent.com/92ccfed4ad11b4743ec414e1b19700847d69e613d8277f902cb67c64c2c07218/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6372656174652d72656163742d6170702f636f6e7472696275746f72732e7376673f77696474683d38393026627574746f6e3d66616c7365)](https://github.com/facebook/create-react-app/graphs/contributors)

Thanks to [Netlify](https://www.netlify.com/) for hosting our documentation.

### Acknowledgements

We are grateful to the authors of existing related projects for their ideas and collaboration:

* [@eanplatter](https://github.com/eanplatter)
* [@insin](https://github.com/insin)
* [@mxstbr](https://github.com/mxstbr)

![](.gitbook/assets/image.png)

## Getting Started:

## Getting Started

Create React App is an officially supported way to create single-page React applications. It offers a modern build setup with no configuration.

### Quick Start[\#](https://create-react-app.dev/docs/getting-started/#quick-start)

npx create-react-app my-appcd my-appnpm start

> If you've previously installed `create-react-app` globally via `npm install -g create-react-app`, we recommend you uninstall the package using `npm uninstall -g create-react-app` or `yarn global remove create-react-app` to ensure that `npx` always uses the latest version.

_\(_[_npx_](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) _comes with npm 5.2+ and higher, see_ [_instructions for older npm versions_](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f)_\)_

Then open [http://localhost:3000/](http://localhost:3000/) to see your app.

When you’re ready to deploy to production, create a minified bundle with `npm run build`.

![npm start](https://cdn.jsdelivr.net/gh/facebook/create-react-app@27b42ac7efa018f2541153ab30d63180f5fa39e0/screencast.svg)

#### Get Started Immediately[\#](https://create-react-app.dev/docs/getting-started/#get-started-immediately)

You **don’t** need to install or configure tools like webpack or Babel. They are preconfigured and hidden so that you can focus on the code.

Create a project, and you’re good to go.

### Creating an App[\#](https://create-react-app.dev/docs/getting-started/#creating-an-app)

**You’ll need to have Node &gt;= 10 on your local development machine** \(but it’s not required on the server\). You can use [nvm](https://github.com/creationix/nvm#installation) \(macOS/Linux\) or [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) to switch Node versions between different projects.

To create a new app, you may choose one of the following methods:

#### npx[\#](https://create-react-app.dev/docs/getting-started/#npx)

npx create-react-app my-app

_\(_[_npx_](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) _comes with npm 5.2+ and higher, see_ [_instructions for older npm versions_](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f)_\)_

#### npm[\#](https://create-react-app.dev/docs/getting-started/#npm)

npm init react-app my-app

_`npm init <initializer>` is available in npm 6+_

#### Yarn[\#](https://create-react-app.dev/docs/getting-started/#yarn)

yarn create react-app my-app

_`yarn create` is available in Yarn 0.25+_

#### Selecting a template[\#](https://create-react-app.dev/docs/getting-started/#selecting-a-template)

You can now optionally start a new app from a template by appending `--template [template-name]` to the creation command.

If you don't select a template, we'll create your project with our base template.

Templates are always named in the format `cra-template-[template-name]`, however you only need to provide the `[template-name]` to the creation command.npx create-react-app my-app --template \[template-name\]

> You can find a list of available templates by searching for ["cra-template-\*"](https://www.npmjs.com/search?q=cra-template-*) on npm.

Our [Custom Templates](https://create-react-app.dev/docs/custom-templates) documentation describes how you can build your own template.

**Creating a TypeScript app\#**

You can start a new TypeScript app using templates. To use our provided TypeScript template, append `--template typescript` to the creation command.npx create-react-app my-app --template typescript

If you already have a project and would like to add TypeScript, see our [Adding TypeScript](https://create-react-app.dev/docs/adding-typescript) documentation.

#### Selecting a package manager[\#](https://create-react-app.dev/docs/getting-started/#selecting-a-package-manager)

When you create a new app, the CLI will use [Yarn](https://yarnpkg.com/) to install dependencies \(when available\). If you have Yarn installed, but would prefer to use npm, you can append `--use-npm` to the creation command. For example:npx create-react-app my-app --use-npm

### Output[\#](https://create-react-app.dev/docs/getting-started/#output)

Running any of these commands will create a directory called `my-app` inside the current folder. Inside that directory, it will generate the initial project structure and install the transitive dependencies:

```text
my-app
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    ├── serviceWorker.js
    └── setupTests.js



```



No configuration or complicated folder structures, only the files you need to build your app. Once the installation is done, you can open your project folder:cd my-app

### Scripts[\#](https://create-react-app.dev/docs/getting-started/#scripts)

Inside the newly created project, you can run some built-in commands:

#### `npm start` or `yarn start`[\#](https://create-react-app.dev/docs/getting-started/#npm-start-or-yarn-start)

Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000/) to view it in the browser.

The page will automatically reload if you make changes to the code. You will see the build errors and lint warnings in the console.

![Build errors](https://cdn.jsdelivr.net/gh/marionebl/create-react-app@9f6282671c54f0874afd37a72f6689727b562498/screencast-error.svg)

#### `npm test` or `yarn test`[\#](https://create-react-app.dev/docs/getting-started/#npm-test-or-yarn-test)

Runs the test watcher in an interactive mode. By default, runs tests related to files changed since the last commit.

[Read more about testing](https://create-react-app.dev/docs/running-tests).

#### `npm run build` or `yarn build`[\#](https://create-react-app.dev/docs/getting-started/#npm-run-build-or-yarn-build)

Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.

Your app is ready to be deployed.[Edit this page](https://github.com/facebook/create-react-app/edit/master/docusaurus/docs/getting-started.md)

