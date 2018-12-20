import turtle
import random
import time

# set up window
wn = turtle.Screen()
wn.title("a very hungry caterpillar by MrsRobot")
wn.bgcolor("lightgrey")
wn.delay(25) # changing speed of refresh rate
turtle.setup(700,700) # window size


# create main turtle which represents snake head
snake = turtle.Turtle()
snake.penup() # to not draw a line while moving
snake.shape("turtle")
snake.turtlesize(1.5,1.5,None) # to have the body bigger than the tail
snake.color("red")
snake.speed(10)

# create an empty variable for defining directions later on
snake_direction = "" 

# create variables for score and high score
score = 0
high_score = 0


# create turtle that will write the scoreboard
score_holder = turtle.Turtle()
score_holder.color("blue")
score_holder.speed(0) # set speed to the fastest so scoreboard is appears immediately when game starts
score_holder.penup() # to not drag a line behind moving the turtle
score_holder.goto(0, 300) # defining that turtle writes the scoreboard on top of the y coordinate
score_holder.hideturtle() # to not see the actual turtle, only it's writing
score_holder.write("High Score: 0     Points: 0", align = "center", font = ("Arial", 20, "normal")) 

# teaching the snake how to turn using nonfruitful functions
def up():
    #accumulator = 0 # this was a failed approach to get the snake moving by itself
    if snake.heading() == 0:
        snake.left(90)
    elif snake.heading() == 180:
        snake.right(90)
    direction()
    #print(snake_direction)

    """while not (wn.onkey(left, "a") or wn.onkey(right, "d")):
        accumulator += 10
        snake.sety(accumulator)""" # same failed approach as in line 40

def down():
    if snake.heading() == 0:
        snake.right(90)
    elif snake. heading() == 180:
        snake.left(90)
    direction()
    #print(snake_direction) # this was to identify bugs during the process
    

def left():
    if snake.heading() == 90:
        snake.left(90)
    elif snake.heading() == 270:
        snake.right(90)
    direction()
    #print(snake_direction) # this was to identify bugs during the process

def right():
    if snake.heading() == 90:
        snake.right(90)
    elif snake. heading() == 270:
        snake.left(90)
    direction()
    #print(snake_direction) # this was to identify bugs during the process


# creating a function that returns where the snake head is pointing towards
def direction():
    global snake_direction
    if snake.heading() == 0:
        snake_direction = "right"
    elif snake.heading() == 90:
        snake_direction = "up"
    elif snake.heading() == 180:
        snake_direction = "left"
    elif snake.heading() == 270:
        snake_direction = "down"
    #print(snake_direction) # this was to identify bugs during the process


# creating a function that gets the snake to move by itself using the coordinates
def movement():
    direction()
    if snake_direction == "right":
        snake.setx(snake.xcor() +10)
    elif snake_direction == "up":
        snake.sety(snake.ycor() +10)
    elif snake_direction == "left":
        snake.setx(snake.xcor() -10)
    elif snake_direction == "down":
        snake.sety(snake.ycor() -10)



# link arrows to actions
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(down, "Down")

# tell the program to react to keyboard input
wn.listen()       

# create random food items
rdm = random.Random() # from the random library
random_turtle = rdm.randrange(-330, 330) # set range a bit smaller than the window width, so the food elements don't appear half outside the window


# create food turtle
food = turtle.Turtle()
food.color("black")
food.shape("circle")
food.penup()
food.speed(10)
food.hideturtle() # to not see the food moving from it's old place
wn.delay(1) # remove the delay so the food distributing is as fast as possible
food.goto(100, 100) # always send the initial food item to the same place
food.showturtle() # to see the food item like a pop-up at the new place
wn.delay(25) # reset the delay

# create empty list for adding turtle tail elements
turtle_tail = []

# create beginning time delay
tail_delay = 25

