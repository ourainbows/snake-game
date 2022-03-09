from turtle import Turtle, Screen

#build snake body
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

class Snake:
    #Constructor
    def __init__(self):
         # save snake segments
        self.segments = []
        # method than created snake
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)
    
    def move(self):
        for seg_num in range(len(self.segments)-1, -1, -1):
            new_x = self.segments[seg_num].xcor()
            new_y = self.segments[seg_num].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].forward(20)