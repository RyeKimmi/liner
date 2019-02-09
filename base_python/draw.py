from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    A = y1 - y0
    B = x0 - x1
    m = -A/B
    X = x0
    Y = y0
    d = 2*A + B

    if m > 0:
        if m > 1:
            #octant 2           
            d = A + 2*B
            while Y <= y1:
                plot(screen, color, X, Y)
                if d < 0:
                    X+=1
                    d += 2*A
                Y+=1
                d += 2*B
        else:
            #octant 1
            d = 2*A + B
            while X <= x1:
                plot(screen, color, X, Y)
                if d > 0:
                    Y+=1
                    d += 2*B
                X+=1
                d += 2*A
    else:
        if m < -1:
            #octant 7
            d = -1*A - 2*B
            while Y >= y1:
                plot(screen, color, X, Y)
                if d > 0:
                    X-=1
                    d += 2*B
                Y-=1
                d += 2*A
        else:
            #octant 8
            d = -2*A - B
            while X >= x1:
                plot(screen, color, X, Y)
                if d < 0:
                    Y-=1
                    d += 2*A
                X-=1
                d += 2*B

'''        
    #octant 1
    while X <= x1:
        plot(screen, color, X, Y)
        if d > 0:
            Y+=1
            d += 2*B
        X+=1
        d += 2*A

    #octant 2
    while Y <= y1:
        plot(screen, color, X, Y)
        if d < 0:
            X+=1
            d += 2*A
        Y+=1
        d += 2*B

    #octant 7
    while Y <= y1:
        plot(screen, color, X, Y)
        if d > 0:
            Y-=1
            d -= 2*B
        X-=1
        d -= 2*A

    #octant 8
    while Y <= y1:
        plot(screen, color, X, Y)
        if d < 0:
            X-=1
            d -= 2*A
        Y-=1
        d -= 2*B
'''
