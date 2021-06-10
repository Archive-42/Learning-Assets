// Stretch Task: Extend the base class CuboidMaker with a sub class called CubeMaker.  Find out the formulas for volume and surface area for cubes and create those methods using the dimension properties from CuboidMaker.  Test your work by logging out your volume and surface area.

class CuboidMaker {
  constructor(attrs) {
    this.length = attrs.length;
    this.width = attrs.width;
    this.height = attrs.height;
  }
  volume() {
    return this.length * this.width * this.height;
  }
  surfaceArea() {
    return (
      2 *
      (this.length * this.width +
        this.length * this.height +
        this.width * this.height)
    );
  }
}

class CubeMaker extends CuboidMaker {
  constructor(attrs) {
    super(attrs);
  }
  volume() {
    return this.length * this.width * this.height;
  }
  surfaceArea() {
    return 6 * (this.length * this.length);
  }
}

const cuboid = new CuboidMaker({ length: 4, width: 5, height: 5 });
const cube = new CubeMaker({ length: 3, width: 3, height: 3 });

// Test your volume and surfaceArea methods by uncommenting the logs below:
console.log(cuboid.volume()); // 100
console.log(cuboid.surfaceArea()); // 130

console.log(cube.volume()); // 27
console.log(cube.surfaceArea()); // 54
