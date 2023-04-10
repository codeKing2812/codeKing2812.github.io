//henter HTML elementer
const topp = document.querySelector('#topp');
const del1 = document.querySelector('#del1');
const del2 = document.querySelector('#del2');
const del3 = document.querySelector('#del3');

//                                  A
//                                  I
//                               GENERELL
//--------------------------------------------------------------------------------------------------------
//                               ANBEFALINGER
//                                  I
//                                  V




//                                  A
//                                  I
//                             ANBEFALINGER
//--------------------------------------------------------------------------------------------------------
//                               KLESSKAP
//                                  I
//                                  V


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

// lager den første diven i rekken av klær for å kunne ha annen info
let førsteDiv = document.createElement('div');
førsteDiv.setAttribute('class', 'infoBoks');

// lager pluss-knappen for å legge til nye plagg, uten å legge den inn i info3
let nyttPlagg = document.createElement('button');
nyttPlagg.setAttribute('id', 'nyttPlagg')
nyttPlagg.innerText = '+';

// hent data fra firebase og oppdater listen over klær i klesskapet
function oppdaterPlagg() {
    db.collection("Klær").get().then((snapshot) => {

        let alleKlaer = snapshot.docs;
        console.log(alleKlaer);

        info3.innerHTML = '';
        førsteDiv.innerHTML = '';

        info3.appendChild(førsteDiv); // legger pluss-knappen inn først i rekken
        førsteDiv.appendChild(nyttPlagg);

        for (let plagg of alleKlaer) {
            let div = document.createElement('div');
            div.setAttribute('class', 'infoBoks');
            info3.appendChild(div);

            let plaggTekst = document.createElement('p');
            div.appendChild(plaggTekst);
            plaggTekst.setAttribute('class', 'plaggTekst');
            plaggTekst.innerText = plagg.data().type + ' av ' + plagg.data().stoff;

            div.innerHTML += '<div id="klesfarge1" style="background-color:' + plagg.data().farge1 + '">&nbsp;'
            + '<div id="klesfarge2" style="background-color:' + plagg.data().farge2 + '"></div> </div>';
        }
    });
};
oppdaterPlagg();




function nyOption (felt, option) { // en funksjon for å legge til options i en form
    let z = document.createElement('option');
    z.setAttribute('value', option);  
    felt.appendChild(z);
    let t = document.createTextNode(option);
    z.appendChild(t);
}

//legg til data til firebase
nyttPlagg.addEventListener('click', leggTilPlagg);
function leggTilPlagg() {

    førsteDiv.innerHTML = '';

    let typeTekst = document.createElement('p');
    førsteDiv.appendChild(typeTekst);
    typeTekst.setAttribute('class', 'skjemaTekst');
    typeTekst.innerText = 'Type plagg:';

    let typeVelger = document.createElement('select');
    førsteDiv.appendChild(typeVelger);

    nyOption(typeVelger, 't-skjorte');
    nyOption(typeVelger, 'genser');
    nyOption(typeVelger, 'skjorte');
    nyOption(typeVelger, 'ytterjakke');
    nyOption(typeVelger, 'bukse');
    nyOption(typeVelger, 'sko');


    let stoffTekst = document.createElement('p');
    førsteDiv.appendChild(stoffTekst);
    stoffTekst.setAttribute('class', 'skjemaTekst');
    stoffTekst.innerText = 'Stofftype:';

    let stoffVelger = document.createElement('select');
    førsteDiv.appendChild(stoffVelger);

    nyOption(stoffVelger, 'bomull')
    nyOption(stoffVelger, 'ull')
    nyOption(stoffVelger, 'kordfløyel')
    nyOption(stoffVelger, 'dongeri')
    nyOption(stoffVelger, 'skinn')
    nyOption(stoffVelger, 'fleece')
    nyOption(stoffVelger, 'glatt polyester')


    let fargeVelger1Tekst = document.createElement('p');
    førsteDiv.appendChild(fargeVelger1Tekst);
    fargeVelger1Tekst.setAttribute('class', 'skjemaTekst');
    fargeVelger1Tekst.innerText = 'Hovedfarge:';

    let fargeVelger1 = document.createElement('input');
    fargeVelger1.setAttribute('type', 'color');
    fargeVelger1.innerText = 'farge';
    førsteDiv.appendChild(fargeVelger1);


    let fargeVelger2Tekst = document.createElement('p');
    førsteDiv.appendChild(fargeVelger2Tekst);
    fargeVelger2Tekst.setAttribute('class', 'skjemaTekst');
    fargeVelger2Tekst.innerText = 'Andrefarge:';

    let fargeVelger2 = document.createElement('input');
    fargeVelger2.setAttribute('type', 'color');
    fargeVelger2.innerText = 'farge';
    førsteDiv.appendChild(fargeVelger2);
    

    let sendKnapp = document.createElement('button');
    sendKnapp.innerText = 'lagre';
    førsteDiv.appendChild(sendKnapp);

    sendKnapp.addEventListener('click',function () {
        db.collection("Klær").add({
            type: typeVelger.value,
            farge1: fargeVelger1.value,
            farge2: fargeVelger2.value,
            stoff: stoffVelger.value
        });
        oppdaterPlagg();
    })
};


