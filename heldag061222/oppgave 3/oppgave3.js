let inputA = document.querySelector('#inputA');
let inputB = document.querySelector('#inputB');
let inputH = document.querySelector('#inputH');
let utAreal = document.querySelector('#utAreal');
let feilA = document.querySelector('#feilA');
let feilB = document.querySelector('#feilB');
let feilH = document.querySelector('#feilH');

let areal = 0;
let a = 0;
let b = 0;
let h = 0;

inputA.focus(); // start med å fokusere på felt a

inputA.onkeydown = function(e){
    if(e.keyCode == 13){ // enter
        a = Number(inputA.value.replaceAll(' ','').replaceAll(',','.')); //fjerner  mellomrom, gjør komma til punktum, og gjør stringen til et tall
        if (!a) {
            feilA.innerText = 'Det du skrev inn er ikke et tall!'
        } else {feilA.innerText = ''}

        regnUt();
        inputB.focus(); // flytt fokus videre
    }
};

inputB.onkeydown = function(e){
    if(e.keyCode == 13){ // enter
        b = Number(inputB.value.replaceAll(' ','').replaceAll(',','.'));//fjerner  mellomrom, gjør komma til punktum, og gjør stringen til et tall
        if (!b) {
            feilB.innerText = 'Det du skrev inn er ikke et tall!'
        } else {feilB.innerText = ''}

        regnUt();
        inputH.focus(); // flytt fokus videre
    }
};

inputH.onkeydown = function(e){
    if(e.keyCode == 13){ // enter
        h = Number(inputH.value.replaceAll(' ','').replaceAll(',','.'));//fjerner  mellomrom, gjør komma til punktum, og gjør stringen til et tall
        if (!h) {
            feilH.innerText = 'Det du skrev inn er ikke et tall!'
        } else {feilH.innerText = ''}

        regnUt();
        inputH.blur(); // fjern fokus
    }
};

function regnUt() {
    console.log(a, b, h);
    
    if (a && b && h) {
        areal = (a+b)*h/2;
        utAreal.style.color = 'black';
        utAreal.innerText = areal;
        console.log(areal);
    } else {
        utAreal.style.color = 'red';
        utAreal.innerText = 'Du må fylle ut alle feltene først!';

    }
}
