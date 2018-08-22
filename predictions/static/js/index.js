// $(document).ready(function() {
// $('#device_types').append('<option value="' + )
// }

$("#get_data").click(function(){
    drawData()
});

$(document).ready(drawData);

// drawData();

function drawData() {

    var ctx = $("#myChart");
    ctx.canvas.width = 50;
    ctx.canvas.height = 50;
    real_data = [{t:"2018-8-22 2018 12:00", y:1}, {t: new Date("2018-8-22 2018 12:30"), y:2}, {t:new Date("2018-8-22 2018 12:30"), y: 3}];
    // real_data=[1, 2, 3];
    var myLineChart = new Chart(ctx, {
        // type: 'line',
        // data: {
        //     datasets:[{
        //         data:[
        //             {x: new Date("January"), y:1},
        //             {x:new Date("February"), y:2}
        //        ],
        //         label: "Predictions",
        //         xAxisID:"Time",
        //         yAxisID: "Predictions",
        //         backgroundColor: window.chartColors.red,
        //         borderColor: window.chartColors.red
        //
        //     }]
        //
        // },
        type: 'line',
        data: {
            labels: [new Date('2018-8-22 12:00:00'), new Date('2018-8-22 12:30:00'), new Date('2018-8-22 13:00:00')],
            datasets: [{
                label: 'Real',
                backgroundColor: "rgba(0,0,200,1)",
                borderColor: "rgba(0,0,200,1)",
                data: real_data,
                fill: false
            },
                {
                label: 'Predicted',
                    backgroundColor: "rgba(200,255,0,1)",
                    borderColor: "rgba(200,255,0,1)",
                data: [
                    1, 15, 3
                ],
                    fill: false
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            tooltips: {
                mode: 'index',
                intersect: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    },
                    type: 'time',
                    time: {
                        unit: 'hour'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }

        }

    });
}