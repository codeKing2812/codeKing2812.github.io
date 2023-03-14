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

//hent data fra firebase og oppdater listen over klær i klesskapet
function oppdaterPlagg() {
    db.collection("Klær").get().then((snapshot) => {
        let alleKlaer = snapshot.docs;
    
        console.log(alleKlaer);
        info3.innerText = '';
        for (let plagg of alleKlaer) {
            let p = document.createElement('p');
            p.setAttribute('class', 'infoBoks');
            info3.appendChild(p);
            p.innerText = plagg.data().farge + ' ' + plagg.data().type + ' av ' + plagg.data().stoff;
        }
    });
};
oppdaterPlagg();

//legg til data til firebase
nyttPlagg.addEventListener('click', leggTilPlagg);
function leggTilPlagg() {

    let navn = document.createElement('label');
    info3.appendChild(navn);
    navn.innerText = 'type: ';

    let typeFelt = document.createElement('input');
    info3.appendChild(typeFelt);

    let fargeFelt = document.createElement('input');
    info3.appendChild(fargeFelt);
    
    let stoffFelt = document.createElement('input');
    info3.appendChild(stoffFelt);

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
            oppdaterPlagg();
        }
    })
}



//------------------------------VÆRMELDING

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


// ---------------------- API

fetch('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.3930&lon=5.3242')
    .then(response => response.json())
    // .then(response => console.log(response))
    .then(response => værmelding(response))
    .catch(err => console.error(err))

function værmelding(metApi) {
    let værTime = metApi.properties.timeseries;
    for (let i = 0; i < 12; i++) {
        let div = document.createElement('div');
        div.setAttribute('class', 'infoBoks');
        info2.appendChild(div);

        let symbol = String(værTime[i].data.next_1_hours.summary.symbol_code);
        console.log(symbol)
        console.log(weatherSymbols.symbol)

        div.innerText += (værTime[i].time.substr(11,5))
        div.innerHTML += ('<br>')
        div.innerText += (værTime[i].data.next_1_hours.summary.symbol_code)
        div.innerHTML += ('<br>')
        div.innerText += (værTime[i].data.next_1_hours.details.precipitation_amount + 'mm')
        div.innerHTML += ('<br>')
        div.innerText += (værTime[i].data.instant.details.air_temperature + '°')
    }
};

