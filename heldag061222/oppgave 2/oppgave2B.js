let terning = 0;
let forsøk = 0;

while (terning != 6) {
    terning = Math.floor(Math.random() * 6) + 1;
    console.log(terning)
    forsøk++;
}
if (forsøk < 3) {
    console.log('Flaks, lotto neste!')
} else if (forsøk == 3 || forsøk == 4) {
    console.log('Tja, som forventet')
} else {console.log('Uflaks!')}