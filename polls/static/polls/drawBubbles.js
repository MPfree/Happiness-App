

function drawBubbles(indicators){
    var indicators_metadata = 0;

    $.get("/static/polls/happiness_indicator_metadata.json", function parse(data){
        console.log(typeof(data))
        indicators_metadata = data
        console.log(indicators_metadata)
        loadBubbles(indicators, indicators_metadata)
    })

function loadBubbles(indicators, metadata){
    var elem = document.getElementById('bubbles');
    var params = { width: 1000, height: 1000 };
    var two = new Two(params).appendTo(elem);

    var x = 150
    var y = 100

    var indicator = null

    for (const [key, value] of Object.entries(indicators)){
        if(x>750){
            x = 150
            y+=225
        }
        indicator = metadata[key]

        var circle = two.makeCircle(x, y, (value*indicator["conversion"])*20);
        circle.fill = indicator["color"];
        circle.stroke = 'orangered'; // Accepts all valid css color
        circle.linewidth = 5;
        console.log(typeof(value))
        two.makeText(indicator["name"] + ': ' + Math.round(value) + ' ' + indicator["unit"], x, y+(value*indicator["conversion"])*20 + 10)

        x+=225
    }

    two.update();
}
}

    