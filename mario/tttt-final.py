import turtle

def main():

    t = turtle.Turtle()
    t2 = turtle.Turtle()
    s = turtle.Screen()
    
    
    s.addshape('9.gif')
    t.shape('9.gif')
    t2.setpos(50, 50)
    
    
    s.addshape('3.gif')
    
    t2.shape('3.gif')
    t.shapesize(3, 2, 5)
    
    
 
if __name__ == "__main__":
    main()
