## React.js Assessment

#### Q1. If you want to import just the Component from the React library, what syntax do you use?

- `import React.Component from 'react'`
- `import [ Component ] from 'react'`
- `import Component from 'react'`
- `import { Component } from 'react'` <<<<<--CORRECT

#### Q2. If a function component should always render the same way given the same props, what is a simple performance optimization available for it?

- Wrap it in the `React.memo` higher-order component. <<<<<--CORRECT
- Implement the `useReducer` Hook.
- Implement the `useMemo` Hook.
- Implement the `shouldComponentUpdate` lifecycle method.

#### Q3. How do you fix the syntax error that results from running this code?

```javascript
const person =(firstName, lastName) =>
       {
            first: firstName,
            last: lastName
        }
console.log(person("Jill", "Wolson"))
```

- Wrap the object in parentheses. <<<<<--CORRECT
- Call the function from another file.
- Add a return statement before the first curly brace.
- Replace the with an array

#### Q4. If you see the following import in a file, what is being used for state management in the component?

`import React, {useState} from 'react';`

- React Hooks <<<<<--CORRECT
- stateful components
- math
- class components

#### Q5. Using object literal enhancement, you can put values back into an object. When you log person to the console, what is the output?

```javascript
const name = 'Rachel';
const age = 31;
const person = { name, age };
console.log(person);
```

- `{{name: "Rachel", age: 31}}`
- `{name: "Rachel", age: 31}` <<<<<--CORRECT
- `{person: "Rachel", person: 31}}`
- `{person: {name: "Rachel", age: 31}}`

#### Q6. What is the testing library most often associated with React?

- Mocha
- Chai
- Sinon
- Jest <<<<<--CORRECT

#### Q7. To get the first item from the array ("cooking") using array destructuring, how do you adjust this line?

```javascript
const topics = ['cooking', 'art', 'history'];
```

- `const first = ["cooking", "art", "history"]`
- `const [] = ["cooking", "art", "history"]`
- `const [, first]["cooking", "art", "history"]`
- `const [first] = ["cooking", "art", "history"]` <<<<<--CORRECT

#### Q8. How do you handle passing through the component tree without having to pass props down manually at every level?

- React Send
- React Pinpoint
- React Router
- React Context <<<<<--CORRECT

#### Q9. What should the console read when the following code is run?

```javascript
const [, , animal] = ['Horse', 'Mouse', 'Cat'];
console.log(animal);
```

- Horse
- Cat <<<<<--CORRECT
- Mouse
- undefined

#### 10. What is the name of the tool used to take JSX and turn it into createElement calls?

- JSX Editor
- ReactDOM
- Browser Buddy
- Babel <<<<<--CORRECT

#### 11. Why might you use useReducer over useState in a React component?

- when you want to replace Redux
- when you need to manage more complex state in an app <<<<<--CORRECT
- when you want to improve performance
- when you want to break your production app

#### 12. Which props from the props object is available to the component with the following syntax?

```javascript
<Message {...props} />
```

- any that have not changed
- all of them <<<<<--CORRECT
- child props
- any that have changed

#### 13. Consider the following code from React Router. What do you call :id in the path prop?

```javascript
<Route path="/:id" />
```

- This is a route modal
- This is a route parameter <<<<<--CORRECT
- This is a route splitter
- This is a route link

#### 14. If you created a component called Dish and rendered it to the DOM, what type of element would be rendered?

```javascript
function Dish() {
  return <h1> Mac and Cheese</h1>;
}

ReactDOM.render(<Dish />, document.getElementById('root'));
```

- `div`
- section
- component
- `h1` <<<<<--CORRECT

#### 15. What does this React element look like given the following function?

```javascript
React.createElement('h1', null, "What's happening?");
```

- `<h1 props={null}>What's happening?</h1>`
- `<h1>What's happening?</h1>` <<<<<--CORRECT
- `<h1 id="component">What's happening?</h1>`
- `<h1 id="element">What's happening?</h1>`

#### 16. What property do you need to add to the Suspense component in order to display a spinner or loading state?

```javascript
function MyComponent() {
  return (
    <Suspense>
      <div>
        <Message />
      </div>
    </Suspense>
  );
}
```

- lazy
- loading
- fallback <<<<<--CORRECT
- spinner

