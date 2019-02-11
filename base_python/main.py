from display import *
from draw import *
import random

screen = new_screen()

'''
\/\/\/ TESTING CASES \/\/\/
color1 = [ 255, 0, 0 ]
color2 = [ 0, 255, 0 ]
color7 = [ 0, 0, 255 ]
color8 = [ 255, 255, 0 ]
slope1 = [ 255, 0, 255 ]
slope0 = [ 0, 255, 255 ]
slopen1 = [ 255, 255, 255 ]
slopeun = [ 100, 100, 100 ] 
#octant 1 PASS
draw_line(0, 0, 500, 250, screen, color1)
#octant 2 PASS
draw_line(0, 0, 250, 500, screen, color2)
#octant 7 PASS
draw_line(0, 500, 250, 0, screen, color7)
#octant 8 PASS
draw_line(0, 500, 500, 250, screen, color8)
#slope 1 PASS
draw_line(0, 0, 500, 500, screen, slope1)
#slope 0 PASS
draw_line(0, 250, 500, 250, screen, slope0)
#slope -1 PASS
draw_line(0, 500, 500, 0, screen, slopen1)
#slope undefined PASS
draw_line(250, 0, 250, 500, screen, slopeun)
/\/\/\ TESTING CASES /\/\/\
'''

R = [ 255, 0, 0 ]
G = [ 0, 255, 0 ]
B = [ 0, 0, 255 ]
Y = [ 255, 255, 0 ]
M = [ 255, 0, 255 ]
C = [ 0, 255, 255 ]
W = [ 255, 255, 255 ]

for j in range(10):
    for i in range(51):
        draw_line(random.randint(0,2*i), random.randint(0,2*i), random.randint(2*i,8*i), random.randint(2*i,8*i), screen, R)    
        R[0] -= 5
        R[1] += 3
        R[2] += 3
        i += 1
    R = [ 255, 0, 0 ]
    j += 1

display(screen)
save_extension(screen, 'img.png')
