let personer = [
    {navn: 'per', født: 1984},
    {navn: 'ole', født: 2006},
    {navn: 'espen', født: 2010},
    {navn: 'mikkel', født: 1964},
    {navn: 'roger', født: 2003},
    {navn: 'lise', født: 1999},
];

for (let person of personer) {
    // person.alder = new Date().getFullYear() - person.født;
    // if (person.alder < 18)
    // console.log(person.navn + ' er under 18 år');

    person.bool = true;
};
personer[2].bool = false;

console.log(personer.every(sjekk))

function sjekk(denne) {
    if (denne.bool) {
        return true;
    }
};