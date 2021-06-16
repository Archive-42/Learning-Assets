import { Color } from '../src/color.js';
import * as colorUtils from '../src/color-utils.js';

test('color-utils.js module exports a function hexToRgb', () => {
  expect(typeof colorUtils.hexToRgb).toBe('function');
});

test('color-utils.js module exports a function rgbToHex', () => {
  expect(typeof colorUtils.rgbToHex).toBe('function');
});

test('color-utils.js / rgbToHex(255, 0, 0) --> "ff0000"', () => {
  expect(colorUtils.rgbToHex(255, 0, 0)).toBe('ff0000');
});

test('color-utils.js / rgbToHex(255, 255, 255) --> "ffffff"', () => {
  expect(colorUtils.rgbToHex(255, 255, 255)).toBe('ffffff');
});

test('color-utils.js / hexToRgb("ff0000") -> {r: 255, g: 0, b: 0}', () => {
  expect(colorUtils.hexToRgb('ff0000')).toMatchObject({ r: 255, g: 0, b: 0 });
});

test('color-utils.js / hexToRgb("f00") -> {r: 255, g: 0, b: 0}', () => {
  expect(colorUtils.hexToRgb('f00')).toMatchObject({ r: 255, g: 0, b: 0 });
});

test('color.r, color.g and color.b properties should all be numbers', () => {
  let color = new Color(255, 255, 255);
  expect(typeof color.r).toBe('number');
  expect(typeof color.g).toBe('number');
  expect(typeof color.b).toBe('number');
});

test('color.hex property should be a string', () => {
  let color = new Color(255, 255, 255);
  expect(typeof color.hex).toBe('string');
});

test('r=255, g=255, b=255 --> color.hex.toLowerCase() should be "ffffff"', () => {
  let color = new Color(255, 255, 255);
  expect(color.hex.toLowerCase()).toBe('ffffff');
});

test('r=255, g=0, b=0 --> color.hex.toLowerCase() should be "ff0000"', () => {
  let color = new Color(255, 0, 0);
  expect(color.hex.toLowerCase()).toBe('ff0000');
});

test('r=299, g=0, b=0 --> color.hex.toLowerCase() should be "ff0000"', () => {
  let color = new Color(299, 0, 0);
  expect(color.hex.toLowerCase()).toBe('ff0000');
});

test('r=100, g=100, b=-30 --> color.hex.toLowerCase() should be "646400"', () => {
  let color = new Color(100, 100, -30);
  expect(color.hex.toLowerCase()).toBe('646400');
});

test('hex=aa0000 --> colors {r: 170, g: 0, b: 0}', () => {
  let color = new Color(100, 100, -30);
  color.hex = 'aa0000';

  expect(color.r).toBe(170);
  expect(color.g).toBe(0);
  expect(color.b).toBe(0);
});

test('hex=aaee33 --> colors {r: 170, g: 238, b: 51}', () => {
  let color = new Color(100, 100, -30);

  color.hex = 'aaee33';

  expect(color.r).toBe(170);
  expect(color.g).toBe(238);
  expect(color.b).toBe(51);
});

test('hex=c49 --> colors {r: 204, g: 68, b: 153}', () => {
  let color = new Color(100, 100, -30);

  color.hex = 'c49';

  expect(color.r).toBe(204);
  expect(color.g).toBe(68);
  expect(color.b).toBe(153);
});

test('Color.fromHex("f00") --> Color(r: 255, g: 0, b: 0)', () => {
  let color = Color.fromHex('f00');

  expect(color.r).toBe(255);
  expect(color.g).toBe(0);
  expect(color.b).toBe(0);
});
