let prisFelt = document.querySelectorAll('.pris')
let pris = 20;

for (let i = 0; i < prisFelt.length; i++) {  
    prisFelt.item(i).innerText = pris;
}

console.log(pris)