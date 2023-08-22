const countries = ['norge', 'japan', 'usa', 'italia', 'canada', 'russland', 'sør-korea', 'kina']
const places = ['lillehammer', 'nagano', 'salt lake city', 'torino', 'vancouver', 'sotsji', 'pyeongchang', 'beijing']
const years = ['1994', '1998', '2002', '2006', '2010', '2014', '2018', '2022']

let fasitIndex = 0;
let antallSpilt = 0;
let antallRette = 0;
let sporsmaalType = 0;
let rett = false;
let farge = 'white';
let dobbelRiktig = false;

let sporsmaal = document.getElementById('sporsmaal')
let sjekkKnapp = document.getElementById('sjekkKnapp')
let sporsmaalKnapp = document.getElementById('sporsmaalKnapp')
let svarFelt = document.getElementById('svar')
let scoreFelt = document.getElementById('score')
let fasitFelt = document.getElementById('fasit')
let body = document.querySelector('body')

sporsmaalKnapp.addEventListener("click",newQuestion)
sjekkKnapp.addEventListener("click",checkAnswer)

function skrivUt() {
    for (let i = 0; i < countries.length; i++){
        console.log("Vinter-OL i " + years[i] + " ble arrangert i " +  places[i] + " i " + countries[i])
    }
}
skrivUt()

//starter programmet med et spørsmål
newQuestion()

//Generer nytt spørsmål og legger det ut på siden
function newQuestion() {
    antallSpilt++;
    dobbelRiktig = false;
    fasitIndex = randomIndex();
    farge = 'white'
    svarFelt.value = ''
    sporsmaalType = Math.floor(3*Math.random());
    if (sporsmaalType == 0) {//spørsmål om by
        sporsmaal.innerHTML = 'I hvilken by ble Vinter-OL arrangert året ' + years[fasitIndex] + '?'
    } else if (sporsmaalType == 1) {//spørsmål om land
        sporsmaal.innerHTML = 'I hvilket land ble Vinter-OL arrangert året ' + years[fasitIndex] + '?'
    } else if (sporsmaalType == 2) {//spørsmål om år
        sporsmaal.innerHTML = 'Hvilket år ble Vinter-OL arrangert i ' + places[fasitIndex] + ' i ' + countries[fasitIndex] + '?'
    }
    svarFelt.style.backgroundColor = farge
    scoreFelt.innerHTML = 'Din score: ' + antallRette + ' av ' + antallSpilt
}

//Sjekker om svaret er rett og oppdaterer scoren
function checkAnswer(){
    if (!dobbelRiktig) {//ikke sjekk hvis du fikk rett uten å få nytt spørsmål
        let svar = svarFelt.value.toLowerCase();

        if (sporsmaalType == 0 && places.indexOf(svar) == fasitIndex) {
            rett = true;
        } else if (sporsmaalType == 1 && countries.indexOf(svar) == fasitIndex) {
            rett = true;
        } else if (sporsmaalType == 2 && years.indexOf(svar) == fasitIndex) {
            rett = true;
        } else {rett = false;}

        if (rett) {
            farge = 'green'
            dobbelRiktig = true;
            antallRette++;
            body.style.animation = 'rett 0.3s 10 alternate' //BLINK
        } else {
            farge = 'red'
            body.style.animation = 'feil 0.3s 10 alternate' //BLINK
            fasitFelt.innerText = "Vinter-OL i " + years[fasitIndex] + " ble arrangert i " +  places[fasitIndex] + " i " + countries[fasitIndex]
        }
    svarFelt.style.backgroundColor = farge
    scoreFelt.innerHTML = 'Din score: ' + antallRette + ' av ' + antallSpilt
    }
}

//Velger et tilfeldig OL ved en index
function randomIndex() {
    let random = Math.floor(Math.random() * years.length);
    return random
}