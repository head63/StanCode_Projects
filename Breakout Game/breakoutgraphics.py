"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10         # Number of rows of bricks
BRICK_COLS = 10         # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        
        # Create a paddle
        self.paddle =GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2 ,y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        # self.paddle_height = self.window.height - PADDLE_OFFSET
        self.window.add(self.paddle)
        
        # Center a filled ball in the graphical 
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width//2-ball_radius, y=window_height//2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize variables
        self.score = 0 # 得分數
        self.ball_bouncing = False #檢測球是否正在動
        self.brick_number = brick_rows * brick_cols
        
        # Draw bricks
        color=['red','orange','yellow','green','blue']
        for j in range(brick_cols):
            for i in range(brick_rows):
                self.brick = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*i, y=brick_offset+(brick_height+brick_spacing)*j)
                self.brick.filled = True
                self.brick.fill_color = color[round(j//2)]
                self.window.add(self.brick)      

        # Score label
        self.score_label = GLabel('Score='+str(self.score))
        self.score_label.font = '-10'
        self.window.add(self.score_label, x=0, y=self.score_label.height)

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_bouncing)

    def move_paddle(self, mouse):
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2
 
    def start_bouncing(self, mouse):
        if not self.ball_bouncing:
            self.ball_bouncing = True
            self.__dx = random.randint(1,MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if (random.random()>0.5):
                self.__dx = -self.__dx

    def bouncing_ball(self):
        for x in range(self.ball.x, self.ball.x+self.ball.width+1, self.ball.width):
            for y in range(self.ball.y, self.ball.y+self.ball.height+1, self.ball.height):
                test_object = self.window.get_object_at(x, y)
                if test_object is not None:
                    if test_object is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy
                    elif test_object == self.score_label:
                        pass
                    else:
                        self.__dy = -self.__dy
                        self.window.remove(test_object)
                        self.score += 1
                        self.__dy += 1
                        self.brick_number -= 1
                        self.score_label.text = 'Score=' + str(self.score)
                    return

    def restart(self):
        self.ball.x = self.window.width//2 - self.ball.width
        self.ball.y = self.window.height//2 - self.ball.height
        self.__dx = self.__dy = 0
        self.ball_bouncing = False

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy
    
    def set_vx(self, new_vx):
        self.__dx = new_vx

    def set_vy(self, new_vy):
        self.__dy = new_vy
