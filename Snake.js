var snake;
var snakeX;
var snakeY;
var leftKey;

snakeX = 250;
snakeY = 250;


function setup(){
	createCanvas(500,500);
}
function draw(){
	background(0);
	snake = rect(snakeX,snakeY,20,20);
    		fill(0);
				if(keyDown(LEFT_ARROW))
   				ship.rotation -= 4;
  				if(keyDown(RIGHT_ARROW))
    			ship.rotation += 4;
{
