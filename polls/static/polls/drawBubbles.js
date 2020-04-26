

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
        elem.innerHTML = ""
      
        var divHeight = elem.offsetHeight;
        var divWidth = elem.offsetWidth;
      
        var params = { width: divWidth, height: divHeight, type:Two.Types.canvas};
        var two = new Two(params).appendTo(elem);
      
        var verticalSpace = divHeight/10;
        var horizontalSpace = divWidth/10;
      
        var x = 2*horizontalSpace;
        var y = 2*verticalSpace;
      
        var indicator = null
      
        for (const [key, value] of Object.entries(indicators)){
            if(x>= ((7/8)*divWidth) ){
                x = 2*horizontalSpace
                y+= 3*verticalSpace
            }
            indicator = metadata[key]
      
            var circle = two.makeCircle(x, y, ((value*indicator["conversion"])/10)*horizontalSpace);
            circle.fill = indicator["color"];
            circle.stroke = 'orangered'; // Accepts all valid css color
            circle.linewidth = 5;
            console.log(typeof(value))
            two.makeText(indicator["name"] + ': ' + Math.round(value) + ' ' + indicator["unit"], x, y+ ((value*indicator["conversion"])/10)*horizontalSpace + 0.5*verticalSpace)
      
            x+=3*horizontalSpace
        }
      
        two.update();
     }
     
     
}

    