const canvas = document.getElementById('mycanvas');
const ctx = canvas.getContext('2d');

class sprite {
    constructor (sheetX, sheetY, sheetWidth, sheetHeight, x, y, width, height, xv, yv, friksjon, animer, flip, iLuften, bilde) {
    this.sheetX = sheetX,
    this.sheetY = sheetY,
    this.sheetWidth = sheetWidth,
    this.sheetHeight = sheetHeight,
    this.sheetNr = 0,
    this.x = x,
    this.y = y,
    this.width = width,
    this.height = height,
    this.xv = xv,
    this.yv = yv,
    this.friksjon = friksjon,
    this.animer = animer,
    this.flip = flip,
    this.iLuften = iLuften,
    this.bilde = bilde;

    this.draw = function() {
        if (this.flip == true) {
            ctx.scale(-1,1); //flip spilleren hvis den går andre vei
            ctx.drawImage(this.bilde, this.sheetX, this.sheetY, this.sheetWidth, this.sheetHeight, -this.x - this.width, this.y, this.width, this.height);
            ctx.scale(-1,1);
        } else {ctx.drawImage(this.bilde, this.sheetX, this.sheetY, this.sheetWidth, this.sheetHeight, this.x, this.y, this.width, this.height);}
        
        this.sheetY = this.sheetHeight * this.sheetNr;
        if (this.animer) {
            if ((frame/7) % 1 == 0)  {//bytt animasjonsbilde hvær n'te frame
                if (this.sheetNr < 6) {
                    this.sheetNr ++;
                } else {this.sheetNr = 1;}
            } 
        } else {this.sheetNr = 0;}

        this.x += this.xv;
        this.y += this.yv; //flytt
    
        if(this.x > canvas.width) {this.x = -this.width;}
        if(this.x + this.width < 0) {this.x = canvas.width;}
        if(this.y > canvas.height) {this.y = -this.height;}
        if(this.y + this.height < 0) {this.y = canvas.height;} //bli i bildet

    }
}}


function tyngdekraft(spiller) { // orginal tyngdekraft funksjon
    for (let bakke of bakkeArr) {
        if (crash(spiller, bakke)) {
            spiller.iLuften = true;
            spiller.y = bakke.y - (spiller.height);
        } else {
            spiller.iLuften = false;
        }
    }
    if (spiller.iLuften) {
        spiller.yv = 0;
    } else {spiller.yv += 0.5;}
};

function crash(sprite1, sprite2) {
    if (sprite1.x + sprite1.width > sprite2.x && sprite1.x < sprite2.x + sprite2.width && sprite1.y + sprite1.height > sprite2.y && sprite1.y < sprite2.y + sprite2.height) {
        return true;
    }
};

function tyngdekraft2(spiller) { //tyngdekraft versjon 2
    spiller.iLuften = bakkeArr.every(sjekk);
    console.log('spiller i luften:', spiller.iLuften)
    
    function sjekk(denne) {
        if (crash(spiller, denne)) {
            return false;
        } else {return true;}
    }

    if (!spiller.iLuften) {
        spiller.yv = 0;
    } else {spiller.yv += 0.5;}
}

const spritesheetGrønn = new Image();
spritesheetGrønn.src = 'bilder/spiller-3.2.png';

const spritesheetRød = new Image();
spritesheetRød.src = 'bilder/Flosshattmann.png';

const bakkeBilde = new Image();
bakkeBilde.src = 'bilder/bakke.png';

let grønn = new sprite(0, 0, 100, 210, 250, 250, 100, 210, 0, 0, 0.5, true, false, true, spritesheetGrønn);
let rød = new sprite(0, 0, 100, 100, 350, 350, 150, 150, 0, 0, 0.5, true, false, true, spritesheetRød);

let bakkeArr = []
function nyBakke(x, y, lengde) {
    bakkeArr.push(new sprite(0, 0, 500, 100, x, y, lengde, 100, 0, 0, 0, false, false, false, bakkeBilde))
}

nyBakke(100, 310, 200)//opretter to nye bakke-blokker
nyBakke(200, 300, 300)

//------------KNAPPER-------------

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


//-----------GAMELOOP--------------

let frame = 0;
function loop() { 
    ctx.clearRect(0,0,canvas.width,canvas.height);
    frame++;

    tyngdekraft2(grønn);

    // tyngdekraft(grønn);
    // tyngdekraft(rød);

    // console.log(grønn.iLuften)

    for (let bakke of bakkeArr) {
        bakke.draw();
    }

    grønn.draw();
    // rød.draw();

    if (Wtast && !grønn.iLuften) { //hopp
        grønn.yv = -10; grønn.iLuften = true;
    }
    if (Atast || Dtast) { //gå til siden
        grønn.animer = true;
        if (Dtast) {
            grønn.flip = false;
            grønn.xv = 3;
        } else {
            grønn.flip = true;1
            grønn.xv = -3;
        }
    } else {
        grønn.animer = false;
        grønn.xv = 0;
    }
    
    if (OppTast && rød.iLuften) {rød.yv = -10; rød.iLuften = false;} //hopp
    if (VenstreTast) {rød.xv = -5;} //venstre
    if (HøyreTast) {rød.xv = 5;} //høyre

    requestAnimationFrame(loop)
}
loop();