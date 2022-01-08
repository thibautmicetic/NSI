let figure_x = 255;
let figure_y = 255;
let figure_z = 255;


  class  oeuvre{
    constructor (figure){
      this.figure = figure;
    }
  
    affichage() {
      stroke(0);
    if (this.figure === "ellipse"){
      let c = color(random(figure_x), random(figure_y), random(figure_z));
  fill(c);
      ellipse(random(400), random(400), random(100), random(100));
    }
    
    if (this.figure === "rect"){
      let c = color(random(figure_x), random(figure_y), random(figure_z));
  fill(c);
      rect(random(400), random(400), random(100), random(100));
    }
    
    if (this.figure === "triangle"){
      let c = color(random(figure_x), random(figure_y), random(figure_z));
  fill(c);
      triangle(random(400), random(400), random(400), random(400), random(400), random(400));
    }
          pg.background(150, 0);
  pg.rotateY(1);
  pg.sphere( );
  image(pg, 0, 0);
  
  pg.background(150, 0);
  pg.sphere();
  image(pg, 200, 0);
  
  pg.background(150, 0);
  pg.sphere();
  image(pg, 0, 200);
  
  pg.background(150, 0);
  pg.sphere();
  image(pg, 200, 200);
  
  pg.background(150, 0);
  pg.cylinder();
  image(pg, 100, 100);
    }
  };

  const figure_color_substract_btn = document.querySelector("#figure-color-substract-btn");
figure_color_substract_btn.addEventListener('click', () => {
  if(figure_x > 0 && figure_y > 0 && figure_z > 0){
    figure_x -= 15;
    figure_y -= 15;
    figure_z -= 15;
  }
});

const figure_color_add_btn = document.querySelector('#figure-color-add-btn');
figure_color_add_btn.addEventListener('click', () => {
  if(figure_x < 255 && figure_y < 255 && figure_z < 255){
    figure_x += 15;
    figure_y += 15;
    figure_z += 15;
  }
});

let x = 255;
let y = 255;
let z = 255;
const bc_substract_btn = document.querySelector('#background-color-substract-button');
bc_substract_btn.addEventListener('click', () => {
  if(x > 0 && y > 0 && z > 0){
  x -= 15;
  y -= 15;
  z -= 15;
  };
});

const bc_add_btn = document.querySelector('#background-color-add-btn');
bc_add_btn.addEventListener('click', () => {
  if(x < 255 && y < 255 && z < 255){
  x += 15;
  y += 15;
  z += 15;
  };
});

let fm = 5;
const frame_rate_substract_btn = document.querySelector('#frame-rate-substract-btn');
frame_rate_substract_btn.addEventListener('click', () => {
  if(fm > 1){
    fm--
  }
});

const frame_rate_add_btn = document.querySelector('#frame-rate-add-btn');
frame_rate_add_btn.addEventListener('click', () => {
  if(fm < 10){
    fm++
  }
});

var oeuvres = [];
  
  function getfigure(){
    let list_figure = ["ellipse", "rect", "triangle"];
    return random(list_figure);
  }
  
  let pg;
  function setup() {
    createCanvas(400, 400);
    pg = createGraphics(200, 200, WEBGL);
   
    
    for (let pas = 0; pas < 20; pas++) {
      oeuvres.push(new oeuvre(getfigure()))
    }
  }
  
  function draw() {
    background(random(x), random(y), random(z));
  
    for (let i=0;i<oeuvres.length;i++) {
      oeuvres[i].affichage()
         frameRate(fm);
    }
  
  
  }
