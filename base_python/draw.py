from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    A = y1 - y0
    B = x1 - x0
    X = x0, Y = y0, d = 2A + B
    
    #octant 1
    while X <= x1:
        plot(x, y)
        if d > 0:
            Y++
            d += 2B
        X++
        d += 2A

    #octant 2
    while Y <= y1:
        plot(x, y)
        if d < 0:
            X++
            d += 2A
        Y++
        d += 2B

    #octant 7
    while Y <= y1:
        plot(x, y)
        if d > 0:
            Y--
            d -= 2B
        X--
        d -= 2A

    #octant 8
    while Y <= y1:
        plot(x, y)
        if d < 0:
            X--
            d -= 2A
        Y--
        d -= 2B
