#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         22/7/2021
# Description:  Use Turtle Graphics to illustrate the city life.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

import turtle
from drawing_procedures import *


# Set the window
screen = turtle.Screen()
screen.bgcolor('#00002E')
screen.bgpic('assets/background.gif')
screen.title('Henry\'s Turtle')
turtle.setup(width = 750, height = 750)

# house
house = turtle.Turtle()
set_turtle(house, '#ebbc48', '#ebbc48', 2)
move_turtle(house, -350, -200)
house.begin_fill()
house.fd(400)
house.lt(90)
house.fd(150)
house.lt(90)
house.fd(100)
house.lt(-90)
house.fd(150)
house.lt(90)
house.fd(200)
house.lt(90)
house.fd(150)
house.lt(-90)
house.fd(100)
house.lt(90)
house.fd(150)
house.end_fill()
house.hideturtle()

# roof_set_up
roof = turtle.Turtle()
set_turtle(roof, '#ff6c22', '#ff6c22', 2)

# left_roof
move_turtle(roof, -370, -50)
roof.begin_fill()
roof.lt(70)
roof.fd(75)
roof.lt(-70)
roof.fd(92)
roof.lt(-90)
roof.fd(70)
roof.lt(-90)
roof.fd(118)
roof.end_fill()

# middle_roof
move_turtle(roof, 70, -50)
roof.begin_fill()
roof.lt(-70)
roof.fd(75)
roof.lt(70)
roof.fd(92)
roof.lt(90)
roof.fd(70)
roof.lt(90)
roof.fd(118)
roof.end_fill()

# right_roof
move_turtle(roof, -150, 100)
roof.begin_fill()
roof.lt(180)
roof.fd(120)
roof.lt(-110)
roof.fd(70)
roof.lt(-70)
roof.fd(200)
roof.lt(-70)
roof.fd(70)
roof.lt(-110)
roof.fd(130)
roof.end_fill()
roof.hideturtle()

# door
door = turtle.Turtle()
set_turtle(door, '#624A3A', '#A18265', 5)
move_turtle(door, -150, -200)
door.begin_fill()
door.lt(180)
door.fd(35)
door.lt(-90)
door.fd(110)
door.lt(-90)
door.fd(70)
door.lt(-90)
door.fd(110)
door.lt(-90)
door.fd(35)
door.end_fill()

# door_handle
move_turtle(door, -125, -145)
door.begin_fill()
door.fillcolor('#624A3A')
door.fd(5)
door.lt(-90)
door.fd(10)
door.lt(-90)
door.fd(5)
door.lt(-90)
door.fd(10)
door.end_fill()

# above_door
move_turtle(door, -185, -70)
door.lt(90)
door.fd(70)
door.hideturtle()

# window
window = turtle.Turtle()
set_turtle(window, '#624A3A', '#5ca4cc', 2)

# Call the function to draw the windows
window_position = [(-325, -130),
                   (-25, -130),
]
for x, y in window_position:
    draw_window(window, x, y)
window.hideturtle()

# middle_window
move_turtle(window, -230, 10)
window.begin_fill()
window.showturtle()
window.lt(90)
window.fd(50)
window.lt(-90)
window.fd(160)
window.lt(-90)
window.fd(50)
window.lt(-90)
window.fd(160)
window.end_fill()
window.lt(-90)
window.fd(25)
window.lt(-90)
window.fd(160)
window.bk(75)
window.lt(90)
window.fd(25)
window.bk(50)
window.hideturtle()

# chimney
chimney = turtle.Turtle()
set_turtle(chimney, '#f36e28', '#f36e28', 2)
move_turtle(chimney, -230, 150)
chimney.begin_fill()
chimney.lt(90)
chimney.fd(60)
chimney.lt(-90)
chimney.fd(30)
chimney.lt(-90)
chimney.fd(60)
chimney.lt(-90)
chimney.fd(30)
chimney.end_fill()
chimney.hideturtle()

