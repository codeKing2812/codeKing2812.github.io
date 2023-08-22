// let mykey = konfigurasjon.API_KEY;

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDw9ulf4heNcgY520GQqEUuwgnfMzkuY00", // NB: Min nøkkel ligg i ei separat fil som eg ikkje deler her. Du kan bruke din eigen direkte, om du vil.
    authDomain: "huskeliste-93739.firebaseapp.com",
    projectId: "huskeliste-93739",
    storageBucket: "huskeliste-93739.appspot.com",
    messagingSenderId: "394163639681",
    appId: "1:394163639681:web:7a45cc7f99593f31560480"
};

// Initialize Firebase
//const app = initializeApp(firebaseConfig);
firebase.initializeApp(firebaseConfig);
// Lager en referanse til databasen
let db = firebase.firestore();

// Henter HTML-elementer
let listeEl = document.querySelector("#liste");
let inputEl = document.querySelector("input");
let knappEl = document.querySelector("button");

// Legger til lytter på knappen
knappEl.addEventListener("click", leggTilHuskepunkt);

// Henter data. Når dataene er ferdig hentet, starter "then"-biten
db.collection("huskeliste").get().then((snapshot) => {
    // Henter ut dokumentene
    let dokumenter = snapshot.docs;

    // Skriver dokumentene til konsollen
    console.log(dokumenter);

    // Går gjennom dokumentene og sender dem videre      
    for (let i = 0; i < dokumenter.length; i++) {
        visHuskeElement(dokumenter[i]);
    }
});

let ulEl = document.querySelector("ul");

// Funksjon som viser hvert element
function visHuskeElement(dokument) {
    // Lager et <div>-element med klassen "listediv"
    let divEl = document.createElement("div");
    divEl.setAttribute("class", "listediv");  
    
    // Lager et <div>-element til selve huskelisteteksten, og legger til dokumentets id i "data-id"
    let divEl2 = document.createElement("div");
    divEl2.setAttribute("data-id", dokument.id);
    divEl2.innerHTML = dokument.data().husketekst;
    
    // Hvis punktet er utført (ferdig), legger vi til klassen "ferdig"
    if (dokument.data().ferdig) {
        divEl2.setAttribute("class", "ferdig");
    }

    // Legger til en lytter for å endre tilstand fra uferdig til ferdig (og omvendt)
    divEl2.addEventListener("click", endreTilstand);

    // Legger til det andre <div>-elementet i det første
    divEl.appendChild(divEl2);

    // Lager en sletteknapp med klassen "avbryt" og legger til dokumentets id i "data-id"
    let slettKnappEl = document.createElement("button");
    slettKnappEl.setAttribute("class", "avbryt");
    slettKnappEl.innerHTML = "Slett";
    slettKnappEl.setAttribute("data-id", dokument.id);
    slettKnappEl.addEventListener("click", slettHuskepunkt);

    // Legger til sletteknappen i det første <div>-elementet
    divEl.appendChild(slettKnappEl);

    // Legger til elementet på siden
    listeEl.appendChild(divEl);   
}

// Lytter etter endringer i databasen
db.collection("huskeliste").onSnapshot(snapshot => {
    // Kaller funksjonen oppdater(), som lager huskelisten på nytt
    oppdater();
});

function oppdater() {
    // Henter data. Når første bit er ferdig hentet, starter "then"-biten
    db.collection("huskeliste").get().then((snapshot) => {
        // Henter ut dokumentene
        let dokumenter = snapshot.docs;

        // Tømmer listeelementet (<div>-elementet der huskelisten lages)
        listeEl.innerHTML = "";

        // Går gjennom dokumentene og lager et element for hvert av dem      
        for (let i = 0; i < dokumenter.length; i++) {
            visHuskeElement(dokumenter[i]);
        }
    })
}

// Funksjon som legger til en ting å huske på
function leggTilHuskepunkt() {
    db.collection("huskeliste").add({
        husketekst: inputEl.value,
        ferdig: false    
    });
}

// Funksjon som endrer tilstanden til et element i huskelisten
function endreTilstand(e) {
    // Finner id-en til klikket element
    let id = e.target.getAttribute("data-id");

    // Henter dokumentet med samme id fra databasen
    db.collection("huskeliste").doc(id).get().then(doc => {
        let status = doc.data().ferdig;

        // Bytter verdien til status (status er lik det omvendte av status)
        status = !status;
        
        // Oppdaterer elementet
        db.collection("huskeliste").doc(id).update({
            ferdig: status
        });
    });
}

// Funksjon som sletter et element fra huskelisten
function slettHuskepunkt(e) {
    // Finner id-en til elementet som ble klikket
    let id = e.target.getAttribute("data-id");

    // Sletter elementet
    db.collection("huskeliste").doc(id).delete();
}