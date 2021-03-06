---
id: 5900f3931000cf542c50fea5
title: 'Problem 38: Pandigital multiples'
challengeType: 5
forumTopicId: 302042
dashedName: problem-38-pandigital-multiples
---

# --description--

Take the number 192 and multiply it by each of 1, 2, and 3:

<div style='margin-left: 4em;'>
  192 × 1 = 192<br>
  192 × 2 = 384<br>
  192 × 3 = 576<br>
</div>

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ... , `n`) where `n` > 1?

# --hints--

`pandigitalMultiples()` should return a number.

```js
assert(typeof pandigitalMultiples() === 'number');
```

`pandigitalMultiples()` should return 932718654.

```js
assert.strictEqual(pandigitalMultiples(), 932718654);
```

# --seed--

## --seed-contents--

```js
function pandigitalMultiples() {
  return true;
}

pandigitalMultiples();
```

# --solutions--

```js
function pandigitalMultiples() {
  function get9DigitConcatenatedProduct(num) {
    // returns false if concatenated product is not 9 digits
    let concatenatedProduct = num.toString();
    for (let i = 2; concatenatedProduct.length < 9; i++) {
      concatenatedProduct += num * i;
    }
    return concatenatedProduct.length === 9 ? concatenatedProduct : false;
  }

  function is1to9Pandigital(num) {
    const numStr = num.toString();

    // check if length is not 9
    if (numStr.length !== 9) {
      return false;
    }

    // check if pandigital
    for (let i = 9; i > 0; i--) {
      if (numStr.indexOf(i.toString()) === -1) {
        return false;
      }
    }
    return true;
  }

  let largestNum = 0;
  for (let i = 9999; i >= 9000; i--) {
    const concatenatedProduct = get9DigitConcatenatedProduct(i);
    if (
      is1to9Pandigital(concatenatedProduct) &&
      concatenatedProduct > largestNum
    ) {
      largestNum = parseInt(concatenatedProduct);
      break;
    }
  }
  return largestNum;
}
```
