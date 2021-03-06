---
id: 5a23c84252665b21eecc8041
title: Sum of a series
challengeType: 5
forumTopicId: 302333
dashedName: sum-of-a-series
---

# --description--

Compute the **n**<sup>th</sup> term of a [series](https://en.wikipedia.org/wiki/Series 'mathematics'), i.e. the sum of the **n** first terms of the corresponding [sequence](https://en.wikipedia.org/wiki/sequence). Informally this value, or its limit when **n** tends to infinity, is also called the _sum of the series_, thus the title of this task. For this task, use: $S*n = \\sum*{k=1}^n \\frac{1}{k^2}$ and compute $S\_{1000}$ This approximates the [zeta function](https://en.wikipedia.org/wiki/Riemann zeta function) for S=2, whose exact value $\\zeta(2) = {\\pi^2\\over 6}$ is the solution of the [Basel problem](https://en.wikipedia.org/wiki/Basel problem).

# --instructions--

Write a function that take $a$ and $b$ as parameters and returns the sum of $a^{th}$ to $b^{th}$ members of the sequence.

# --hints--

`sum` should be a function.

```js
assert(typeof sum == 'function');
```

`sum(1, 100)` should return a number.

```js
assert(typeof sum(1, 100) == 'number');
```

`sum(1, 100)` should return `1.6349839001848923`.

```js
assert.equal(sum(1, 100), 1.6349839001848923);
```

`sum(33, 46)` should return `0.009262256361481223`.

```js
assert.equal(sum(33, 46), 0.009262256361481223);
```

`sum(21, 213)` should return `0.044086990748706555`.

```js
assert.equal(sum(21, 213), 0.044086990748706555);
```

`sum(11, 111)` should return `0.08619778593108679`.

```js
assert.equal(sum(11, 111), 0.08619778593108679);
```

`sum(1, 10)` should return `1.5497677311665408`.

```js
assert.equal(sum(1, 10), 1.5497677311665408);
```

# --seed--

## --seed-contents--

```js
function sum(a, b) {}
```

# --solutions--

```js
function sum(a, b) {
  function fn(x) {
    return 1 / (x * x);
  }
  var s = 0;
  for (; a <= b; a++) s += fn(a);
  return s;
}
```
