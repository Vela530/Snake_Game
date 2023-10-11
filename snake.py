from turtle import Turtle, Screen
import time

startingplaces = [(40,0), (20,0), (0,0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

move_distance = 20
screen = Screen()



class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in startingplaces:
            tim = Turtle()
            tim.shape("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            #tim.speed("slowest")
            self.segments.append(tim)



    def add(self):
        new_seg = Turtle()
        new_seg.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_seg)

        screen.update()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        
        
        

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
                
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    
    
        
            