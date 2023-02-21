const firebaseConfig = {
    apiKey: "AIzaSyCHe_tP28D20pYDcd7hpnYQX0bSlv6GvP0",
    authDomain: "autoklaer.firebaseapp.com",
    projectId: "autoklaer",
    storageBucket: "autoklaer.appspot.com",
    messagingSenderId: "1048452991690",
    appId: "1:1048452991690:web:a75b8822b57ee088cf4233",
    measurementId: "G-68QZTDMF1H"
};

// import firebase from 'firebase';
// const firebase = require("firebase");
// Required for side-effects
// require("firebase/firestore");

firebase.initializeApp(firebaseConfig);
let db = firebase.firestore();

//hent HTML elementer
const topp = document.querySelector('#topp')
const del1 = document.querySelector('#del1')
const del2 = document.querySelector('#del2')
const del3 = document.querySelector('#del3')
const nyttPlagg = document.querySelector('#nyttPlagg')

//hent data fra firebase
function hentPlagg() {
    db.collection("Klær").get().then((snapshot) => {
        let alleKlaer = snapshot.docs;
    
        console.log(alleKlaer);

        for (let plagg of alleKlaer) {
            let p = document.createElement('p');
            del3.appendChild(p);
            p.innerText = plagg.data().farge + ' ' + plagg.data().type + ' av ' + plagg.data().stoff;
        }
    });
};

//legg til data til firebase
nyttPlagg.addEventListener('click', leggTilPlagg);
function leggTilPlagg() {

    let navn = document.createElement('label');
    del3.appendChild(navn);
    navn.innerText = 'type: ';

    let typeFelt = document.createElement('input');
    del3.appendChild(typeFelt);

    let fargeFelt = document.createElement('input');
    del3.appendChild(fargeFelt);
    
    let stoffFelt = document.createElement('input');
    del3.appendChild(stoffFelt);

    let typeIn = '';
    let fargeIn = '';
    let stoffIn = '';

    typeFelt.focus();

    typeFelt.addEventListener('keydown', n1);
    function n1(e) {
        if(e.key == 'Enter'){
            typeIn = inputFelt.value;
            inputFelt.value = '';
            navn.innerText = 'farge: ';
            fargeFelt.focus();
        }
    };

    fargeFelt.addEventListener('keydown', function(e) {
        if(e.key == 'Enter'){
            fargeIn = inputFelt.value;
            inputFelt.value = '';
            navn.innerText = 'stoff: ';
            stoffFelt.focus();
        }
    })
    stoffFelt.addEventListener('keydown', function(e) {
        if(e.key == 'Enter'){
            stoffIn = inputFelt.value;
            inputFelt.value = '';
            navn.innerText = ' ';
            stoffFelt.blur();

            db.collection("Klær").add({
                type: inType,
                farge: inFarge,
                stoff: inStoff
            });
        }
    })


    // inputFelt.addEventListener('keydown', function(e) {
    //     if (e.key == 'Enter') {
    //         inType = inputFelt.value;
    //         inputFelt.value = '';
    //         navn.innerText = 'farge: ';
    //         hvilketFelt++;
    //     }
    //     if (e.key == 'Enter' && hvilketFelt == 1) {
    //         inFarge = inputFelt.value;
    //         inputFelt.value = '';
    //         navn.innerText = 'stoff: ';
    //         hvilketFelt++;
    //     }
    //     if (e.key == 'Enter' && hvilketFelt == 2) {
    //         inStoff = inputFelt.value;
            
    //         db.collection("Klær").add({
    //             type: inType,
    //             farge: inFarge,
    //             stoff: inStoff
    //         });
    //     }
    // })
}