#### 17. What do you call the message wrapped in curly braces below?

```javascript
let message = 'Hi there';
const element = <p>{message}</p>;
```

- a JS function
- a JS element
- a JS expression <<<<<--CORRECT
- a JSX wrapper

#### 18. What can you use to handle code splitting?

- `React.memo`
- `React.split`
- `React.lazy` <<<<<--CORRECT
- `React.fallback`

#### 19. When do you use useLayoutEffect?

- to optimize for all devices
- to complete the update
- to change the layout of the screen
- when you need the browser to paint before the effect runs <<<<<--CORRECT

#### 20. What is the difference between the click behaviors of these two buttons (assuming that this.handleClick is bound correctly)?

```javascript
A. <button onClick="{this.handleClick}>Click Me</button>"
B. <button onClick="{event => this.handleClick(event)}}>Click Me</button>"
```

- Button A will not have access to the event object on click of the button.
- Button B will not fire the handler this.handleClick successfully. <<<<<--CORRECT
- Button A will not fire the handler this.handleClick successfully.
- There is no difference

#### 21. How do you destructure the properties that are sent to the Dish component?

```javascript
function Dish(props) {
  return (
    <h1>
      {props.name} {props.cookingTime}
    </h1>
  );
}
```

- `function Dish([name, cookingTime]) { return <h1>{name} {cookingTime}</h1>; }`
- `function Dish({name, cookingTime}) { return <h1>{name} {cookingTime}</h1>; }` <<<<<--CORRECT

- `function Dish(props) { return <h1>{name} {cookingTime}</h1>; }`
- `function Dish(...props) { return <h1>{name} {cookingTime}</h1>; }`

#### 22. When might you use React.PureComponent?

- when you do not want your component to have props
- when you have sibling components that need to be compared
- when you want a default implementation of shouldComponentUpdate() <<<<<--CORRECT
- when you do not want your component to have state

#### 23. Why is it important to avoid copying the values of props into a component's state where possible?

- because you should never mutate state
- because getDerivedStateFromProps() is an unsafe method to use
- because you want to allow a component to update in response to changes in the props <<<<<--CORRECT
- because you want to allow data to flow back up to the parent

#### 24. What is the children prop?

- a property that adds child components to state
- a property that lets you pass components as data to other components <<<<<--CORRECT
- a property that lets you set an array as a property
- a property that lets you pass data to child elements

#### 25. Which attribute do you use to replace innerHTML in the browser DOM?

- injectHTML
- dangerouslySetInnerHTML <<<<<--CORRECT
- weirdSetInnerHTML
- strangeHTML

#### 26. Which of these terms commonly describe React applications?

- declarative <<<<<--CORRECT
- integrated
- closed
- imperative

#### 27. When using webpack, why would you need to use a loader?

- to put together physical file folders
- to process files
- to load external data <<<<<--CORRECT
- to load the website into everyone's phone

#### 28. A representation of a user interface that is kept in memory and is synced with the "real" DOM is called what?

- virtual DOM <<<<<--CORRECT
- DOM
- virtual elements
- shadow DOM

#### 29. You have written the following code but nothing is rendering. How do you fix this problem?

```javascript
const Heading = () => {
  <h1>Hello!</h1>;
};
```

- Add a render function
- Change the curly braces to parentheses or add a return statement before the h1 tag. <<<<<-- Correct
- Move the h1 to another component.
- Surround the h1 in a div.

#### Q30. To create a constant in JavaScript, which keyword do you use?

- const <<<<<--CORRECT
- let
- constant
- var

#### Q31. What do you call a React component that catches JavaScript errors anywhere in the child component tree?

- error bosses
- error catchers
- error helpers
- error boundaries <<<<<--CORRECT

#### Q32. In which lifecycle method do you make requests for data in a class component?

- constructor
- componentDidMount <<<<<--CORRECT
- componentWillReceiveProps
- componentWillMount

#### Q33. React components are composed to create a user interface. How are components composed?

- by putting them in the same file
- by nesting components <<<<<--CORRECT
- with webpack
- with code splitting

#### Q34. All React components must act like **\_\_** with respect to their props.

- monads
- pure functions <<<<<--CORRECT
- recursive functions
- higher-order functions

#### Q35. Why might you use a ref?

