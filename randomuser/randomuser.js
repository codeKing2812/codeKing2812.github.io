let antallBrukere = 0;
let inputAntall = document.createElement('input');
document.body.appendChild(inputAntall);
inputAntall.type = 'number';

inputAntall.addEventListener('keyup', function () {
    antallBrukere = inputAntall.value;
    // console.log('enter')
    oppdaterFolk()
})

function oppdaterFolk() {
    ut.innerText = '';

    fetch('https://randomuser.me/api/?results=' + antallBrukere)
        .then(response => response.json())
        // .then(response => console.log(response))
        .then(response => behandleSvar(response))
        .catch(err => console.error(err))

}

function behandleSvar(svar) {
    for (bruker of svar.results) {
    console.log(svar);
    console.log('Navn: ' + bruker.name.first);

    let navn = document.createElement('p');
    ut.appendChild(navn);
    navn.innerText += bruker.name.title + ' ' + bruker.name.first + ' ' + bruker.name.last;
    
    let alder = document.createElement('p');
    ut.appendChild(alder);
    navn.innerText += ', som er ' + bruker.dob.age + ' år gammel';

    let bilde = document.createElement('img');
    ut.appendChild(bilde);
    bilde.setAttribute('src', bruker.picture.large);

    bilde.addEventListener('mouseover', function () {
        bilde.style.scale = '1.1';
    })
    bilde.addEventListener('mouseleave', function () {
        bilde.style.scale = '0.8';
    })
}}

let overskrift = document.createElement('h1');
document.body.appendChild(overskrift);
overskrift.innerText = 'Ansatte ved IT avdelingen ved ASVG';
overskrift.setAttribute('class', 'bakgrunn');

let ut = document.createElement('div');
document.body.appendChild(ut);

let høyde = 50;
overskrift.style.height =  høyde + 'px';
let bredde = 600;
overskrift.style.width =  bredde + 'px';

document.addEventListener('keydown', function (e) {
    let tast = e.code;
    if (tast === 'KeyW') {
        høyde -= 2;
    } else if (tast === 'KeyS') {
        høyde += 2;
    } else if (tast === 'KeyD') {
        bredde += 2;
    } else if (tast === 'KeyA') {
        bredde -= 2;
    }
    overskrift.style.height =  høyde + 'px';
    overskrift.style.width =  bredde + 'px';
})
