let terning = 0; 
//linjen over lager en ny variabel, kaller den 'terning' og setter verdien lik 0.

while (terning != 6) {
    //linjen over gjør dette:
    //det som ligger innenfor while-loopen skal skje så lenge variabelen terning ikke er lik 6. 
    //det vil altså skje helt til terning er lik 6, og så stoppe.

    terning = Math.floor(Math.random() * 6) + 1; 
    //linjen over gjør dette:
    //Math.random velger et 'tilfeldig' tall mellom 0 og 1, deretter ganger vi det med 6 slik at vi får et tall mellom 0 og 6. 
    //Dette tallet er et desimaltall, så vi bruker math.floor for å runde ned til nærmeste heltall. vi har nå et heltall fom. 0 tom. 5
    //Vi legger til 1 for å få fom. 1 tom. 6, og setter variabelen 'terning' lik dette tallet.

    console.log(terning);
    //linjen over skriver ut variabelen 'terning' i konsollen
}
