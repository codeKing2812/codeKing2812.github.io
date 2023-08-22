var inputSvar;
var svar;
var r;
var vinner;
var dScore = 0;
var bScore = 0;
// definer variabler

function steinSaksPapir (inputSvar) {
    var r = Math.floor(Math.random()*3+1);
    if (r==1) {svar='stein'} 
    else if (r==2) {svar='saks'} 
    else{svar='papir'} //velg stein, saks eller papir tilfeldig

    if (inputSvar==1 && r==2 || 
        inputSvar==2 && r==3 || 
        inputSvar==3 && r==1) {vinner='deg!'; bScore++;}
    else if (inputSvar==1 && r==3 || 
        inputSvar==2 && r==1 || 
        inputSvar==3 && r==2) {vinner='datamaskinen!'; dScore++;}
    else {vinner='ingen!'} //sjekk hvem som vant

    document.getElementById("data").innerHTML = 'loading...';
    setTimeout(function(){
        document.getElementById("data").innerHTML = svar;
        document.getElementById("vinner").innerHTML = vinner;
    }, 200); //lag en falsk innlasting før resultatet blir vist

    document.getElementById("dScore").innerHTML = dScore;
    document.getElementById("bScore").innerHTML = bScore; //oppdater scoren
}