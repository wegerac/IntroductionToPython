"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Andrew Weger.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(20)

andy = rg.SimpleTurtle('turtle')
rosie = rg.SimpleTurtle('turtle')
siri = rg.SimpleTurtle('turtle')
cortana = rg.SimpleTurtle('turtle')

andy.pen = rg.Pen('red', 20)
andy.speed = 10
andy.left(90)
andy.forward(200)

rosie.pen = rg.Pen('orange', 20)
rosie.speed = 10
rosie.right(90)
rosie.forward(200)

siri.pen = rg.Pen('green', 20)
siri.speed = 10
siri.forward(200)

cortana.pen = rg.Pen('blue', 20)
cortana.speed = 10
cortana.left(180)
cortana.forward(200)

andy.pen = rg.Pen('red', 5)
andy.pen_up()
andy.right(90)
andy.forward(20)
andy.left(90)
andy.pen_down()
for k in range(5):
    andy.draw_circle(20)
    andy.pen_up()
    andy.left(90)
    andy.forward(40)
    andy.right(90)
    andy.pen_down()

andy.draw_circle(20)

for k in range(4):
    andy.pen_up()
    andy.right(180)
    andy.forward(40)
    andy.left(180)
    andy.pen_down()
    andy.draw_circle(20)

rosie.pen_up()
rosie.right(90)
rosie.forward(20)
rosie.left(90)
rosie.pen_down()
rosie.pen = rg.Pen('orange', 5)
for k in range(5):
    rosie.draw_circle(20)
    rosie.pen_up()
    rosie.left(90)
    rosie.forward(40)
    rosie.right(90)
    rosie.pen_down()

rosie.draw_circle(20)

for k in range(4):
    rosie.pen_up()
    rosie.right(180)
    rosie.forward(40)
    rosie.left(180)
    rosie.pen_down()
    rosie.draw_circle(20)

cortana.pen_up()
cortana.right(90)
cortana.forward(20)
cortana.left(90)
cortana.pen_down()
cortana.pen = rg.Pen('blue', 5)
for k in range(5):
    cortana.draw_circle(20)
    cortana.pen_up()
    cortana.left(90)
    cortana.forward(40)
    cortana.right(90)
    cortana.pen_down()

cortana.draw_circle(20)

for k in range(4):
    cortana.pen_up()
    cortana.right(180)
    cortana.forward(40)
    cortana.left(180)
    cortana.pen_down()
    cortana.draw_circle(20)

siri.pen_up()
siri.right(90)
siri.forward(20)
siri.left(90)
siri.pen_down()
siri.pen = rg.Pen('green', 5)
for k in range(5):
    siri.draw_circle(20)
    siri.pen_up()
    siri.left(90)
    siri.forward(40)
    siri.right(90)
    siri.pen_down()

siri.draw_circle(20)

for k in range(4):
    siri.pen_up()
    siri.right(180)
    siri.forward(40)
    siri.left(180)
    siri.pen_down()
    siri.draw_circle(20)

boxy = rg.SimpleTurtle('turtle')
boxy.left(90)
boxy.speed = 10
boxy.pen_up()
boxy.forward(220)
boxy.left(90)
boxy.pen_down()
boxy.pen = rg.Pen('red', 5)
boxy.forward(220)
boxy.left(90)
boxy.forward(220)
boxy.pen = rg.Pen('blue', 5)
boxy.forward(220)
boxy.left(90)
boxy.forward(220)
boxy.pen = rg.Pen('orange', 5)
boxy.forward(220)
boxy.left(90)
boxy.forward(220)
boxy.pen = rg.Pen('green', 5)
boxy.forward(220)
boxy.left(90)
boxy.forward(220)
boxy.pen_up()
boxy.left(90)
boxy.forward(220)
boxy.right(180)
boxy.pen_down()
boxy.pen = rg.Pen('red', 5)
boxy.left(45)
boxy.forward(308)
boxy.left(180)
boxy.forward(308)
boxy.pen = rg.Pen('blue', 5)
boxy.right(90)
boxy.forward(308)
boxy.right(180)
boxy.forward(308)
boxy.right(90)
boxy.pen = rg.Pen('orange', 5)
boxy.forward(308)
boxy.left(180)
boxy.forward(308)
boxy.pen = rg.Pen('green', 5)
boxy.right(90)
boxy.forward(308)
boxy.left(180)
boxy.forward(308)
boxy.right(135)

window.close_on_mouse_click()
