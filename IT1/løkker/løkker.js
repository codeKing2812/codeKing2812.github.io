let teller = 1; 

while (teller < 10) {
    console.log(teller); 
    teller++;
};

let JBnavn = ['JB', 'Jo Bjørnar', 'Jobis', 'Jobemann', 'JoBoy'];

for (i = 0; i < JBnavn.length; i++) {
    console.log(JBnavn[i])
};

console.table(JBnavn);
JBnavn[1] = 'Jo Bjørnis';
console.log(JBnavn);

for (i = 0; i < JBnavn.length; i++) {
    console.log('-');
    for (bokstav of JBnavn[i]) {
        console.log(bokstav);
    };
};

function randomTallFraTil (min, maks) {
    min = Math.ceil(min);
    maks = Math.floor(maks);
    return Math.floor(Math.random() * (maks - min + 1) + min);
};

console.log('Tilfeldig tall fra 1 til 10:', randomTallFraTil(1, 10));

let tilfeldigTallArray = [];

for (i = 0; i < 10; i++) {
    tilfeldigTallArray[i] = randomTallFraTil(1, 20);
}

console.log(tilfeldigTallArray);


