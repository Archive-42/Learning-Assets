const express = require("express");
const app = express();
const port = 3000;
const mongoose = require("mongoose");

const Review = require("./models/review");

app.use(express.json());

const uri = process.env.DB_URI;

mongoose.connect(uri, { useNewUrlParser: true });
const db = mongoose.connection;

db.once("open", () => {
  console.log("MongoDB database connection established successfully");
});

app.get("/", (req, res) => {
  Review.find()
    .then((reviews) => res.json(reviews))
    .catch((err) => res.status(400).json("Error: " + err));
});

/* 
Create a new review with these properties and assign it to a variable named "newReview". Here is an example of creating a new exercise: 
```
const newExercise = new Exercise({
  username,
  description,
  duration,
  date,
});
```
*/

app.post("add", (req, res) => {
  const movie_title = req.body.movie_title;
  const review = req.body.review;
  const stars = Number(req.body.stars);
  const date = Date.parse(req.body.date);
});

app.listen(port, () => console.log(`Review server listening on port ${port}!`));
