const canvas = document.getElementById('mycanvas');
const ctx = canvas.getContext('2d');

class box {
    constructor (sheetX, sheetY, sheetWidth, sheetHeight, x, y, width, height, xv, yv, friksjon, animer, påBakken, bilde) {
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
    this.animer = animer,
    this.påBakken = påBakken,
    this.bilde = bilde;

}}

function tyngdekraft(spiller) {
    spiller.yv = spiller.yv + 0.5;
    if (spiller.y + spiller.height > bakke.y) {
        spiller.påBakken = true;
        spiller.yv = 0;
        spiller.y -= 1;
    }

};

// function kræsj(boks1, boks2) {
//     if (boks1.x + boks1.width/2 > boks2.x && boks1.x < boks2.x + boks2.width/2 && boks1.y + boks1.height > boks2.y && boks1.y < boks2.y + boks2.height) {
//         boks1.yv = -boks1.yv;
//         boks1.xv = -boks1.xv;
//     }

// };

box.prototype.draw = function() {
    ctx.drawImage(this.bilde, this.sheetX, this.sheetY, this.sheetWidth, this.sheetHeight, this.x, this.y, this.width, this.height);
    
    if ((frame/7) % 1 == 0 && this.animer) {
        if (this.sheetX < this.bilde.width - 100) {
            this.sheetX += this.sheetWidth;
        } else {this.sheetX = 0;}
    }
    
    this.x += this.xv;
    this.y += this.yv; //flytt

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
    if(e.key=="w") {
        Wtast = true;
    }
    if(e.key=="s") {
        Stast = true;
    }
    if(e.key=="a") {
        Atast = true;
    }
    if(e.key=="d") {
        Dtast = true;
    }

    if(e.key=="ArrowUp") {
        OppTast = true;
    }
    if(e.key=="ArrowDown") {
        NedTast = true;
    }
    if(e.key=='ArrowRight') {
        HøyreTast = true;
    }
    if(e.key=="ArrowLeft") {
        VenstreTast = true;
    }
});

addEventListener("keyup", function(e) {
    if(e.key=="w") {
        Wtast = false;
    }
    if(e.key=="s") {
        Stast = false;
    }
    if(e.key=="a") {
        Atast = false;
    }
    if(e.key=="d") {
        Dtast = false;
    }

    if(e.key=="ArrowUp") {
        OppTast = false;
    }
    if(e.key=="ArrowDown") {
        NedTast = false;
    }
    if(e.key=='ArrowRight') {
        HøyreTast = false;
    }
    if(e.key=="ArrowLeft") {
        VenstreTast = false;
    }
});

const spritesheetGrønn = new Image();
spritesheetGrønn.src = 'bilder/Snurrehattmann.png';

const spritesheetRød = new Image();
spritesheetRød.src = 'bilder/Flosshattmann.png';

const bakkeBilde = new Image();
bakkeBilde.src = 'bilder/bakke.png';

let grønn = new box(0, 0, 100, 100, 250, 250, 150, 150, 0, 0, 0.5, true, true, spritesheetGrønn);
let rød = new box(0, 0, 100, 100, 350, 350, 150, 150, 0, 0, 0.5, true, true, spritesheetRød);
let bakke = new box(0, 0, 500, 100, 0, 500, 700, 100, 0, 0, 0, false, false, bakkeBilde);

let frame = 0;
function loop() { 
    ctx.clearRect(0,0,canvas.width,canvas.height);
    frame++;

    bakke.draw();
    grønn.draw();
    rød.draw();

    tyngdekraft(grønn);
    tyngdekraft(rød);
    // kræsj(grønn, rød);

    if (Wtast && grønn.påBakken) {grønn.yv -= 10; grønn.påBakken = false;} //hopp
    if (Atast) {grønn.xv = -5;} //venstre
    if (Dtast) {grønn.xv = 5;} //høyre

    if (OppTast && rød.påBakken) {rød.yv -= 10; rød.påBakken = false;} //hopp
    if (VenstreTast) {rød.xv = -5;} //venstre
    if (HøyreTast) {rød.xv = 5;} //høyre

    requestAnimationFrame(loop)
}
loop();