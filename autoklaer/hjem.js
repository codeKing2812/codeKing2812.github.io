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

const topp = document.querySelector('#topp')
const del1 = document.querySelector('#del1')
const del2 = document.querySelector('#del2')
const del3 = document.querySelector('#del3')

db.collection("Klær").get().then((snapshot) => {
    let alleKlaer = snapshot.docs;
  
    console.log(alleKlaer);

    for (let plagg of alleKlaer) {
        let p = document.createElement('p');
        del3.appendChild(p);
        p.innerText = plagg.data().farge + ' ' + plagg.data().type + ' av ' + plagg.data().stoff;
    }
});