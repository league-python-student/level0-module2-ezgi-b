# When you are done, this program will draw an ice cream cone with 
#     scoops of ice cream, sprinkles, and a cherry on top.


def setup():

    size(500,500)
     
    # Call the make_ice_cream_cone() function below to draw the cone for your ice cream
    make_ice_cream_cone()
    # Use the add_scoop() function below to add as many scoops of ice cream as you want
    # Choose a different flavor for each scoop
    add_scoop("chocolate")
    add_scoop("strawberry")
    add_scoop("vanilla")
    # Use the add_sprinkle() function provided to add some sprinkles to your ice cream
    add_sprinkle(100)
    # Write code to add a cherry to the top of your ice cream. Hint: ellipse
    add_cherry(1)

def add_cherry(num):
    global scoops
    fill(160, 0, 30)
    if num == 1:
        ellipse(width/2,coneY - 40 - (SCOOPSIZE*scoops)/2, 50, 50)
        stroke(0, 130, 0)
        strokeWeight(3)
        line(width/2,coneY - 60 - (SCOOPSIZE*scoops)/2, width/2 + 15,coneY - 90 - (SCOOPSIZE*scoops)/2)
    if num == 2:
        ellipse(width/2 + 30,coneY - 40 - (SCOOPSIZE*scoops)/2, 50, 50)
        stroke(0, 130, 0)
        strokeWeight(3)
        line(width/2 + 30,coneY - 60 - (SCOOPSIZE*scoops)/2, width/2 + 15,coneY - 90 - (SCOOPSIZE*scoops)/2)
        
        noStroke()
        ellipse(width/2 - 30,coneY - 40 - (SCOOPSIZE*scoops)/2, 50, 50)
        stroke(0, 130, 0)
        strokeWeight(3)
        line(width/2 - 30,coneY - 60 - (SCOOPSIZE*scoops)/2, width/2 + 15,coneY - 90 - (SCOOPSIZE*scoops)/2)

#***********  These are functions for you to use. DON'T CHANGE CODE BELOW THIS LINE !!!   *****************/

SCOOPSIZE = 150
scoops = 0
coneY = 320


def make_ice_cream_cone():
     fill(188,126,49)
     triangle(190,300,310,300,255,500)


def add_scoop(flavor):
     global scoops;
     noStroke()
     if flavor.lower() == "chocolate":
         fill(116,71,16)
     elif flavor.lower() == "strawberry":
         fill( 232 ,144,129)
     elif flavor.lower() == "vanilla":
         fill(245, 243, 227)
     else:
         print "ERROR: We don't have the flavor "+ flavor 
         return

     ellipse(width/2,coneY - 50 - (SCOOPSIZE*scoops)/2,SCOOPSIZE,SCOOPSIZE)
     scoops+=1


def add_sprinkle(number_of_sprinkles):
    for i in range(number_of_sprinkles):
        fill(random(256),random(256),random(256))
        min_x = width/2-SCOOPSIZE/2 + 10
        max_x = SCOOPSIZE/3 +width/2 +10
        min_y = coneY-((SCOOPSIZE)*scoops)/2-40
        max_y = coneY
        sprinkle_area_x = random(min_x, max_x)
        sprinkle_area_y = random(min_y, max_y)
        sprinkle_width = random(2,9)
        sprinkle_height = random(2,9)
        ellipse(sprinkle_area_x,sprinkle_area_y,sprinkle_height,sprinkle_width)