while True:
    wn.update()


    # reset game if snake collides with the window borders
    x,y = snake.position()
    if x > 350 or x < -350 or y < -350 or y > 350:
        #print("done") # this was to identify bugs during the process
        snake.hideturtle()
        wn.delay(1) # speed up process of resetting game
        #new_tail.hideturtle() # this was a failed approach
        for element in (turtle_tail): # send all the tail elements to a place outside the window
            element.goto(1234,1234)
        turtle_tail.clear() # reset the tail list as an empty list
        #print(len(turtle_tail)) # this was to identify bugs during the process

        # display game over
        over = turtle.Turtle()
        over.color("black")
        over.speed(0)
        over.hideturtle() # hide snake so user can't see it moving back to start position
        over.penup()
        over.goto(0, 100)
        over.write("GAME OVER", align = "center", font = ("Arial", 100, "bold"))
        time.sleep(1) # display message for only a second
        over.clear() # remove game over message

        snake.home() # send the snake to it's original 0,0 position
        snake_direction = "" # empty it's direction variable
        snake.showturtle() # display snake for new game
        wn.delay(25)

        # move food to a new random place
        x = random.randint(-340, 340)
        y = random.randint(-340, 340)
        wn.delay(1)
        food.hideturtle()
        food.goto(x, y)
        food.showturtle()

        # reset scoreboard
        score = 0 # reset current score
        score_holder.clear() 
        score_holder.write("Score: 0  High Score: {}".format(high_score), align = "center", font = ("Arial", 20, "normal")) # leave high_score value there
        #print("im inside the border collision") # this was to identify bugs during the process

   # death by suicide
    for element in turtle_tail:
       if element.distance(snake) < 10:
            #print("IM INSIDE THE SUICIDE PART") # this was to identify bugs during the process
            snake.hideturtle()
            wn.delay(1) # speed up process of resetting game
            for element in (turtle_tail):
                element.goto(1234,1234) # send tail elements to a place outside the window, so user can't see them
            turtle_tail.clear()

            # reset snake
            snake.home() # send snake to it's initial position 0,0
            snake_direction = ""
            snake.showturtle()
            wn.delay(25)

            # reset scoreboard
            score = 0 #reset current score
            score_holder.clear()
            score_holder.write("Score: 0  High Score: {}".format(high_score), align = "center", font = ("Arial", 20, "normal")) # leave high_score value there




      
    if (snake.distance(food) < 15): # or (x > 350 or x < -350 or y < -350 or y > 350) # this didn't work as it created many bugs, so it was split into two parts
        # enter the if when the food has been eaten 
        x = random.randint(-340, 340)
        y = random.randint(-340, 340)
        wn.delay(1)
        food.hideturtle()
        food.goto(x, y)
        food.showturtle()
        if tail_delay > 0: # as long as the time is positive, substract one millisecond
            wn.delay(tail_delay-2)

        new_tail = turtle.Turtle()
        new_tail.shape("circle")
        new_tail.color("red")
        new_tail.penup()
        new_tail.speed(10)
        turtle_tail.append(new_tail)
        #print("im inside the food loop") # this was to identify bugs during the process

        # add 10 points to the scoreboard after eating food
        score += 10

        # update high score if necessary
        if score > high_score:
            high_score = score

        score_holder.clear()
        score_holder.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Arial", 20, "normal"))

    # make tail elemement take place of previous tail element
    for element in range(len(turtle_tail)-1, 0, -1):
        if(snake_direction=="up"):
            x = turtle_tail[element-1].xcor()
            y = turtle_tail[element-1].ycor()-10
            turtle_tail[element].goto(x,y)
            #print("other tails up") # this was to identify bugs during the process
        elif(snake_direction=="down"):
            x = turtle_tail[element-1].xcor()
            y = turtle_tail[element-1].ycor()+10
            turtle_tail[element].goto(x,y)
            #print("other tails down") # this was to identify bugs during the process
        elif(snake_direction=="right"):
            x = turtle_tail[element-1].xcor()-8
            y = turtle_tail[element-1].ycor()
            turtle_tail[element].goto(x,y)
            #print("other tails right") # this was to identify bugs during the process
        elif(snake_direction=="left"):
            x = turtle_tail[element-1].xcor()+8
            y = turtle_tail[element-1].ycor()
            turtle_tail[element].goto(x,y)
            #print("other tails left") # this was to identify bugs during the process
        #print(turtle_tail[0].distance(turtle_tail[1])) # this was to identify bugs during the process

    # replace main turtle with the first tail element
    if len(turtle_tail) > 0:
        if(snake_direction=="up"):
            x = snake.xcor()
            y = snake.ycor()-5
            turtle_tail[0].goto(x,y)
        elif(snake_direction=="down"):
            x = snake.xcor()
            y = snake.ycor()+5
            turtle_tail[0].goto(x,y)
        elif(snake_direction=="left"):
            x = snake.xcor()+5
            y = snake.ycor()
            turtle_tail[0].goto(x,y)
        elif(snake_direction=="right"):
            x = snake.xcor()-5
            y = snake.ycor()
            turtle_tail[0].goto(x,y)
        #print("first tail") # this was to identify bugs during the process
        
        
    if snake_direction != "":
        movement()



# close the application
wn.mainloop()
