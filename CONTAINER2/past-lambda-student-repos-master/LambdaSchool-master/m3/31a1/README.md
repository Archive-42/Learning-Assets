# React-Todo

We're going to practice building a stateful class component with this project. Even though hooks are gaining popularity among react developers, class components are going to be around for a long time. It's imperative that you get use to class components, and feel comfortable working with class components since you'll most likely need to work with them if you are hired to work on a React app.

## Initializing the project.

- [x] `Fork and clone` this project and cd into your cloned version.
- [x] `npm install` or `yarn install` will pull in all the node_modules you need.
- [x] `npm start` or `yarn start` will start a development server on your `http://localhost:3000`.
- [x] If npm or yarn asks you to select different port with some error message, just confirm and it will pull it up on port 3001. This simply means you have a development server up and running on that port already.

## Instructions

- [x] Your job is to write the components to complete the Todo List application.
- [x] Your todo list should be fully functional and you should design it however you'd like. Feel free to get creative here. I have supplied a gif for you to see what the MVP functionality is.

![Todo App MVP](todo.gif)

- [x] Your todo data should be an array of objects that look a lot like this:

```js
[
  {
    task: "Organize Garage",
    id: 1528817077286,
    completed: false,
  },
  {
    task: "Bake Cookies",
    id: 1528817084358,
    completed: false,
  },
];
```

- [x] The `task` field is the todo title that will be shown to the user.
- [x] The `completed` field should default to `false` and will be the field that we toggle when we complete a todo.
- [x] The `id` field is a unique `Time Stamp` that will be assigned by `Date.now()`.

#### Instructions

- [x] **Don't focus on styling yet**. We want you to worry about function over form today.
- [x] Your todo list should display a list of todos, an input field, a submit button, and a clear all button.
- [x] Be sure to use the given files for building out these components.
- [x] `<App />` will hold all the data needed for this project. It will also be the container for your Todo Components.
- [x] All of your application data will be stored here on `<App />`.
- [x] All of your `handler` functions should live here on `<App />`.
- [x] `<TodoList />` receives your Todos array and iterates over the list generating a new `<Todo />` for each element in the array.
- [x] `<Todo />` is a component that takes in the `todo` data and displays the task to the screen.
- [x] `<TodoForm>` will hold your input field and your `Add Todo` and `Clear Completed` buttons.
- [x] Your input field should take in user input, and allow a user to press `Enter` or click on the `Submit Button` to add a todo to your list.
- [x] Once a todo is submitted, the Todo List should re-render and show the added todo.

---

- [x] Add the functionality to toggle your todo's completed flag from `false` to `true`.
- [x] Once a todo is completed, be sure to demonstrate to the user that the todo is completed by adding a line-through style property if the completed flag is true.
- [x] Add the ability to remove any todos that you have completed. `.filter` will be your best friend here. When a user clicks on the `Clear Completed` button call your handler function that will filter out any todos that have the completed flag toggled to `true`.
- [x] **Now is the time to style** Take your time to make this an app that you can be proud of.

#### Stretch Problems

- [ ] **Persist your data** in `window.localStorage()` hint: you may have to pass your data to a stringifier to get it to live inside the `localStorage()` of the browser. This will cause it to persist past the page refresh.

- [x] **Search Functionality** Add a input bar that allows you to search through your tasks and only show the ones that match the search input.

- [x] **Hosting** Create a [Netlify Account](https://www.netlify.com/) and follow the tutorial on how to host your shiny new todo app on the world wide web.
