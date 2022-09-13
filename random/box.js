//dette programmet er en liten boks du kan flytte rundt med WASD

    var canvas = document.getElementById('mycanvas');
    var ctx = canvas.getContext('2d');
    
    var box = {};
    box.x = 240;
    box.y = 240;
    box.xv = 0;
    box.yv = 0;
    box.w = 20;
    box.h = 20; 
        
    function keyDetector (key) {
    if (key.keyCode == 87 ) {box.yv-=2;} //opp
    if (key.keyCode == 83 ) {box.yv+=2;} //ned
    if (key.keyCode == 65 ) {box.xv-=2;} //høyre
    if (key.keyCode == 68 ) {box.xv+=2;} //venstre
    }
    
    function loop() { 
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.strokeRect(box.x, box.y, box.w, box.h);
    
    box.x += box.xv;
    box.y += box.yv;
    if (box.yv < 0) {box.yv+=0.02;}
    if (box.yv > 0) {box.yv-=0.02;}
    if (box.xv < 0) {box.xv+=0.02;}
    if (box.xv > 0) {box.xv-=0.02;}//friksjon

    if(box.x > canvas.width) {box.x=0-box.w;}
    if(box.x+box.w < 0) {box.x=canvas.width;}
    if(box.y > canvas.height) {box.y=0-box.h;}
    if(box.y+box.h < 0) {box.y=canvas.height;} //bli på kartet  
    }
    
    setInterval(loop,20);
    addEventListener('keydown',keyDetector);
