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
            if ((frame/7) % 1 == 0)  {//bytt animasjonsbilde hver n'te frame
                if (this.sheetNr < 6) {
                    this.sheetNr ++;
                } else {this.sheetNr = 1;}
            } 
        } else {
            this.sheetNr = 0;
            // this.sheetX = 50;
            // this.sheetWidth = 10;
        }

        this.x += this.xv;
        this.y += this.yv; //flytt
        
        if(this.x > canvas.width) {this.x = -this.width;}
        if(this.x + this.width < 0) {this.x = canvas.width;}
        if(this.y > canvas.height) {this.y = -this.height;}
        if(this.y + this.height < 0) {this.y = canvas.height;} //bli i bildet
    }
}}


// function tyngdekraft_1(spiller) { // orginal tyngdekraft funksjon
//     for (let bakke of bakkeArr) {
//         if (crash(spiller, bakke)) {
//             spiller.iLuften = true;
//             spiller.y = bakke.y - (spiller.height);
//         } else {
//             spiller.iLuften = false;
//         }
//     }
//     if (spiller.iLuften) {
//         spiller.yv = 0;
//     } else {spiller.yv += 0.5;}
// };

function tyngdekraft(spiller) { //tyngdekraft versjon 2
    spiller.iLuften = bakkeArr.every(sjekk);

    function sjekk(denne) {
        let denneResultat = touching(spiller, denne);

        if (denneResultat == 'topp') {
            spiller.yv = 0;
        }
        if (denneResultat == 'høyre') {
            spiller.x = denne.x - (spiller.width);
        }
        if (denneResultat == 'venstre') {
            spiller.x = denne.x + (denne.width);
        }
        if (denneResultat == 'bunn') {
            spiller.y = denne.y - (spiller.height);
            return false;
        } else {return true;}
        
    }

    if (!spiller.iLuften) {
        spiller.yv = 0;
    } else {spiller.yv += 0.5;}
};

function touching(sprite1, sprite2) {
    let bunn = true;
    if (sprite1.x + sprite1.width > sprite2.x && sprite1.x < sprite2.x + sprite2.width && 
        sprite1.y + sprite1.height > sprite2.y && sprite1.y < sprite2.y + sprite2.height) {
        
        // console.log('touch')
        
        // if (sprite1.y + sprite1.height < sprite2.y + 5) {
        //     return 'bunn';
        // } else 

        // bunn = true;
        if (sprite1.y > sprite2.y + sprite2.height - 10) {
            // bunn = false;
            console.log('topp')
            return 'topp'
        }
        if (sprite1.x + sprite1.width < sprite2.x + 5) {
            // bunn = false;
            console.log('høyre')
            return 'høyre';
        }
        if (sprite1.x > sprite2.x + sprite2.width - 5) {
            // bunn = false;
            console.log('venstre')
            return 'venstre';
        } 
        if (sprite1.y + sprite1.height < sprite2.y + 15) {
            console.log('bunn')
            return 'bunn';
        }

        // return true;
    }
};

const spritesheetGrønn = new Image();
spritesheetGrønn.src = 'bilder/spiller-3.2.png';

const spritesheetRød = new Image();
spritesheetRød.src = 'bilder/Flosshattmann.png';

const bakkeBilde = new Image();
bakkeBilde.src = 'bilder/bakke-1.0.png';

let grønn = new sprite(10, 0, 90, 210, 250, 250, 100, 210, 0, 0, 0.5, true, false, true, spritesheetGrønn);
let rød = new sprite(0, 0, 100, 100, 350, 350, 150, 150, 0, 0, 0.5, true, false, true, spritesheetRød);

let bakkeArr = []
function nyBakke(x, y, lengde) {
    while (lengde > 500) {
        bakkeArr.push(new sprite(0, 0, 500, 100, x, y, 500, 100, 0, 0, 0, false, false, false, bakkeBilde))
        lengde -= 500;
        x += 500;
    }
    bakkeArr.push(new sprite(0, 0, lengde, 100, x, y, lengde, 100, 0, 0, 0, false, false, false, bakkeBilde))
}

nyBakke(200, 500, 200)//opretter bakke-blokker
nyBakke(200, 500, 200)
nyBakke(-100, 550, 1100)
nyBakke(450, 200, 100)

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
    if(e.code=='KeyW') {
        Wtast = true;
    }
    if(e.code=='KeyS') {
        Stast = true;
    }
    if(e.code=='KeyA') {
        Atast = true;
    }
    if(e.code=='KeyD') {
        Dtast = true;
    }

    if(e.key=='ArrowUp') {
        OppTast = true;
    }
    if(e.key=='ArrowDown') {
        NedTast = true;
    }
    if(e.key=='ArrowRight') {
        HøyreTast = true;
    }
    if(e.key=='ArrowLeft') {
        VenstreTast = true;
    }
});

addEventListener("keyup", function(e) {
    if(e.code=='KeyW') {
        Wtast = false;
    }
    if(e.code=='KeyS') {
        Stast = false;
    }
    if(e.code=='KeyA') {
        Atast = false;
    }
    if(e.code=='KeyD') {
        Dtast = false;
    }

    if(e.key=='ArrowUp') {
        OppTast = false;
    }
    if(e.key=='ArrowDown') {
        NedTast = false;
    }
    if(e.key=='ArrowRight') {
        HøyreTast = false;
    }
    if(e.key=='ArrowLeft') {
        VenstreTast = false;
    }
});


//-----------GAMELOOP--------------

let frame = 0;
function loop() { 
    ctx.clearRect(0,0,canvas.width,canvas.height);
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
    frame++;

    tyngdekraft(grønn);
    // tyngdekraft(rød);

    for (let bakke of bakkeArr) {
        bakke.draw();
    }

    grønn.draw();
    // rød.draw();

    if (Wtast && !grønn.iLuften || OppTast && !grønn.iLuften) { //hopp
        grønn.yv = -10; grønn.iLuften = true;
    }
    if (Atast || Dtast || HøyreTast || VenstreTast) { //gå til siden
        grønn.animer = true;
        if (Dtast || HøyreTast) {
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

if (localStorage.antallBesok) {
    localStorage.antallBesok = Number(localStorage.antallBesok) + 1;
} else {
    localStorage.antallBesok = 1;
}
console.log(localStorage.antallBesok);