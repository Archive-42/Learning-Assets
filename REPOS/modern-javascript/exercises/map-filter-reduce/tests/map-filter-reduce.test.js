/* eslint no-extend-native: 0 */
import * as coll from '../src/collection-utils';

describe('collection-utils.js exports', () => {
  test('must export a map function', () => {
    expect(typeof coll.map).toBe('function');
  });

  test('must export a reduce function', () => {
    expect(typeof coll.reduce).toBe('function');
  });

  test('must export a filter function', () => {
    expect(typeof coll.filter).toBe('function');
  });

  test('must export a forEach function', () => {
    expect(typeof coll.forEach).toBe('function');
  });
});

describe('collection-utils#forEach', () => {
  let c = 0;
  test('Sum up [1, 2, 3]', () => {
    coll.forEach([1, 2, 3], x => {
      c += x;
    });
    expect(c).toBe(6);
  });
});

describe('collection-utils#map', () => {
  test('Square [1, 2, 3]', () => {
    expect(coll.map([1, 2, 3], x => x * x)).toMatchObject([1, 4, 9]);
  });
});

describe('collection-utils#filter', () => {
  test('filter [1, 2, 3] where x > 2', () => {
    expect(coll.filter([1, 2, 3], x => x > 2)).toMatchObject([3]);
  });
});

describe('collection-utils#reduce', () => {
  test('Sum up [1, 2, 3]', () => {
    expect(coll.reduce([1, 2, 3], (x, acc) => acc + x, 0)).toBe(6);
  });
});
