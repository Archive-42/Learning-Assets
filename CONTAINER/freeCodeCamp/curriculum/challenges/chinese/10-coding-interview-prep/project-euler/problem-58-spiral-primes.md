---
id: 5900f3a61000cf542c50feb9
title: 'Problem 58: Spiral primes'
challengeType: 5
forumTopicId: 302169
dashedName: problem-58-spiral-primes
---

# --description--

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

<div style='text-align: center;'>
  <strong><span style='color: red;'>37</span></strong> 36 35 34 33 32 <strong><span style='color: red;'>31</span></strong><br>
  38 <strong><span style='color: red;'>17</span></strong> 16 15 14 <strong><span style='color: red;'>13</span></strong> 30<br>
  39 18  <strong><span style='color: red;'>5</span></strong>  4  <strong><span style='color: red;'>3</span></strong> 12 29<br>
  40 19  6  1  2 11 28<br>
  41 20  <strong><span style='color: red;'>7</span></strong>  8  9 10 27<br>
  42 21 22 23 24 25 26<br>
  <strong><span style='color: red;'>43</span></strong> 44 45 46 47 48 49<br>
</div>

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

# --hints--

`spiralPrimes()` should return a number.

```js
assert(typeof spiralPrimes() === 'number');
```

`spiralPrimes()` should return 26241.

```js
assert.strictEqual(spiralPrimes(), 26241);
```

# --seed--

## --seed-contents--

```js
function spiralPrimes() {
  return true;
}

spiralPrimes();
```

# --solutions--

```js
// solution required
```
