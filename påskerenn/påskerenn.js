const oversikt = document.querySelector('#oversikt');
const tabell = document.querySelector('#tabell');
document.querySelector('#skjema_nyPerson').addEventListener('submit', nyPerson);
document.querySelector('#slettKnapp').addEventListener('click', slettForrige);
tabell.addEventListener('click', rediger);
document.querySelector('#plussKnapp').addEventListener('click', nyRad);


let personer = [
    {navn: 'Hogne', alder: 23, akt1: 0, akt2: 0, akt3: 0, tot: 0},
    {navn: 'Linus', alder: 17, akt1: 0, akt2: 0, akt3: 0, tot: 0},
    {navn: 'JoBjo', alder: 42, akt1: 0, akt2: 0, akt3: 0, tot: 0},
    {navn: 'Britt-Helen', alder: 29, akt1: 0, akt2: 0, akt3: 0, tot: 0},
];

oppdaterDeltakerListe();

function nyPerson(event) {
    event.preventDefault(); // single page app som betyr at vi ikke forlater nettsiden
    let innNavn = document.querySelector('#navn').value;
    let innAlder = document.querySelector('#alder').value;
    personer.push({navn: innNavn, alder: innAlder, akt1: 0, akt2: 0, akt3: 0, tot: 0});

    oppdaterDeltakerListe();
};

function oppdaterDeltakerListe() {
    tabell.innerHTML = '<tr> <th>Deltaker</th> <th>Alder</th> <th>Akt. 1</th> <th>Akt. 2</th> <th>Akt. 3</th> <th>Total</th> </tr>';
    
    for (let person of personer) {
        let rad = document.createElement('tr');
        tabell.appendChild(rad);
        person.tot = person.akt1 + person.akt2 + person.akt3;
        rad.innerHTML += '<td>' + person.navn + '</td>' + '<td>' + person.alder + '</td>' + '<td>' + person.akt1 + '</td>' + '<td>' + person.akt2 + '</td>' + '<td>' + person.akt3 + '</td>' + '<td>' + person.tot + '</td>';
    };
    console.log(personer);
};

function slettForrige() {
    personer.pop();
    oppdaterDeltakerListe();
    console.log(personer);
};

let elements;
let redigerFelt;
function rediger() {
    elements = document.querySelectorAll(':hover');
    elements[elements.length - 1].innerHTML = '<input type="text" autocomplete="off" id="rediger">';
    redigerFelt = document.querySelector('#rediger');
    redigerFelt.focus();
    redigerFelt.addEventListener('keydown', sluttRediger);
}

function sluttRediger(e) {
    if (e.key == 'Enter') {
        console.log(redigerFelt.value)
        elements[elements.length - 1].innerHTML = '<td>' + redigerFelt.value + '</td>';
    }
}

function nyRad() {
    personer.push({navn: '', alder: '', akt1: 0, akt2: 0, akt3: 0, tot: 0});
    oppdaterDeltakerListe();
}