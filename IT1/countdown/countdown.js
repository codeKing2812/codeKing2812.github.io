var sekunder;
var tellNedInterval;

var lofiMusikk = new Audio('lyd/lofi.mp3')
var happyMusikk = new Audio('lyd/happy.mp3')

function start() {
sekunder = prompt('hvor lenge skal nedtellinge vare?');
tellNedInterval = setInterval(tellNed, 1000); // start intervallet
document.getElementById('tid').style.color = 'black';
}

function tellNed() {
    document.querySelector("#tid").innerText = sekunder;

    if (sekunder <= 3) {
        console-console.log('3 sek'); //log for feilsøking
        document.getElementById('tid').style.color = 'red';
    }

    if (sekunder <= 0) {
        document.querySelector("#ferdig").innerText = 'FERDIG!';
        document.getElementById('tid').style.color = 'green';
        lofiMusikk.pause(); //stopp bakgrunnsmusikken
        happyMusikk.play(); //start gladmusikk
        clearInterval(tellNedInterval); //avslutt loopen
    }
    sekunder--;
}

function bakgrunnsMusikk () {
    happyMusikk.pause();
    lofiMusikk.play();
}

document.body.addEventListener('click',bakgrunnsMusikk)