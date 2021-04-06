def setup():
  size(550, 500)
  strokeWeight(5)
  frameRate(5)
  textSize(70)
def draw():
    clear()
    background(204,204,204)
    s = createShape()
    s.beginShape()
    s.fill(0,255,255)
    s.vertex(50, 300)
    s.vertex(100, 260)
    s.vertex(160,220)
    s.vertex(190,160)
    s.vertex(210, 215)
    s.vertex(400, 245)
    s.vertex(480,180)
    s.vertex(440,260)
    s.vertex(480, 355)
    s.vertex(400, 280)
    s.vertex(310, 320)
    s.vertex(250,335)
    s.vertex(270,370)
    s.vertex(230, 340)
    s.vertex(115, 340)
    s.vertex(125, 315)
    s.vertex(90, 325)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    point(150, 300)
    if hex(get(mouseX, mouseY)) == ('FF00FFFF'):
        fill(random(0,255),random(0,255),random(0,255)) # najpierw ustawiamy kolor,a potem w nim rysujemy
        text('A.N.', width/2-40, height/2-70)
    elif (keyPressed == True): # nie chodziłoo napis o treści prawda, tylko typ logiczny prawda
        if (key == 'a'):
            fill(0,255,0)
            text('A.  ', width/2-40, height/2-70) # skoro już rozdzielasz, to takie małe wizualne uzupełnienie ;)
        elif (key == 'n'):
            fill(255,255,0)
            text('   N.', width/2-40, height/2-70)
        else:
            fill(255,0,0)
            text('A.N.', width/2-40, height/2-70)
    else:
        fill(255,0,255)
        text('A.N.', width/2-40, height/2-70)
   # 2 pkt 
