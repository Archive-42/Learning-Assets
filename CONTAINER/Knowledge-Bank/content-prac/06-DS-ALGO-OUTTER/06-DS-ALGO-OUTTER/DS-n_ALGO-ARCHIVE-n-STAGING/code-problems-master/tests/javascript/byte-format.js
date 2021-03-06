var expect = require("chai").expect;
var byteFormat = require("../../solutions/javascript/byte-format");

describe("Byte format", function () {
  it("should show B format", function () {
    expect(byteFormat(1022)).to.equal("1022 B");
  });

  it("should show KB format", function () {
    expect(byteFormat(10221)).to.equal("9.98 KB");
  });

  it("should show KB format rounded to 3 digital", function () {
    expect(byteFormat(10221, 3)).to.equal("9.981 KB");
  });

  it("should show MB format", function () {
    expect(byteFormat(1022932324)).to.equal("975.54 MB");
  });

  it("should show GB format", function () {
    expect(byteFormat(1022932123237)).to.equal("952.68 GB");
  });

  it("should show TB format", function () {
    expect(byteFormat(1022932453333234)).to.equal("930.35 TB");
  });

  it("should show PB format", function () {
    expect(byteFormat(1022932453333234444)).to.equal("908.55 PB");
  });

  it("should show EB format", function () {
    expect(byteFormat(1022932453333234444324)).to.equal("887.25 EB");
  });

  it("should show ZB format", function () {
    expect(byteFormat(1022932453333234444324454)).to.equal("866.46 ZB");
  });

  it("should show YB format", function () {
    expect(byteFormat(10243245333323444432445431)).to.equal("8.47 YB");
  });

  it("should show YB format when number larger than 1024YB", function () {
    expect(byteFormat(232932453333234444324454333424324)).to.equal(
      "192677209.43 YB"
    );
  });
});
