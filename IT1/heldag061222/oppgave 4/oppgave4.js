let solheimviken = [];
let danmarksplass = [];
let solheimvikenSnitt = 0;
let danmarksplassSnitt = 0;
let lengde = 1440;

for (let i = 0; i < lengde; i++) {
    solheimviken.push(Math.round(Math.random()*150))// lager tilfeldige verdier og legger de til i arrayen
    danmarksplass.push(Math.round(Math.random()*150))

    solheimvikenSnitt += solheimviken[i]; // lager en stor variabel med den totale verdien av arrayen
    danmarksplassSnitt += danmarksplass[i];
}

console.log('Liste fra Solheimviken:', solheimviken)
console.log('Liste fra Danmarksplass:', danmarksplass)

//-------------------- GJENNOMSNITTLIGE VERDIER --------------------------------------------------------------
console.log('')
console.log('GJENNOMSNITTLIGE VERDIER')

solheimvikenSnitt = solheimvikenSnitt/lengde; // deler den totale summen på 1440 for å finne gjennomsnitt
danmarksplassSnitt = danmarksplassSnitt/lengde;

console.log('Gjennomsnittlig mengde svevestøv i Solheimsviken:',solheimvikenSnitt)
console.log('Gjennomsnittlig mengde svevestøv på Danmarksplass:', danmarksplassSnitt)

if (solheimvikenSnitt < danmarksplassSnitt) { // sjekker hvilken snittverdi som er høyest
    console.log('Det er høyest konsentrasjon av svevestøv på Danmarksplass')
} else if (solheimvikenSnitt > danmarksplassSnitt) {
    console.log('Det er høyest konsentrasjon av svevestøv i Solheimsviken')
} else {
    console.log('Det er nøyaktig like høy konsentrasjon av svevestøv på Danmarksplass som i Solheimsviken')
}

//-------------------- STØRSTE VERDIER --------------------------------------------------------------
console.log('')
console.log('STØRSTE VERDIER')

console.log('Den største verdien funnet i Solheimsviken var:',største(solheimviken));
console.log('Den største verdien funnet på Danmarksplass var:',største(danmarksplass));

if (største(solheimviken) < største(danmarksplass)) { // sjekker hvilken maksverdi som er høyest
    console.log('Den største verdien funnet totalt var på Danmarksplass')
} else if (største(solheimviken) > største(danmarksplass)) {
    console.log('Den største verdien funnet totalt var i Solheimsviken')
} else {
    console.log('Den største verdien var lik for både Solheimsviken og Danmarksplass')
}

function største(array) {
    array.sort(function(a, b){return b - a}); // sorterer listen fra størst til minst
    return array[0];
}

//-------------------- MINSTE VERDIER --------------------------------------------------------------
console.log('')
console.log('MINSTE VERDIER')

console.log('Den minste verdien funnet i Solheimsviken var:',minste(solheimviken));
console.log('Den minste verdien funnet på Danmarksplass var:',minste(danmarksplass));

if (minste(solheimviken) > minste(danmarksplass)) { // sjekker hvilken minimumsverdi som er minst
    console.log('Den minste verdien funnet totalt var på Danmarksplass')
} else if (minste(solheimviken) < minste(danmarksplass)) {
    console.log('Den minste verdien funnet totalt var i Solheimsviken')
} else {
    console.log('Den minste verdien var lik for både Solheimsviken og Danmarksplass')
}

function minste(array) {
    array.sort(function(a, b){return a - b}); // sorterer listen fra minst til størst
    return array[0];
}

//-------------------- LUK UT VERDIER --------------------------------------------------------------
console.log('')
console.log('LUK UT VERDIER')

function lukUt(array,grenseverdi) {
    while (array.indexOf(grenseverdi) == -1) {
        grenseverdi--; // hvis ikke grenseverdien finnes i listen blir den mindre helt til den finnes
    }

    array.sort(function(a, b){return b - a}) // sorterer fra størst til minst
    array.splice(0, array.indexOf(grenseverdi)) // fjerner alle verdier i listen fra index 0 til indexen til 140
    return array
    
}
console.log('Oppdatert liste fra Solheimsviken sortert og uten verdier over 140:', lukUt(solheimviken, 140));
console.log('Oppdatert liste fra Danmarksplass sortert og uten verdier over 140:', lukUt(danmarksplass, 140));