chimney.fillcolor('#bc4132')
chimney.lt(-90)
chimney.fd(60)
chimney.showturtle()
chimney.begin_fill()
chimney.lt(90)
chimney.fd(10)
for _ in range(2):
    chimney.lt(-90)
    chimney.fd(10)
    chimney.lt(-90)
    chimney.fd(50)
chimney.end_fill()
chimney.hideturtle()

# street
street = turtle.Turtle()
set_turtle(street, '#4b4c4e', '#4b4c4e', 0)
move_turtle(street, -380, -280)
street.begin_fill()
street.fd(760)
street.lt(-90)
street.fd(90)
street.lt(-90)
street.fd(760)
street.lt(-90)
street.fd(90)
street.end_fill()

set_turtle(street, 'dark gray', 'dark gray', 0)
street.begin_fill()
street.fd(10)
street.lt(-90)
street.fd(760)
street.lt(-90)
street.fd(10)
street.lt(-90)
street.fd(760)
street.end_fill()
street.hideturtle()

# roadside
roadside = turtle.Turtle()
set_turtle(roadside, '#92d476', '#92d476', 0)
move_turtle(roadside, -380, -201)
roadside.begin_fill()
roadside.fd(760)
roadside.lt(-90)
roadside.fd(69)
roadside.lt(-90)
roadside.fd(760)
roadside.lt(-90)
roadside.fd(69)
roadside.end_fill()
roadside.hideturtle()

# broken_line
line = turtle.Turtle()
set_turtle(line, 'dark gray', 'dark gray', 4)
i = -350
while i <= 250:
    move_turtle(line, i, -350)
    line.fd(100)
    i += 150
line.hideturtle()

# little_stair
stair = turtle.Turtle()
set_turtle(stair, '#e4d3c5', '#e4d3c5', 0)
move_turtle(stair, -150, -195)
stair.begin_fill()
stair.bk(50)
stair.lt(-90)
stair.fd(20)
stair.lt(90)
stair.fd(100)
stair.lt(90)
stair.fd(20)
stair.lt(90)
stair.fd(50)
stair.end_fill()
stair.hideturtle()

# oval_tree_set_up
oval1 = turtle.Turtle()
set_turtle(oval1, '#3a831e', '#3a831e', 0)
oval1.shape('circle')

oval2 = turtle.Turtle()
set_turtle(oval2, '#3a831e', '#3a831e', 0)
oval2.shape('circle')

oval3 = turtle.Turtle()
set_turtle(oval3, '#3a831e', '#3a831e', 0)
oval3.shape('circle')

oval4 = turtle.Turtle()
set_turtle(oval4, '#3a831e', '#3a831e', 0)
oval4.shape('circle')

# draw_oval_tree
move_turtle(oval1, -320, -215)
oval1.shapesize(4, 2)

move_turtle(oval2, -240, -215)
oval2.shapesize(4, 2)

move_turtle(oval3, -55, -215)
oval3.shapesize(4, 2)

move_turtle(oval4, 23, -215)
oval4.shapesize(4, 2)

# big_tree
tree = turtle.Turtle()
set_turtle(tree, '#624A3A', '#624A3A', 0)
move_turtle(tree, 105, -260)
tree.begin_fill()
tree.fd(20)
tree.lt(90)
tree.fd(100)
tree.lt(90)
tree.fd(20)
tree.lt(90)
tree.fd(100)
tree.end_fill()
tree.hideturtle()

# leaf
leaf = turtle.Turtle()
set_turtle(leaf, '#3a831e', '#3a831e', 0)
move_turtle(leaf, 75, -250)
leaf.begin_fill()
leaf.lt(60)
leaf.fd(50)
leaf.lt(150)
leaf.fd(30)
leaf.lt(-150)
leaf.fd(40)
leaf.lt(150)
leaf.fd(30)
leaf.lt(-140)
leaf.fd(140)
leaf.lt(-140)
leaf.fd(140)
leaf.lt(-140)
leaf.fd(30)
leaf.lt(150)
leaf.fd(40)
leaf.lt(-150)
leaf.fd(30)
leaf.lt(150)
leaf.fd(50)
leaf.lt(-120)
leaf.fd(80)
leaf.end_fill()
leaf.hideturtle()

