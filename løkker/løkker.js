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