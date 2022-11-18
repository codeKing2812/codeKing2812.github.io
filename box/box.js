//dette programmet er en liten boks du kan flytte rundt med WASD
const canvas = document.getElementById('mycanvas');
const ctx = canvas.getContext('2d');

class box {
    constructor (x, y, xv, yv, width, height, friksjon, maksFart, farge) {
    this.x = 240;
    this.y = 240;
    this.xv = 0;
    this.yv = 0;
    this.width = 20;
    this.height = 20;
    this.friksjon = 0.05;
    this.maksFart = 7;
    this.farge = 'black';
    }
}

box.prototype.draw = function() {
    ctx.fillRect(this.x, this.y, this.width, this.height); //tegn
    ctx.fillStyle = this.farge;

    this.x += this.xv;
    this.y += this.yv; //flytt

    if (this.yv < 0) {this.yv += this.friksjon;}
    if (this.yv > 0) {this.yv -= this.friksjon;}
    if (this.xv < 0) {this.xv += this.friksjon;}
    if (this.xv > 0) {this.xv -= this.friksjon;}//friksjon

    if (this.yv < -this.maksFart) {this.yv = -this.maksFart;}
    if (this.yv > this.maksFart) {this.yv = this.maksFart;}
    if (this.xv < -this.maksFart) {this.xv = -this.maksFart;}
    if (this.xv > this.maksFart) {this.xv = this.maksFart;}//maksfart

    if(this.x > canvas.width) {this.x = 0 - this.width;}
    if(this.x + this.width < 0) {this.x = canvas.width;}
    if(this.y > canvas.height) {this.y = 0 - this.height;}
    if(this.y + this.height < 0) {this.y = canvas.height;} //bli på kartet  

} 

function keyDetector (key) {
    if (key.keyCode == 87 ) {selv.yv -= 2;} //opp
    if (key.keyCode == 83 ) {selv.yv += 2;} //ned
    if (key.keyCode == 65 ) {selv.xv -= 2;} //høyre
    if (key.keyCode == 68 ) {selv.xv += 2;} //venstre
}

let selv = new box();
let slem = new box();



function loop() { 
    ctx.clearRect(0,0,canvas.width,canvas.height);
    selv.draw();
    slem.draw();

    requestAnimationFrame(loop)
}

// setInterval(loop,50);
addEventListener('keydown',keyDetector);