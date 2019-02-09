from display import *
from draw import *

screen = new_screen()
color1 = [ 255, 0, 0 ]
color2 = [ 0, 255, 0 ]
color7 = [ 0, 0, 255 ]
color8 = [ 255, 255, 0 ]
slope1 = [ 255, 0, 255 ]
slope0 = [ 0, 255, 255 ]
slopen1 = [ 255, 255, 255 ]
slopeun = [ 100, 100, 100 ] 

#octant 1 PASS
#draw_line(0, 0, 500, 250, screen, color1)
#octant 2 PASS
#draw_line(0, 0, 250, 500, screen, color2)
#octant 7
draw_line(0, 500, 250, 0, screen, color7)
#octant 8
draw_line(0, 500, 500, 250, screen, color8)
#slope 1
#draw_line(0, 0, 500, 500, screen, slope1)
#slope 0
#draw_line(0, 250, 500, 250, screen, slope0)
#slope -1
#draw_line(0, 500, 500, 0, screen, slopen1)
#slope undefined
#draw_line(0, 0, 0, 500, screen, slopeun)

display(screen)
save_extension(screen, 'img.png')
