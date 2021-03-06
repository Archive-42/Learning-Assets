function drawDashboard(year) {
  d3.select(".dashboard").html("");
  const index = data.findIndex((d) => d.year === year);

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
    .style("font", (d) => (d === year ? "bold 10px verdana" : "10px verdana"))
    .on("mouseover", (d) => drawDashboard(d));

  const twitterLine = d3
    .line()
    .x((d) => xScale(d.year))
    .y((d) => yScale(d.followers.twitter));

  lineGraph
    .append("path")
    .attr("d", twitterLine(data))
    .attr("stroke", twitterColor)
    .attr("stroke-width", 3)
    .attr("fill", "transparent");

  const tumblrLine = d3
    .line()
    .x((d) => xScale(d.year))
    .y((d) => yScale(d.followers.tumblr));

  lineGraph
    .append("path")
    .attr("d", tumblrLine(data))
    .attr("stroke", tumblrColor)
    .attr("stroke-width", 3)
    .attr("fill", "transparent");

  const instagramLine = d3
    .line()
    .x((d) => xScale(d.year))
    .y((d) => yScale(d.followers.instagram));

  lineGraph
    .append("path")
    .attr("d", instagramLine(data))
    .attr("stroke", instagramColor)
    .attr("stroke-width", 3)
    .attr("fill", "transparent");

  lineGraph
    .selectAll("twitter-circles")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", (d) => xScale(d.year))
    .attr("cy", (d) => yScale(d.followers.twitter))
    .attr("r", 6)
    .attr("fill", "white")

    /*
      Similar to how you made the text bold for the label of the displayed year; change the `fill` of the `twitter-circles` to use a `d` function that returns the `twitterColor` when `d.year` equals `year`, and leave it `white` if it doesn't.
    */

    .attr("stroke", twitterColor)
    .style("cursor", "pointer")
    .on("mouseover", (d) => drawDashboard(d.year));

  lineGraph
    .selectAll("tumblr-circles")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", (d) => xScale(d.year))
    .attr("cy", (d) => yScale(d.followers.tumblr))
    .attr("r", 6)
    .attr("fill", "white")
    .attr("stroke", tumblrColor)
    .style("cursor", "pointer");

  lineGraph
    .selectAll("instagram-circles")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", (d) => xScale(d.year))
    .attr("cy", (d) => yScale(d.followers.instagram))
    .attr("r", 6)
    .attr("fill", "white")
    .attr("stroke", instagramColor)
    .style("cursor", "pointer");

  const rightDashboard = d3.select(".dashboard").append("div");

  const pieGraph = rightDashboard
    .append("svg")
    .attr("width", 200)
    .attr("height", 200)
    .style("position", "relative")
    .style("left", "20px");

  const pieArc = d3.arc().outerRadius(100).innerRadius(0);

  const pieColors = d3
    .scaleOrdinal()
    .domain(data[index].followers)
    .range([twitterColor, tumblrColor, instagramColor]);

  const pie = d3.pie().value((d) => d.value);

  const pieGraphData = pieGraph
    .selectAll("pieSlices")
    .data(pie(d3.entries(data[index].followers)))
    .enter()
    .append("g")
    .attr("transform", "translate(100, 100)");

  pieGraphData
    .append("path")
    .attr("d", pieArc)
    .attr("fill", (d) => pieColors(d.data.key))
    .attr("stroke", "white")
    .attr("stroke-width", 2);

  pieGraphData
    .selectAll("pieSliceText")
    .data(pie(d3.entries(data[index].followers)))
    .enter()
    .append("text")
    .text(
      (d) =>
        `${Math.round(
          (d.data.value / d3.sum(d3.values(data[index].followers))) * 100
        )}%`
    )
    .attr("transform", (d) => `translate(${pieArc.centroid(d)})`)
    .style("text-anchor", "middle")
    .style("font", "10px verdana");

  const legend = rightDashboard
    .append("table")
    .attr("width", 200)
    .attr("height", 120)
    .style("font", "12px verdana")
    .style("position", "relative")
    .style("top", "30px");

  const legendTitle = legend
    .append("thead")
    .append("tr")
    .append("th")
    .text("2020 followers")
    .attr("colspan", 3)
    .style("position", "relative")
    .style("left", "20px");

  const legendRows = legend
    .append("tbody")
    .selectAll("tr")
    .data(d3.entries(data[index].followers))
    .enter()
    .append("tr");

  legendRows
    .append("td")
    .text((d) => d.key)
    .attr("align", "right");

  legendRows
    .append("td")
    .attr("align", "center")
    .append("div")
    .style("width", "16px")
    .style("height", "16px")
    .style("background-color", (d) => pieColors(d.key));

  legendRows
    .append("td")
    .text((d) => d.value)
    .attr("align", "left");
}

drawDashboard(2020);