- to directly access the DOM node <<<<<--CORRECT
- to refer to another JS file
- to call a function
- to bind the function

#### Q36. What is `[e.target.id]` called in the following code snippet?

```javascript
handleChange(e) {
  this.setState({[e.target.id]: e.target.value })
}
```

- a computer property name
- a set value
- a dynamic key <<<<<--CORRECT
- a JSX code string

#### Q37. What is the name of this component?

```
class Clock extends React.Component {
   render() {
    return <h1>Look at the time: {time}</h1>;
   }
  }
```

- Clock <<<<<--CORRECT
- It does not have a name prop.
- React.Component
- Component

#### Q38. What is sent to an Array.map() function?

- a callback function that is called once for each element in the array <<<<<--CORRECT
- the name of another array to iterate over
- the number of times you want to call the function
- a string describing what the function should do

#### Q39. Why is it a good idea to pass a function to setState instead of an object?

- It is more functional than an object
- It makes sure that the object is not mutated
- It automatically updates a component
- setState is asynchronous and might result in out of sync values. <<<<<--CORRECT

#### Q40. What package contains the render() function that renders a React element tree to the DOM?

- `React`
- `ReactDOM` <<<<<--CORRECT
- `Render`
- `DOM`

#### Q41. How do you set a default value for an uncontrolled form field?

- Use the `value` property
- Use the `defaultValue` property <<<<<--CORRECT
- Use the `default` property
- It assigns one automatically

#### Q42. What do you need to change about this code to get it to run?

```js
class clock extends React.Component {
  render() {
    return <h1>Look at the time: {this.props.time}</h1>;
  }
}
```

