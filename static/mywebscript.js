let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const response = JSON.parse(xhttp.responseText);
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    //xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    //xhttp.send();
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify({ statement: textToAnalyze }));
}
