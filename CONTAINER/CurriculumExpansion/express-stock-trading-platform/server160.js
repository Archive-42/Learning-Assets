const express = require("./node_modules/express");
const app = express();

app.listen(3000, function () {
  console.log("Your app is listening on port 3000.");
});

app.get("/hi", (req, res) => {
  res.send("Hi there trader!");
});

const prices = {
  ABC: 48.83,
  DEF: 2.98,
  GHI: 3.99,
  JKL: 99,
  MNO: 45.38,
  OPQ: 0.48,
  RST: 9.32,
  UVW: 10.94,
  XYZ: 5.32,
};

const checkTickerAndShares = (req, res, next) => {};

// As previously mentioned, the user may send the ticker route parameter in lowercase, uppercase, or a combination of both.
// Modify the 'req.params.ticker' so that it is all in uppercase, like `req.params.ticker = req.params.ticker.toUpperCase()`

app.get("/buy/:ticker/:shares", checkTickerAndShares, (req, res) => {
  const ticker = req.params.ticker;
  const shares = req.params.shares;
  const total = shares * prices[ticker];

  res.send(
    `Transaction complete, you purchased ${shares} shares of ${ticker} at $${prices[ticker]}/share for a total of $${total}.`
  );
});

app.get("/sell/:ticker/:shares", checkTickerAndShares, (req, res) => {
  const ticker = req.params.ticker;
  const shares = req.params.shares;
  const total = shares * prices[ticker];
  res.send(
    `Transaction complete, you sold ${shares} shares of ${ticker} at $${prices[ticker]}/share for a total of $${total}.`
  );
});

app.get("/price/:ticker", (req, res) => {
  const ticker = req.params.ticker.toUpperCase();

  if (!(ticker in prices)) {
    res.send("Error: the ticker you entered is invalid.");
  } else {
    res.send(`The price of ${ticker} is $${prices[ticker]}.`);
  }
});
