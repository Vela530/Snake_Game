from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from wall import Wall
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
wall = Wall()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    # screen.update()
    time.sleep(0.1)
    snake.move()

    

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_is_over()
    
    for end in snake.segments:
        if end == snake.segments[0]:
            pass
        elif snake.head.distance(end)<10:
            game_is_on = False
            scoreboard.game_is_over()
            
            
        

    
    
    
    
    
    

    


screen.exitonclick()













