      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['month', 'Sales', 'Expenses'],
          ['January',  1000,      400],
          ['February',  1170,      460],
          ['March',  660,       1120],
          ['Aprile',  660,       1120],
          ['May',  1030,      540],
          ['June',  1030,      540],
          ['Jule',  1030,      540],
          ['August',  1030,      540],
          ['September',  1030,      540],
          ['October',  1030,      540],
          ['November',  1030,      540],
          ['December',  1030,      540]



        ]);

        var options = {
          title: 'Company Performance',
          hAxis: {title: 'months',  titleTextStyle: {color: '#333'}},
          vAxis: {minValue: 0}
        };

        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