# lower_car_body
car = turtle.Turtle()
set_turtle(car, '#f94342', '#f94342', 2)
move_turtle(car, -230, -330)
car.begin_fill()
car.fd(160)
car.lt(90)
car.fd(40)
car.lt(90)
car.fd(160)
car.lt(90)
car.fd(40)
car.end_fill()

## upper_car_body

# car_glass
set_turtle(car, '#7bdff6', '#7bdff6', 2)
move_turtle(car, -200, -290)
car.begin_fill()
car.lt(150)
car.fd(40)
car.lt(-60)
car.fd(70)
car.lt(-60)
car.fd(39.5)
car.lt(-120)
car.fd(106)
car.end_fill()

# outside_glass
set_turtle(car, '#f94342', '#f94342', 5)
move_turtle(car, -200, -290)
car.begin_fill()
car.lt(-120)
car.fd(40)
car.lt(-60)
car.fd(70)
car.lt(-60)
car.fd(39.5)

move_turtle(car, -145, -290)
car.lt(150)
car.fd(32)
car.hideturtle()

# wheels
wheel = turtle.Turtle()
set_turtle(wheel, 'black', '#ebbc48', 4)
        
# Call the function to draw the wheels
draw_wheel(wheel, -200, -340)
draw_wheel(wheel, -105, -337)
wheel.hideturtle()

# flag
flag = turtle.Turtle()
set_turtle(flag, '#624A3A','#624A3A', 7)
move_turtle(flag, 195, -257)
flag.lt(90)
flag.fd(350)

set_turtle(flag, '#DA251D', '#DA251D', 7)
flag.begin_fill()
flag.lt(-90)
flag.fd(120)
flag.lt(-90)
flag.fd(70)
flag.lt(-90)
flag.fd(120)
flag.end_fill()
flag.hideturtle()

# star
star = turtle.Turtle()
set_turtle(star, '#FFCD00', '#FFCD00', 2)
draw_star(star, 230, 63)

# dog_face
dog = turtle.Turtle()
set_turtle(dog, '#93a2a9', '#93a2a9', 2)
move_turtle(dog, 235, -235)
dog.begin_fill()
dog.circle(18)
dog.end_fill()
dog.hideturtle()

# eyes
eye = turtle.Turtle()
set_turtle(eye, 'black', 'black', 2)

# Call the function to draw the eyes
eye_position = [(233, -214),
                (242, -210),
]
for x, y in eye_position:
    draw_eye(eye, x, y)
eye.hideturtle()

# mouth
mouth = turtle.Turtle()
set_turtle(mouth, 'black', 'black', 2)
move_turtle(mouth, 235, -227)
mouth.circle(3, 160)
mouth.hideturtle()

# left_ear
l_ear = turtle.Turtle()
set_turtle(l_ear, '#93a2a9', '#93a2a9', 0)
l_ear.shape('circle')
move_turtle(l_ear, 220, -202)

# right_ear
r_ear = turtle.Turtle()
set_turtle(r_ear, '#93a2a9', '#93a2a9', 0)
r_ear.shape('circle')
move_turtle(r_ear, 252, -202)

# body
body = turtle.Turtle()
set_turtle(body, '#93a2a9', '#93a2a9', 0)
body.shape('circle')
move_turtle(body, 255, -239)
body.shapesize(1, 3)

# legs
leg = turtle.Turtle()
set_turtle(leg, 'black', 'black', 2)

# Call the function to draw the legs
leg_position = [(232, -243),
                (247, -248),
                (262, -241),
                (277, -245),
]
for x, y in leg_position:
    draw_leg(leg, x, y)
leg.hideturtle()

# tail_set_up
tail = turtle.Turtle()
set_turtle(tail, '#93a2a9', '#93a2a9', 4)
move_turtle(tail, 276, -242)
tail.begin_fill()
tail.lt(40)
tail.fd(20)
tail.lt(-90)
tail.circle(4)
tail.end_fill()
tail.hideturtle()
