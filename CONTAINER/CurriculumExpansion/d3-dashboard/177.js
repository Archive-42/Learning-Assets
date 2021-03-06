const svgMargin = 60,
  svgWidth = 700,
  svgHeight = 500,
  twitterColor = "#7cd9d1",
  tumblrColor = "#f6dd71",
  instagramColor = "#fd9b98";

const lineGraph = d3
  .select(".dashboard")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

const yScale = d3
  .scaleLinear()
  .domain([0, 5000])
  .range([svgHeight - svgMargin, svgMargin]);

const xScale = d3
  .scaleLinear()
  .domain([2012, 2020])
  .range([svgMargin, svgWidth - svgMargin]);

const yAxis = d3.axisLeft(yScale).ticks(6, "~s");

const xAxis = d3.axisBottom(xScale).tickFormat(d3.format("")).tickPadding(10);

lineGraph
  .append("g")
  .call(yAxis)
  .attr("transform", `translate(${svgMargin}, 0)`)
  .style("font", "10px verdana");

lineGraph
  .append("g")
  .call(xAxis)
  .attr("transform", `translate(0, ${svgHeight - svgMargin})`)
  .selectAll("text")
  .style("transform", "translate(-12px, 0) rotate(-50deg)")
  .style("text-anchor", "end")
  .style("cursor", "pointer")
  .style("font", "10px verdana");

const twitterLine = d3.line().x((d) => d.year);

/*
    The problem here is that the `svg` is only 700 wide, so setting the `x` values to the year will put them off the chart. You need to pass each year to the `xScale` and it will create `x` values based on your scale.

    In the "`d` function", return the `xScale` function and pass it the year you already added.
  */
