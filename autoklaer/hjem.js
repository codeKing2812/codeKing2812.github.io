const firebaseConfig = {
    apiKey: "AIzaSyCHe_tP28D20pYDcd7hpnYQX0bSlv6GvP0",
    authDomain: "autoklaer.firebaseapp.com",
    projectId: "autoklaer",
    storageBucket: "autoklaer.appspot.com",
    messagingSenderId: "1048452991690",
    appId: "1:1048452991690:web:a75b8822b57ee088cf4233",
    measurementId: "G-68QZTDMF1H"
};

firebase.initializeApp(firebaseConfig);
let db = firebase.firestore();

//hent HTML elementer
const topp = document.querySelector('#topp')
const del1 = document.querySelector('#del1')
const del2 = document.querySelector('#del2')
const del3 = document.querySelector('#del3')
const nyttPlagg = document.querySelector('#nyttPlagg')


let klesskap = document.createElement('p');
del3.appendChild(klesskap);

//hent data fra firebase
function hentPlagg() {
    db.collection("Klær").get().then((snapshot) => {
        let alleKlaer = snapshot.docs;
    
        console.log(alleKlaer);
        klesskap.innerText = '';
        for (let plagg of alleKlaer) {
            let p = document.createElement('p');
            klesskap.appendChild(p);
            p.innerText = plagg.data().farge + ' ' + plagg.data().type + ' av ' + plagg.data().stoff;
        }
    });
};
hentPlagg();

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

    typeFelt.addEventListener('keydown', function(e) {
        if(e.key == 'Enter'){
            console.log('type: ' + typeFelt.value)
            typeIn = typeFelt.value;
            navn.innerText = 'farge: ';
            fargeFelt.focus();
        }
    })

    fargeFelt.addEventListener('keydown', function(e) {
        if(e.key == 'Enter'){
            console.log('farge: ' + fargeFelt.value)
            fargeIn = fargeFelt.value;
            navn.innerText = 'stoff: ';
            stoffFelt.focus();
        }
    })

    stoffFelt.addEventListener('keydown', function(e) {
        if(e.key == 'Enter'){
            stoffIn = stoffFelt.value;
            navn.innerText = ' ';
            stoffFelt.blur();
            typeFelt.value = '';
            fargeFelt.value = '';
            stoffFelt.value = '';

            db.collection("Klær").add({
                type: typeIn,
                farge: fargeIn,
                stoff: stoffIn
            });
            hentPlagg();
        }
    })
}



//                      VÆRMELDING

let værFelt = document.createElement('p');
del2.appendChild(værFelt);

fetch('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.3930&lon=5.3242')
    .then(response => response.json())
    // .then(response => console.log(response))
    .then(response => værmelding(response))
    .catch(err => console.error(err))

function værmelding(metApi) {
    let værTime = metApi.properties.timeseries;
    for (let i = 0; i < 10; i++) {
        let p = document.createElement('p');
        værFelt.appendChild(p);
        p.innerText = ('Temperaturen kl ' + værTime[i].time.substr(11,5) + ' blir ' + værTime[i].data.instant.details.air_temperature + ' grader')
    }
};