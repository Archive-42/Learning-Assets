//This is a function that returns the circumference of a circle
//this keyword is not associated with any object
var circumference = function () {
  return 2 * Math.PI * this.radius;
};
//define circle objects
var circle1 = { x: 100, y: 200, radius: 50 };
var circle2 = { x: 200, y: 300, radius: 25 };

//invoke the function
//this = circle1
console.log(circumference.call(circle1)); //314.159
//this = circle2
console.log(circumference.call(circle2)); //157.079