- Add quotes around the return value
- Remove `this`
- Remove the render method
- Capitalize `clock` <<<<<--CORRECT (In JSX, lower-case tag names are considered to be HTML tags. Read [this article](https://reactjs.org/docs/jsx-in-depth.html#html-tags-vs.-react-components))

#### Q43. Which Hook could be used to update the document's title?

- `useEffect(function updateTitle() { document.title = name + ' ' + lastname; });` <<<<<--CORRECT
- `useEffect(() => { title = name + ' ' + lastname; });`
- `useEffect(function updateTitle() { name + ' ' + lastname; });`
- `useEffect(function updateTitle() { title = name + ' ' + lastname; });`

#### Q44. What can you use to wrap Component imports in order to load them lazily?

- `React.fallback`
- `React.split`
- `React.lazy` <<<<<--CORRECT
- `React.memo`

#### Q45. How do you invoke setDone only when component mounts, using hooks?

```javascript
function MyComponent(props) {
  const [done, setDone] = useState(false);

  return <h1>Done: {done}</h1>;
}
```

- `useEffect(() => { setDone(true); });`
- `useEffect(() => { setDone(true); }, []);`
- `useEffect(() => { setDone(true); }, [setDone]);` <<<<<--CORRECT
- `useEffect(() => { setDone(true); }, [done, setDone]);`

#### Q46.

What value of button will allow you to pass the name of the person to be hugged?

```javascript
class Huggable extends React.Component{
  hug(id){
    console.log("hugging " + id);
  }

  render() {
    let name = "kitteh";
    let button = // Missing Code
    return button;
  }
}
```

- `<button onClick={(name) => this.hug(name)>Hug Button</button>`<<<<<--CORRECT
- `<button onClick={this.hug(e, name)}>Hug Button</button>`
- `<button onClick={(e) => hug(e,name)}>Hug Button</button>` 
- `<button onClick={(e) => this.hug(name, e)}>Hug Button</button>`

#### Q47.

Currently, `handleClick` is being called instead of passed as a reference. How do you fix this?

```javascript
<button onClick={this.handleClick()}>Click this</button>
```

- `<button onClick={this.handleClick.bind(handleClick}>Click this</button>`<<<<<--CORRECT
- `<button onClick={handleClick()}>Click this</button>`
- `<button onClick={this.handleClick}>Click this</button>` 
- `<button onclick={this.handleClick}>Click this</button>`

# ReactJs Assessment 

>### Q1. How do you refactor this function using an arrow function?
```js
function add(x, y) {
  console.log(x + y);
}
```
- [ ] const add = x,y => console.log(x + y);

- [ ] const add = x,y => x + y;

- [x] const add = (x, y) => console.log(x + y);

- [ ] function add = (x, y) => console.log(x + y);

>### Q2. Consider the following component. What is the default color for the star?
```js
const Star = ({ selected = false }) => (
  <Icon color={selected ? "red" : "grey"} />
);
```
- [x] grey

- [ ] red

- [ ]  black

- [ ] white

>### Q3. Which function is used to update state variables in a React class component?

- [x] setState

- [ ] refreshState

- [ ] replaceState

- [ ] updateState

>### Q4. How do you fix the syntax error that results from running this code?
```js
const person =(firstName, lastName) =>
       {
            first: firstName,
            last: lastName
        }
console.log(person("Jill", "Wolson"))
```
- [x] Wrap the object in parentheses.

- [ ] Call the function from another file.

- [ ] Add a return statement before the first curly brace.

- [ ] Replace the with an array

>### Q5. How do you make an image more accessible in React?

- [ ] It is not possible

- [x] Add an alt tag.

- [ ] Create a new image that explains the image.

- [ ] Add text to the image.

>### Q6. What is the name of the tool used to take JSX and turn it into createElement calls?

- [ ] JSX Editor

- [ ] ReactDOM

- [ ] Browser Buddy

- [x] Babel

>### Q7. Why should you use React Router's Link component instead of a basic `<a>` tag in React?

- [ ] The `<a>` tag triggers a full page reload, while the Link component does not.

- [ ] The `<a>` tag will cause an error when used in React.

- [ ] The Link component allows the user to use the browser's Back button.-

- [ ] There is no difference—the Link component is just another name for the `<a>` tag.

>### Q8. When do you use useLayoutEffect?

- [ ] to optimize for all devices

- [ ] to complete the update

- [ ] to change the layout of the screen

- [x] when you need the browser to paint before the effect runs

>### Q9. How do you add a class of heading to this h1 element?
```js
let dish = <h1>Mac and Cheese</h1>;
```
```html
[ ] let dish = <h1 class="heading">Mac and Cheese</h1>;

[x] let dish = <h1 className="heading">Mac and Cheese</h1>;

[ ] let dish = <h1 class:"heading">Mac and Cheese</h1>;

[ ] let dish = <h1 class={heading}>Mac and Cheese</h1>;
```
>### Q10. What will this code render?
```js
ReactDOM.render(
  React.createElement("h1", {id: "heading"}, "New Articles"),
  document.getElementById("root")
);
```
```html
[ ] <h1>New Articles</h1>

[ ] <h1 id="heading">New Articles</h1>

[ ] <h1 id="root">New Articles</h1>

[ ] <header id="root">New Articles</header>
```
>### Q11. To create a constant in JavaScript, which keyword do you use?

- [x] const

- [ ] let

- [ ] constant

- [ ] var

>### Q12. What command can you use to generate a React project?

- [ ] react-start

- [ ] react-gen

- [x] create-react-app

- [ ] react-starter

>### Q13. What is the browser extension called that React developers use to debug applications?

- [ ] React Developer Tools

- [ ] React Debug

- [ ] React Codewatch

- [ ] React Tooling Add-on

>### Q14. A representation of a user interface that is kept in memory and is synced with the "real" DOM is called what?

- [ ] shadow DOM

- [x] virtual DOM

- [ ] DOM

- [ ] virtual elements

>### Q15. Which tool is not part of Create React App?

- [ ] jQuery-

- [ ] webpack

- [ ] React

- [ ] ReactDOM

>### Q16. What will happen when this useEffect Hook is executed, assuming name is not already equal to John?
```js
useEffect(() => {
setName("John");
}, [name]);
```
- [ ] It will cause an infinite loop.

- [ ] It will cause an error immediately.

- [ ] It will update the value of name once and not run again until name is changed from the outside.

- [ ] It will execute the code inside the function, but only after waiting to ensure that no other component is accessing the name variable.

>### Q17. Currently, handleClick is being called instead of passed as a reference. How do you fix this? 
```js
<button onClick={this.handleClick()}>Click this</button>
```
```js
[ ] <button onClick={this.handleClick.bind(handleClick)}>Click this</button>

[ ] <button onClick={handleClick()}>Click this</button>

[ ] <button onclick={this.handleClick}>Click this</button>

[ ] <button onClick={this.handleClick}>Click this</button>
```
>### Q18. You have created a new method in a class component called handleClick, but it is not working. Which code is missing?
```js
class Button extends React.Component {

    constructor(props) {
         super(props);
         // Missing line
    }

    handleClick() {...}
}
```
```js
[ ] this.handleClick.bind();

[ ] this.handleClick = this.handleClick.bind(this);

[ ] props.bind(handleClick);

[ ] this.handleClick.bind(this);
```
>### Q19. You have written the following code but nothing is rendering. How do you fix this problem?
```js
const Heading = () => {
  <h1>Hello!</h1>;
};
```
- [ ] Add a render function

- [x] Change the curly braces to parentheses or add a return statement before the h1 tag. 

- [ ] Move the h1 to another component.

- [ ] Surround the h1 in a div.

>### Q20. If you created a component called Dish and rendered it to the DOM, what type of element would be rendered?
```js
function Dish() {
  return <h1> Mac and Cheese</h1>;
}
ReactDOM.render(<Dish />, document.getElementById('root'));
```
- [ ] `div`

- [ ] section

- [ ] component

- [x] `h1`

>### Q21. Using object literal enhancement, you can put values back into an object. When you log person to the console, what is the output?
```js
const name = 'Rachel';
const age = 31;
const person = { name, age };
console.log(person);
```
```js
[ ] {{name: "Rachel", age: 31}}

[x] {name: "Rachel", age: 31}

[ ] {person: "Rachel", person: 31}}

[ ] {person: {name: "Rachel", age: 31}}
```
>### Q22. What property do you need to add to the Suspense component in order to display a spinner or loading state?
```js
function MyComponent() {
  return (
    <Suspense>
      <div>
        <Message />
      </div>
    </Suspense>
  );
}
```
- [ ] lazy

- [ ] loading

- [x] fallback

- [ ] spinner

>### Q23. React components are composed to create a user interface. How are components composed?

- [ ] by putting them in the same file

- [x] by nesting components

- [ ] with webpack

- [ ] with code splitting

>### Q24. What does this React element look like given the following function?
```js
React.createElement('h1', null, "What's happening?");
```
```html
[ ] <h1 props={null}>What's happening?</h1>

[x] <h1>What's happening?</h1>

[ ] <h1 id="component">What's happening?</h1>

[ ] <h1 id="element">What's happening?</h1>
```
>### Q25. All React components must act like --- with respect to their props.

- [ ] monads

- [x] pure functions

- [ ] recursive functions

- [ ] higher-order functions -

>### Q26. Consider the following code from React Router. What do you call :id in the path prop?
```js
<Route path="/:id" />
```
- [ ] This is a route modal

- [x] This is a route parameter

- [ ] This is a route splitter

- [ ] This is a route link

>### Q27. If you want to import just the Component from the React library, what syntax do you use?
```js
[ ] import React.Component from 'react'

[ ] import [ Component ] from 'react'

[ ] import Component from 'react'

[x] import { Component } from 'react'
```
>### Q28. To get the first item from the array ("cooking") using array destructuring, how do you adjust this line?
```js
const topics = ['cooking', 'art', 'history'];
```
```js
[ ] const first = ["cooking", "art", "history"]

[ ] const [] = ["cooking", "art", "history"]

[ ] const [, first]["cooking", "art", "history"]

[x] const [first] = ["cooking", "art", "history"]
```
>### Q29. How do you invoke setDone only when component mounts, using hooks?
```js
function MyComponent(props) {
  const [done, setDone] = useState(false);
  return <h1>Done: {done}</h1>;
}
```
```js
[ ] useEffect(() => { setDone(true); });

[ ] useEffect(() => { setDone(true); }, []);

[x] useEffect(() => { setDone(true); }, [setDone]);

[ ] useEffect(() => { setDone(true); }, [done, setDone]);
```
>### Q30. What is the difference between the click behaviors of these two buttons (assuming that this.handleClick is bound correctly)?

```js
A. <button onClick="{this.handleClick}>Click Me</button>"
B. <button onClick="{event => this.handleClick(event)}}>Click Me</button>"
```
- [ ] Button A will not have access to the event object on click of the button.

- [x] Button B will not fire the handler this.handleClick successfully.

- [ ] Button A will not fire the handler this.handleClick successfully.

- [ ] There is no difference

>### Q31. What is the name of this component?
```js
class Comp extends React.Component {
  render() {
    return <h1>Look at the time: {time}</h1>;
 }
}
```
- [ ] React.Component

- [ ] h1

- [ ] Comp

- [ ] Component

>### Q32. Which package contains the render() function that renders a React element tree to the DOM?

- [ ] Render

- [ ] DOM

- [ ] React

- [ ] ReactDOM

>### Q33. What do you call the message wrapped in curly braces below?

```js
let message = 'Hi there';
const element = <p>{message}</p>;
```
- [ ] a JS function

- [ ] a JS element

- [x] a JS expression 

- [ ] a JSX wrapper

>### Q34. You have added a style property to the h1 but there is an unexpected token error when it runs. How do you fix this? 
```js
const element = <h1 style={ backgroundColor: "blue" }>Hi</h1>;
```
```html
const element = <h1 style={blue}>Hi</h1>;

const element = <h1 style="blue">Hi</h1>;

const element = <h1 style="backgroundColor: "blue"">Hi</h1>;

const element = <h1 style={{backgroundColor: "blue"}}>Hi</h1>;
```
>### Q35. What is the first argument, x, that is sent to the createElement function?
```js
React.createElement(x,y,z);
```
- [ ] data that should be displayed in the element

- [ ] the order in which this element should be placed on the page

- [ ] the properties of the element

- [ ] the element that should be created

>### Q36. If a function component should always render the same way given the same props, what is a simple performance optimization available for it?

- [x] Wrap it in the `React.memo` higher-order component.

- [ ] Implement the `useReducer` Hook.

- [ ] Implement the `useMemo` Hook.

- [ ] Implement the `shouldComponentUpdate` lifecycle method.

>### Q37. What is the children prop?

- [ ] a property that adds child components to state

- [x] a property that lets you pass components as data to other components

- [ ] a property that lets you set an array as a property

- [ ] a property that lets you pass data to child elements

>### Q38. When using webpack, why would you need to use a loader?

- [ ] to put together physical file folders

- [ ] to process files

- [x] to load external data

- [ ] to load the website into everyone's phone
>### Q39. How do you set a default value for an uncontrolled form field?

- [ ] Use the `value` property

- [x] Use the `defaultValue` property 

- [ ] Use the `default` property

- [ ] It assigns one automatically

>### Q40. What value of button will allow you to pass the name of the person to be hugged?
```js
class Huggable extends React.Component{
  hug(id){
    console.log("hugging " + id);
  }

  render() {
    let name = "kitteh";
    let button = // Missing Code
    return button;
  }
}
```
- [x] `<button onClick={(name) => this.hug(name)>Hug Button</button>`

- [ ] `<button onClick={this.hug(e, name)}>Hug Button</button>`

- [ ] `<button onClick={(e) => hug(e,name)}>Hug Button</button>` 

- [ ] `<button onClick={(e) => this.hug(name, e)}>Hug Button</button>`

>### Q41. When might you use React.PureComponent?

- [ ] when you do not want your component to have props

- [ ] when you have sibling components that need to be compared

- [x] when you want a default implementation of shouldComponentUpdate()

- [ ] when you do not want your component to have state

>### Q42. Why is it a good idea to pass a function to setState instead of an object?

- [ ] It is more functional than an object

- [ ] It makes sure that the object is not mutated

- [ ] It automatically updates a component

- [x] setState is asynchronous and might result in out of sync values.

>### Q43. What do you need to change about this code to get it to run?
```js
class clock extends React.Component {
  render() {
    return <h1>Look at the time: {this.props.time}</h1>;
  }
}
```
- [ ] Add quotes around the return value

- [ ] Remove `this`

- [ ] Remove the render method

- [x] Capitalize `clock`

>### Q44. What do you call a React component that catches JavaScript errors anywhere in the child component tree?

- [ ] error bosses

- [ ] error catchers

- [ ] error helpers

- [x] error boundaries

>### Q45. What can you use to wrap Component imports in order to load them lazily?

- [ ] `React.fallback`

- [ ] `React.split`

- [x] `React.lazy`

- [ ] `React.memo`

>### Q46. Which attribute do you use to replace innerHTML in the browser DOM?

- [ ] injectHTML

- [x] dangerouslySetInnerHTML

- [ ] weirdSetInnerHTML

- [ ] strangeHTML

>### Q47. Which term commonly describes React applications?

- [ ] integrated

- [ ] closed

- [ ] imperative

- [ ] declarative

>### Q48. If you see the following import in a file, what is being used for state management in the component?
`import React, {useState} from 'react';`

- [x] React Hooks

- [ ] stateful components

- [ ] math

- [ ] class components

>### Q49. How do you destructure the properties that are sent to the Dish component?
```js
function Dish(props) {
  return (
    <h1>
      {props.name} {props.cookingTime}
    </h1>
  );
}
```
```js
- [ ] function Dish([name, cookingTime]) { return <h1>{name} {cookingTime}</h1>; }

- [x] function Dish({name, cookingTime}) { return <h1>{name} {cookingTime}</h1>; }

- [ ] function Dish(props) { return <h1>{name} {cookingTime}</h1>; }

- [ ] function Dish(...props) { return <h1>{name} {cookingTime}</h1>; }
```
>### Q50. Currently, `handleClick` is being called instead of passed as a reference. How do you fix this?
```js
<button onClick={this.handleClick()}>Click this</button>
```
```js
- [x] <button onClick={this.handleClick.bind(handleClick}>Click this</button>

- [ ] <button onClick={handleClick()}>Click this</button>

- [ ] <button onClick={this.handleClick}>Click this</button>

- [ ] <button onclick={this.handleClick}>Click this</button>
```
>### Q51. Why might you use useReducer over useState in a React component?

- [ ] when you want to replace Redux

- [x] when you need to manage more complex state in an app

- [ ] when you want to improve performance

- [ ] when you want to break your production app


## Credits: 
* https://www.w3schools.com/ 
* https://google.com
* https://linkedIn.com
* https://reactjs.org/

[(Back to top of the page)](#ReactJs-Assessment)
---
---
---

React.js Assessment
-----------------

#### Q1. If you want to import just the Component from the React library, what syntax do you use?
- `import React.Component from 'react'` 
- `import [ Component ] from 'react'`
- `import Component from 'react'`
- `import { Component } from 'react'` <<<<<--CORRECT

#### Q2. If a function component should always render the same way given the same props, what is a simple performance optimization available for it?
- Wrap it in the React.memo higher-order component. <<<<<--CORRECT
- Implement the useReducer Hook.
- Implement the useMemo Hook.
- Implement the shouldComponentUpdate lifecycle method.

#### Q3. How do you fix the syntax error that results from running this code?
```javascript
const person =(firstName, lastName) => 
       {
            first: firstName,
            last: lastName        
        }    
console.log(person("Jill", "Wolson"))
```
- Wrap the object in parentheses. <<<<<--CORRECT
- Call the function from another file.
- Add a return statement before the first curly brace.
- Replace the with an array

#### Q4. If you see the following import in a file, what is being used for state management in the component?
`import React, {useState} from 'react';`
- React Hooks <<<<<--CORRECT
- stateful components 
- math 
- class components

#### Q5. Using object literal enhancement, you can put values back into and object. When you log person to the console, what is the output?
```javascript
const name = "Rachel";
const age = 31;
const person = {name, age }
console.log(person)
```
- `{{name: "Rachel", age: 31}}`
- `{name: "Rachel", age: 31}` <<<<<--CORRECT
- `{person: "Rachel", person: 31}}`
- `{person: {name: "Rachel", age: 31}}`

#### Q6. What is the testing library most often associated with React?
- Mocha
- Chai
- Sinon
- Jest <<<<<--CORRECT

#### Q7. To get the first item from the array ("cooking") using array destructuring, how do you adjust this line?
```javascript
const topics = ["cooking", "art", "history"]
``` 
- `const first = ["cooking", "art", "history"]`
- `const [] = ["cooking", "art", "history"]`
- `const [, first]["cooking", "art", "history"]`
- `const [first] = ["cooking", "art", "history"]` <<<<<--CORRECT

#### Q8. How do you handle passing through the component tree without having to pass props down manually at every level?
- React Send
- React Pinpoint 
- React Router
- React Context <<<<<--CORRECT

#### Q9. What should the console read when the following code is run?
```javascript
const [, , animal] = ["Horse", "Mouse", "Cat"]
console.log(animal)
```
- Horse
- Cat <<<<<--CORRECT
- Mouse
- undefined

#### 10. What is the name of the tool used to take JSX and turn it into createElement calls?
- JSX Editor
- ReactDOM
- Browser Buddy
- Babel <<<<<--CORRECT

#### 11. Why might you use useReducer over useState in a React component?
- when you want to replace Redux
- when you need to manage more complex state in an app <<<<<--CORRECT
- when you want to improve performance 
- when you want to break your production app

#### 12. Which props from the props object is available to the component with the following syntax?
```javascript
<Message {...props}/>
```
- any that have not changed 
- all of them <<<<<--CORRECT
- child props
- any that have changed

#### 13. Consider the following code from React Router. What do you call :id in the path prop?
```javascript
<Route path="/:id" />
```
- This is a route modal
- This is a route parameter <<<<<--CORRECT
- This is a route splitter
- This is a route link

#### 14. If you created a component called Dish and rendered it to the DOM, what type of element would be rendered?
```javascript
function Dish() {
  return <h1> Mac and Cheese</h1>;
}

ReactDOM.render(
    <Dish />,
    document.getElementById('root')
)
```
- div
- section
- component
- h1 <<<<<--CORRECT

#### 15. What does this React element look like given the following function?
```javascript
React.createElement(
    "h1",
    null,
    "What's happening?"
);
```
- `<h1 props={null}>What's happenning?</h1>`
- `<h1>What's happening?</h1>` <<<<<--CORRECT
- `<h1 id="component">What's happening?</h1>`
- `<h1 id="element">What's happening?</h1>`

#### 16. What property do you need to add the Suspense component in order to display a spinner or loading state?
```javascript
function MyComponent() {
  return (
    <Suspense>
        <div>
            <Message />
        </div>
    </Suspense>
    );   
}
```
- lazy
- loading
- fallback <<<<<--CORRECT
- spinner

#### 17. What do you call the message wrapped in curly braces below?
```javascript
let message = "Hi there";
const element = <p>{message}</p>
```
- a JS function
- a JS element
- a JS expression <<<<<--CORRECT
- a JSX wrapper

#### 18. What can you use to handle code splitting?
- `React.memo`
- `React.split`
- `React.lazy` <<<<<--CORRECT
- `React.fallback`

#### 19. When do you use useLayoutEffect?
- to optimize for all devices
- to complete the update 
- to change the layout of the screen
- when you need the browser to paint before the effect runs <<<<<--CORRECT

#### 20. What is the difference between the click behaviors of these two buttons (assuming that this.handleClick is binded correctly)?
```javascript
A. <button onClick="{this.handleClick}>Click Me</button>"
B. <button onClick="{event => this.handleClick()event}}>Click Me</button>"
```
- Button A will not have access to the event object on click of the button.
- Button B will not fire the handler this.handleClick successfully. <<<<<--CORRECT
- Button A will not fire the handler this.handleClick successfully.
- There is no difference

#### 21. How do you destructure the properties that are sent to the Dish component?
```javascript
function Dish(props) {
   return <h1>{props.name} {props.cookingTime}</h1>
}
```
- `function Dish([name, cookingTime]) {
    return <h1>{name} {cookingTime}</h1>;
}`
- `function Dish({name, cookingTime}) {
    return <h1>{name} {cookingTime}</h1>; 
}` <<<<<--CORRECT

- `function Dish(props) {
    return <h1>{name} {cookingTime}</h1>;
}`
- `function Dish(...props) {
    return <h1>{name} {cookingTime}</h1>;
}`

#### 22. When might you use React.PureComponent?
- when you do not want your component to have props
- when you have sibling components that need to be compared
- when you want to implement shouldComponentUpdate() by default to not update unnecessarily <<<<<--CORRECT
- when you do not want your component to have state

#### 23. Why is it important to avoid copying the values of props into a component's state where possible?
- because you should never mutate state
- because getDerivedStateFromProps() is an unsafe method to use
- because you want to allow a component to update in response to changes in the props <<<<<--CORRECT
- because you want to allow data to flow back up to the parent

#### 24. What is the children prop?
- a property that adds child components to state
- a property that lets you pass components as data to other components <<<<<--CORRECT
- a property that lets you set an array as a property
- a property that lets you pass data to child elements