//                                  A
//                                  I
//                               KLESSKAP
//--------------------------------------------------------------------------------------------------------
//                              VÆRMELDING
//                                  I
//                                  V


//  API
fetch('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.3930&lon=5.3242')
    .then(response => response.json())
    // .then(response => console.log(response))
    .then(response => værmelding(response))
    .catch(err => console.error(err))

function værmelding(metApi) {

    let værTime = metApi.properties.timeseries;

    for (let i = 0; i < 16; i++) {

        let div = document.createElement('div');
        div.setAttribute('class', 'infoBoks');
        info2.appendChild(div);
        
        let symbol = værTime[i].data.next_1_hours.summary.symbol_code;
        console.log(weatherSymbols[symbol]);

        let tid = document.createElement('p');
        div.appendChild(tid);
        tid.innerText = (værTime[i].time.substr(11,5))
        
        let img = document.createElement('img');
        img.setAttribute('src', 'Bilder/værsymboler/' + weatherSymbols[symbol] + '.png');
        img.setAttribute('class', 'værsymboler')
        div.appendChild(img);

        let nedbør = document.createElement('p');
        div.appendChild(nedbør);
        nedbør.innerText = (værTime[i].data.next_1_hours.details.precipitation_amount + 'mm')
        
        let temp = document.createElement('p');
        div.appendChild(temp);
        temp.innerText = (værTime[i].data.instant.details.air_temperature + '°')
    }
};

const weatherSymbols = { // VÆRSYMBOLER
    clearsky_day: '01d',
    clearsky_night: '01n',
    clearsky_polartwilight: '01m',
    fair_day: '02d',
    fair_night: '02n',
    fair_polartwilight: '02m',
    partlycloudy_day: '03d',
    partlycloudy_night: '03n',
    partlycloudy_polartwilight: '03m',
    cloudy: '04',
    rainshowers_day: '05d',
    rainshowers_night: '05n',
    rainshowers_polartwilight: '05m',
    rainshowersandthunder_day: '06d',
    rainshowersandthunder_night: '06n',
    rainshowersandthunder_polartwilight: '06m',
    sleetshowers_day: '07d',
    sleetshowers_night: '07n',
    sleetshowers_polartwilight: '07m',
    snowshowers_day: '08d',
    snowshowers_night: '08n',
    snowshowers_polartwilight: '08m',
    rain: '09',
    heavyrain: '10',
    heavyrainandthunder: '11',
    sleet: '12',
    snow: '13',
    snowandthunder: '14',
    fog: '15',
    sleetshowersandthunder_day: '20d',
    sleetshowersandthunder_night: '20n',
    sleetshowersandthunder_polartwilight: '20m',
    snowshowersandthunder_day: '21d',
    snowshowersandthunder_night: '21n',
    snowshowersandthunder_polartwilight: '21m',
    rainandthunder: '22',
    sleetandthunder: '23',
    lightrainshowersandthunder_day: '24d',
    lightrainshowersandthunder_night: '24n',
    lightrainshowersandthunder_polartwilight: '24m',
    heavyrainshowersandthunder_day: '25d',
    heavyrainshowersandthunder_night: '25n',
    heavyrainshowersandthunder_polartwilight: '25m',
    lightssleetshowersandthunder_day: '26d',
    lightssleetshowersandthunder_night: '26n',
    lightssleetshowersandthunder_polartwilight: '26m',
    heavysleetshowersandthunder_day: '27d',
    heavysleetshowersandthunder_night: '27n',
    heavysleetshowersandthunder_polartwilight: '27m',
    lightssnowshowersandthunder_day: '28d',
    lightssnowshowersandthunder_night: '28n',
    lightssnowshowersandthunder_polartwilight: '28m',
    heavysnowshowersandthunder_day: '29d',
    heavysnowshowersandthunder_night: '29n',
    heavysnowshowersandthunder_polartwilight: '29m',
    lightrainandthunder: '30',
    lightsleetandthunder: '31',
    heavysleetandthunder: '32',
    lightsnowandthunder: '33',
    heavysnowandthunder: '34',
    lightrainshowers_day: '40d',
    lightrainshowers_night: '40n',
    lightrainshowers_polartwilight: '40m',
    heavyrainshowers_day: '41d',
    heavyrainshowers_night: '41n',
    heavyrainshowers_polartwilight: '41m',
    lightsleetshowers_day: '42d',
    lightsleetshowers_night: '42n',
    lightsleetshowers_polartwilight: '42m',
    heavysleetshowers_day: '43d',
    heavysleetshowers_night: '43n',
    heavysleetshowers_polartwilight: '43m',
    lightsnowshowers_day: '44d',
    lightsnowshowers_night: '44n',
    lightsnowshowers_polartwilight: '44m',
    heavysnowshowers_day: '45d',
    heavysnowshowers_night: '45n',
    heavysnowshowers_polartwilight: '45m',
    lightrain: '46',
    lightsleet: '47',
    heavysleet: '48',
    lightsnow: '49',
    heavysnow: '50',
};