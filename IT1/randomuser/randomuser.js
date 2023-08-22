let antallBrukere = 0;
let loading = false;
let inputAntall = document.createElement('input');
document.body.appendChild(inputAntall);
inputAntall.type = 'number';

inputAntall.addEventListener('keyup', function () {
    if (!loading) {
        loading = true;
        antallBrukere = inputAntall.value;
        // console.log('enter')
        oppdaterFolk()
    }
})

function oppdaterFolk() {
    main.innerText = 'Loading...';

    fetch('https://randomuser.me/api/?nat=no&results=' + antallBrukere)
        .then(response => response.json())
        // .then(response => console.log(response))
        .then(response => behandleSvar(response))
        .catch(err => console.error(err))

}

function behandleSvar(svar) {  
    main.innerText = '';
    
    for (bruker of svar.results) {
    console.log(svar);
    console.log('Navn: ' + bruker.name.first);

    let litenDiv = document.createElement('div');
    main.appendChild(litenDiv);
    litenDiv.setAttribute('class', 'litenDiv');    

    let navn = document.createElement('p');
    litenDiv.appendChild(navn);
    navn.innerText += bruker.name.first + ' ' + bruker.name.last;
    
    let alder = document.createElement('p');
    litenDiv.appendChild(alder);
    alder.innerText += bruker.dob.age + ' år gammel';

    let sted = document.createElement('p');
    litenDiv.appendChild(sted);
    sted.innerText += 'Fra ' + bruker.location.city;

    let bilde = document.createElement('img');
    litenDiv.appendChild(bilde);
    bilde.setAttribute('src', bruker.picture.large);
    bilde.setAttribute('class', 'brukerBilde');

    

    litenDiv.addEventListener('mouseover', function () {
        litenDiv.style.scale = '1.1';
        bilde.style.scale = '1.0';
    })
    litenDiv.addEventListener('mouseleave', function () {
        litenDiv.style.scale = '1.0';
        bilde.style.scale = '0.8';
    })

    loading = false;
}}

let overskrift = document.createElement('h1');
document.body.appendChild(overskrift);
overskrift.innerText = 'Medlemmer i SIAN';
overskrift.setAttribute('class', 'bakgrunn');

let logo = document.createElement('img');
overskrift.appendChild(logo);
logo.setAttribute('src', 'bilder/sianLogo.jpg');
logo.setAttribute('id', 'logo');

let main = document.createElement('div');
document.body.appendChild(main);
main.setAttribute('id', 'main');

// let høyde = 50;
// overskrift.style.height =  høyde + 'px';
// let bredde = 600;
// overskrift.style.width =  bredde + 'px';

// document.addEventListener('keydown', function (e) {
//     let tast = e.code;
//     if (tast === 'KeyW') {
//         høyde -= 2;
//     } else if (tast === 'KeyS') {
//         høyde += 2;
//     } else if (tast === 'KeyD') {
//         bredde += 2;
//     } else if (tast === 'KeyA') {
//         bredde -= 2;
//     }
//     overskrift.style.height =  høyde + 'px';
//     overskrift.style.width =  bredde + 'px';
// })
