anychart.onDocumentReady(function () {
    anychart.data.loadCsvFile(
      'https://ForesightAPI.sentientplatypu.repl.co/getNumbers/' + document.URL.split("/").pop(),
      function (data) {
        // create data table on loaded data
        var dataTable = anychart.data.table();
        csvSettings = {ignoreFirstRow: true, columnsSeparator: ",", rowsSeparator: " "};
        dataTable.addData(data);
  
        // map loaded data for the candlestick series
        var mapping = dataTable.mapAs({
          "open": 1,
          "high": 2,
          "low": 3,
          "close": 4,
          "ohlc":7
        });

        var chart = anychart.stock();

        // create first plot on the chart
        var plot = chart.plot(0);

        // set grid settings
        plot.yGrid(true).xGrid(true).yMinorGrid(false).xMinorGrid(false);
        plot.xGrid().stroke({
            color: "#707070",
            thickness: 1
          });
        plot.yGrid().stroke({
        color: "#707070",
        thickness: 1
        });

        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", (constants.API_URL + "/getInfo/" + document.URL.split("/").pop()), false ); // false for synchronous request
        xmlHttp.send( null );
        var name =  JSON.parse(xmlHttp.response).companyName;

        var series = plot.candlestick(mapping).name(name)


        series.legendItem().iconType('rising-falling');
        series.risingFill("#00FF19")
        series.risingStroke("rgba(0,0,0,0)");
        series.fallingFill("#FF0000")
        series.fallingStroke("rgba(0,0,0,0)");




        // create scroller series with mapped data
        chart.scroller().candlestick(mapping);
        // set chart selected date/time range
        chart.selectRange('2020-11-27', '2021-11-26');

        // create range picker
        var rangePicker = anychart.ui.rangePicker();

        // init range picker
        rangePicker.render(chart);

        // create range selector
        var rangeSelector = anychart.ui.rangeSelector();

        // init range selector
        rangeSelector.render(chart);
        // sets the title of the chart

        // set container id for the chart
        chart.container('graph');

        //STYLES
        chart.background().fill("#141414")

        // initiate chart drawing
        chart.draw();
        console.log("finished draing chart")
        changeTableStyle()
      }
    );
  });