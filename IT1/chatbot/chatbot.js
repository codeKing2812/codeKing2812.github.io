var submitKnapp = document.querySelector('#submit');
var chatSvar = document.querySelector('#chatSvar');
var chatInput = document.querySelector('#chatInput');
var forstår = false;

chatSvar.innerHTML += '<br>';

function submitFunksjon () {
    console.log('submit');
    let inputTekst = document.querySelector('#inputTekst').value;
    inputTekst = inputTekst.toLowerCase();
    console.log(inputTekst);
    forstår = false;
    
    chatInput.innerText += inputTekst;
    chatInput.innerHTML += '<br><br>';
    
    if (inputTekst.indexOf('hei') > -1) {
        forstår = true;
        chatSvar.innerText += 'Hei! ';
    }
    if (inputTekst.indexOf('ball') > -1) {
        forstår = true;
        chatSvar.innerText += 'Jeg liker baller. ';
    } 
    if (inputTekst.indexOf('hva heter du') > -1) {
        forstår = true;
        chatSvar.innerText += 'Jeg heter Pedro. Hva heter du?';
    }
    if (inputTekst.indexOf('jeg heter') > -1) {
        forstår = true;
        chatSvar.innerText += 'Det var et stygt navn. ';
    }
    if (forstår == false) {
        chatSvar.innerText += 'Jeg forstår ikke hva du mener. ';
    }
    chatSvar.innerHTML += '<br><br>'
}

submitKnapp.addEventListener('click', submitFunksjon);