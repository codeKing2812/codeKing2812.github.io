const utskrift = document.querySelector('#utskrift');
const inputTall = document.querySelector('#inputTall');
var base = 5;
var tier;
var x;

function svar () { 
    x = inputTall.value;

    console.log('input: ',x);
    console.log('base: ',base);
    console.log('konvertert med parseInt til titallssytem: ', parseInt(x, base));
    console.log('konvertert selv til base system: ', selvKonverter(x,base));
    console.log('-');
    // utskrift.innerText = selvKonverter(x, base);
};

function selvKonverter (x, base) {
    tier = Math.floor(x / base);
    hundrer = Math.floor(tier / base);
    return 10*tier + (x - base*tier);
};

 