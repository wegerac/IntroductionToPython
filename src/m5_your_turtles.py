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
# TODO: 2.
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

window.close_on_mouse_click()
