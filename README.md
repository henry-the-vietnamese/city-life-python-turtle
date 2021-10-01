# Illustrate City Life Using Python Turtle
**Aim**: Using Python Turtle to draw an illustration of the city life, with house, car, animal, and so on.

To begin, I import the turtle() module, after which I define all of the functions I am going to use in the code. I then set the window for the project by setting the height and width. What is interesting is that I apply a gif image to the background to make it look more realistic and colourful. Therefore, I include that gif in the same zip file with other code so that it would run smoothly without error. Furthermore, for almost every element, I specify it with an appropriate name, such as house, roof, and dog using turtle.Turtle() method.

There are seven procedures which are pulled out from main.py to store in drawing_procedures.py so as to optimise and improve code legibility and code reuse.

Inside the draw_window(window, x, y) function (with the two arguments being the x- and y- coordinates of the window), a short for loop is used to draw the square-shape border of the window.

The draw_wheel(wheel, x1, y1) function has two arguments being the x- and y- coordinates of the wheel. These coordinates will be specified later when I get to that part. Inside that function, I divide it into two circumstances, which simply refers to the two wheels, after which I use a while loop to draw the wheel at the particular (x2, y2) position.

I begin drawing by going through the order:
- House overall
- Left, middle, and right roofs
- Door
- Windows (2 times)  
  -  Now I specify the coordinates of each window as arguments of the draw_window(x, y) function.
- Middle big window
- Chimney</br>
- Street</br>
- Roadside</br>
- Broken lines  
  -  I use a while loop to repeatedly draw a straight line, each of which is separated by 150 units – specified by the i variable – until i equals 250.
- Little stair in front of the door
- Oval trees (4 times)
- Big tree
- Leaf of the tree
- The lower part of the car
- The upper part of the car
- Wheels (2 times)
  -  Now I specify the coordinates of each wheel as arguments of the draw_wheel(x1, y1) function.
- Flag
- The star on the flag
- Dog face
  -  I use the circle(18) function to draw the face with a radius of 18 units.
- Eyes (2 times)  
  -  Now I specify the coordinates of each eye as arguments of the draw_eye(x, y) function.
- Mouth  
  -  I use the circle(3, 160) function to draw a circle of 3 units radius, but only 160 degrees of it is drawn to make it look better.
- Left ear
- Right ear
- Body
- Legs (4 times)  
  -  Now I specify the coordinates of each leg as arguments of the draw_leg(x, y) function.
-  Tail

# Output
![The output of running main.py](assets/output.jpg)
