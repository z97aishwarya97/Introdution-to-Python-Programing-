# Implementation of classic arcade game Pong
# Import modules
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [-random.randrange(60, 180)/60,random.randrange(120, 240)/60]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel[1] = -random.randrange(60, 180)/60
    if right == True:
        ball_vel[0] = random.randrange(120, 240)/60
    else:
        ball_vel[0] = -random.randrange(120, 240)/60
    pass

# define event handlers
def newgame():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn(0 == random.randrange(0,11) % 2)
    pass

def draw(canvas):
    global score1, score2, paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos < (HALF_PAD_HEIGHT) and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle2_pos < (HALF_PAD_HEIGHT) and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle1_pos > (HEIGHT - (HALF_PAD_HEIGHT)) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos > (HEIGHT - (HALF_PAD_HEIGHT)) and paddle2_vel > 0:
        paddle2_vel = 0    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel        
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Grey")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Grey")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Grey")
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos-HALF_PAD_HEIGHT), (0, paddle1_pos+HALF_PAD_HEIGHT), (PAD_WIDTH-3, paddle1_pos+HALF_PAD_HEIGHT),(PAD_WIDTH-3,paddle1_pos-HALF_PAD_HEIGHT)], PAD_WIDTH-1, "Teal","Teal")
    canvas.draw_polygon([(WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH, paddle2_pos+HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH+3, paddle2_pos+HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH+3,paddle2_pos-HALF_PAD_HEIGHT)], PAD_WIDTH-1, "Red","Red")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS) or ball_pos[1] <= (BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT):
            spawn(True)
            score2 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
            
    if  ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT):
            spawn(False)
            score1 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
            
    # draw ball and scores
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    canvas.draw_text(str(score1), (170, 50), 36, "Teal")
    canvas.draw_text(str(score2), (400, 50), 36, "Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong Battle", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", newgame, 100)

# start frame
newgame()
frame.start()

