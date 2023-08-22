const inTekst = document.querySelector('#inTekst');
const inNøkkel = document.querySelector('#nøkkel');
const utKryptert = document.querySelector('#kryptert');
const kopiKrypt = document.querySelector('#kopiKrypt');
let arr_kryptertTekst = [];
let str_kryptertTekst = '';
let nøkkel = 0;
let tekst = '';

inTekst.addEventListener('keydown', function(e){
    if(e.key == 'Enter'){
        inNøkkel.focus();
        krypter();
    }
});
inNøkkel.addEventListener('keydown', function(e){
    if(e.key == 'Enter'){
        krypter();
    }
});

function krypter() {
    nøkkel = Number(inNøkkel.value);
    tekst = inTekst.value;
    arr_kryptertTekst = [];

    console.log('tekst:', tekst);
    console.log('nøkkel', nøkkel);

    for (i = 0; i < tekst.length; i++) { //for alle tegn i teksten
        arr_kryptertTekst.push(tekst.charCodeAt(i)); //legg til bokstaven som charCode i arrayen

        arr_kryptertTekst[i] += nøkkel; //legg til nøkkelen
        console.log('kryptering:', arr_kryptertTekst[i])

        arr_kryptertTekst[i] = String.fromCharCode(arr_kryptertTekst[i]); //gjør ny charCode om til en vanlig bokstav
        console.log('kryptert bokstav:', arr_kryptertTekst[i]);
    };

    console.log('kryptert tekst:', arr_kryptertTekst); 
    
    if (inTekst.value && inNøkkel.value) { // hvis du har fylt inn begge så vis den krypterte meldingen
        str_kryptertTekst = '';
        utKryptert.innerText = '';

        for (tegn of arr_kryptertTekst) {
            str_kryptertTekst += tegn;
        }
        utKryptert.innerHTML = str_kryptertTekst;
        kopiKrypt.innerText = 'Kopier kryptert tekst';
    } else {
        utKryptert.innerText = 'fyll ut begge feltene først!';
    };
};

kopiKrypt.addEventListener('click', function(){
    navigator.clipboard.writeText(str_kryptertTekst); // kopier teksten
    kopiKrypt.innerText = 'Kryptert tekst er kopiert!';
});

//--------------BRUTE FORCE---------------

const inKrypt = document.querySelector('#inKrypt');
const bruteForslag = document.querySelector('#bruteForslag');
const bruteAlt = document.querySelector('#bruteAlt');
const visAlt = document.querySelector('#visAlt');
let arr_bruteAlt = [];
let str_bruteAlt = '';
let bruteNøkkel = 0;
let kode = '';

inKrypt.addEventListener('keydown', function(e){
    if(e.key == 'Enter'){
        bruteForce();
    }
});

function bruteForce() {
    bruteForslag.innerHTML = 'Forslag:';
    bruteAlt.innerHTML = 'Alternativer:';
    arr_bruteAlt = [];
    kode = inKrypt.value;
    console.log('kode:', kode);


    bruteNøkkel = -100;
    while (bruteNøkkel < 100) {
        //prøv med alle nøkler fra -500 til +500
        let sannsynlighet = 0;

        for (i = 0; i < kode.length; i++) { //for alle tegn i teksten
            arr_bruteAlt.push(kode.charCodeAt(i)); //legg til bokstaven som charCode i arrayen
            console.log('charcode oprinnelig:', arr_bruteAlt[i]);

            arr_bruteAlt[i] += bruteNøkkel; //legg til nøkkelen
            console.log('charcode bF:', arr_bruteAlt[i]);

            if ( arr_bruteAlt[i] == 32 
                || ( 64 < arr_bruteAlt[i] && arr_bruteAlt[i] < 91 )
                || ( 96 < arr_bruteAlt[i] && arr_bruteAlt[i] < 123 )
                ) { //hvis innenfor det engelske alfabetet
                sannsynlighet++;
            }

            arr_bruteAlt[i] = String.fromCharCode(arr_bruteAlt[i]); //gjør ny charCode om til en vanlig bokstav
            console.log('bokstav bF:', arr_bruteAlt[i]);
        };
        console.log('tekst bF:', arr_bruteAlt); 
        
        sannsynlighet = Math.floor(sannsynlighet *99/arr_bruteAlt.length) //gjør om sannsynligheten til prosent

        str_bruteAlt = '';
        for (tegn of arr_bruteAlt) {
            str_bruteAlt += tegn;
        } // gjør arrayen om til en string

        if (sannsynlighet > 0) {
            str_bruteAlt += ' ' + sannsynlighet;
            
        } else {
            bruteAlt.innerHTML += '<br>' + str_bruteAlt;
        }


        arr_bruteAlt = [];
        bruteNøkkel++;
    };

};

visAlt.addEventListener('click', function() {
    bruteAlt.style.display = 'inline';
});

// kopiBrute.addEventListener('click', function(){
//     navigator.clipboard.writeText(str_kryptertTekst); // kopier teksten
//     kopiBrute.innerText = 'Kryptert tekst er kopiert!';
// });