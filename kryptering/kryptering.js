const inTekst = document.querySelector('#inTekst');
const inNøkkel = document.querySelector('#nøkkel');
const utKryptert = document.querySelector('#kryptert');
const arr_kryptertTekst = [];
let nøkkel = 0;
let tekst = '';

inTekst.onkeydown = function(e){
    if(e.keyCode == 13){
        cæsarKrypter();
    }
};

inNøkkel.onkeydown = function(e){
    if(e.keyCode == 13){
        cæsarKrypter();
    }
};

function cæsarKrypter() {
    nøkkel = Number(inNøkkel.value);
    tekst = inTekst.value;

    console.log('tekst:', tekst);
    console.log('nøkkel:', nøkkel);
    console.log('lengde på tekst:', tekst.length);

    for (i = 0; i < inTekst.value.length; i++) {
        arr_kryptertTekst.push(Number(tekst.charCodeAt(i)));
    };
    for (i = 0; i < arr_kryptertTekst.length; i++) {
        arr_kryptertTekst[i] += nøkkel;
    };

    console.log('koder:', arr_kryptertTekst); 
    
    if (inTekst.value != '' && inNøkkel.value != '') {
        utKryptert.innerText = arr_kryptertTekst;
    } else {
        utKryptert.innerText = 'fyll ut begge feltene først!';
    };
};