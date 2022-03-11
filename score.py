from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.write(f"Score: {self.score}", font=(FONT), align=ALIGN)
    
    def increase_score(self):
        self.clear()
        self.score += 1 
        self.update_score()

    def game_over(self):
        self.clear()
        self.write("GAME OVER", font=(FONT), align=ALIGN)