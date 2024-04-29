import turtle #for drawing graphics
import random #generating random numbers

# the below piece of code is to define the 
# width and height constant game window dimensions
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10 #the size of the food 
DELAY = 100 # the delay between each frame of the game

# the movement offsets for the snake in different directions
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# reset function- initialize(snake's initial position, direction, and the food's position) or to reset the game,
def reset():
    global snake, snake_direction, food_pos, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    # screen.update() Only needed if we are fussed about drawing food before next call to `draw_snake()`.
    move_snake() # to start the game


def move_snake(): # movement of the snake
    global snake_direction

    #  Next position for head of snake.
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:
        reset()
    else:

        snake.append(new_head)
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

        #  Allow screen wrapping
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < - WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        # Clear previous snake stamps
        pen.clearstamps()

        # Draw snake
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        # Refresh screen
        screen.update()

        # Rinse and repeat
        turtle.ontimer(move_snake, DELAY)


def food_collision(): # checks the collision of the food and snake
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True #if collision
    return False # if not


def get_random_food_pos(): # random position of the food
    x = random.randint(-int(WIDTH / 2) + FOOD_SIZE, int(WIDTH / 2) - FOOD_SIZE)
    y = random.randint(-int(HEIGHT / 2) + FOOD_SIZE, int(HEIGHT / 2) - FOOD_SIZE)
    return (x, y)



def get_distance(pos1, pos2):#the Euclidean distance between two points
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def go_up():#controlling the direction of the snake 
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_right():#controlling the direction of the snake 
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_down():#controlling the direction of the snake 
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_left():#controlling the direction of the snake 
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


# Screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake  Game")
screen.bgcolor("black")
screen.setup(500, 500)
screen.tracer(0)

# Pen- creates the snake's body segments with a square shape 
pen = turtle.Turtle("square")
pen.penup()
pen.pencolor("yellow")

# Food- food for the snake with a circular shape
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)  # Default size of turtle "square" shape is 20.
food.penup()

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Let's go
reset()
turtle.done()
#reset() function to start the game and enters the event loop with 
#turtle.done() to keep the window open and responsive to user input.