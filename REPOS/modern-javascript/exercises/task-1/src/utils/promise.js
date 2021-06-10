// @ts-check

/**
 * Check to see whether a value is a promise
 *
 * @param {object} x value to check
 * @returns {boolean} true if the value is found to be a promise
 */
export function isPromise(x) {
  return x && typeof x.then === 'function';
}

/**
 * Returns a promise that will resolve in a particular amount of time
 *
 * @param {number} time time to wait (in ms)
 * @returns {Promise} a promise that will resolve after time
 */
export function wait(time) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve();
    }, time);
  });
}
