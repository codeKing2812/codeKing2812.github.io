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
const firebase = require("firebase");
// Required for side-effects
require("firebase/firestore");

firebase.initializeApp(firebaseConfig);

let db = firebase.firestore();

db.collection("Klær").get().then((snapshot) => {
    let dokumenter = snapshot.docs;
  
    console.log(dokumenter);
});