//dette programmet er en liten boks du kan flytte rundt med WASD
const canvas = document.getElementById('mycanvas');
const ctx = canvas.getContext('2d');

class box {
    constructor (sheetX, sheetY, sheetWidth, sheetHeight, x, y, width, height, xv, yv, friksjon, bilde) {
    this.sheetX = sheetX,
    this.sheetY = sheetY,
    this.sheetWidth = sheetWidth,
    this.sheetHeight = sheetHeight,
    this.x = x,
    this.y = y,
    this.width = width,
    this.height = height,
    this.xv = xv,
    this.yv = yv,
    this.friksjon = friksjon,
    this.bilde = bilde;
}}

box.prototype.draw = function() {
    ctx.drawImage(this.bilde, this.sheetX, this.sheetY, this.sheetWidth, this.sheetHeight, this.x, this.y, this.width, this.height);
    console.log(this.sheetX);
    
    if ((frame/20) % 1 == 0) {
        if (this.sheetX < this.bilde.width) {
            this.sheetX += this.sheetWidth;
        } else {this.sheetX = 0;}
    }
    
    this.x += this.xv;
    this.y += this.yv; //flytt

    if (this.yv < 0) {this.yv += this.friksjon;}
    if (this.yv > 0) {this.yv -= this.friksjon;}
    if (this.xv < 0) {this.xv += this.friksjon;}
    if (this.xv > 0) {this.xv -= this.friksjon;}//friksjon

    if(this.x > canvas.width) {this.x = 0 - this.width;}
    if(this.x + this.width < 0) {this.x = canvas.width;}
    if(this.y > canvas.height) {this.y = 0 - this.height;}
    if(this.y + this.height < 0) {this.y = canvas.height;} //bli på kartet  

}

let Wtast = false;
let Stast = false;
let Dtast = false;
let Atast = false;

let OppTast = false;
let NedTast = false;
let VenstreTast = false;
let HøyreTast = false;

addEventListener("keydown", function(e) {
    let tast = e.key;
    console.log(tast);

    if(e.key==="w") {
        Wtast = true;
    }
    if(e.key==="s") {
        Stast = true;
    }
    if(e.key==="a") {
        Atast = true;
    }
    if(e.key==="d") {
        Dtast = true;
    }

    if(e.key==="ArrowUp") {
        OppTast = true;
    }
    if(e.key==="ArrowDown") {
        NedTast = true;
    }
    if(e.key==="ArrowLeft") {
        VenstreTast = true;
    }
    if(e.key==="ArrowRight") {
        HøyreTast = true;
    }

});

addEventListener("keyup", function() {
    Wtast = false;
    Stast = false;
    Atast = false;
    Dtast = false;

    OppTast = false;
    NedTast = false;
    VenstreTast = false;
    HøyreTast = false;
});

const spritesheetGrønn = new Image();
spritesheetGrønn.src = 'bilder/Snurrehattmann.png';

const spritesheetRød = new Image();
spritesheetRød.src = 'bilder/Flosshattmann.png';

let grønn = new box(0, 0, 100, 100, 250, 250, 150, 150, 0, 0, 0.2, spritesheetGrønn);
let rød = new box(0, 0, 100, 100, 350, 350, 150, 150, 0, 0, 0.2, spritesheetRød);

let frame = 0;
function loop() { 
    frame++;

    ctx.clearRect(0,0,canvas.width,canvas.height);
    grønn.draw();
    rød.draw();

    if (Wtast) {grønn.yv -= 1;} //opp
    if (Stast) {grønn.yv += 1;} //ned
    if (Atast) {grønn.xv -= 1;} //venstre
    if (Dtast) {grønn.xv += 1;} //høyre

    if (OppTast) {rød.yv -= 1;} //opp
    if (NedTast) {rød.yv += 1;} //ned
    if (VenstreTast) {rød.xv -= 1;} //venstre
    if (HøyreTast) {rød.xv += 1;} //høyre

    requestAnimationFrame(loop)
}
loop();

// setInterval(loop,50);