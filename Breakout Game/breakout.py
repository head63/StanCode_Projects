"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000/50   # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:    
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)

        # Add the animation loop here!
        graphics.bouncing_ball()

        # Hits the side and bounces
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_vx(-vx)
        if graphics.ball.y <= 0:
            graphics.set_vy(-vy)

        # Lose life
        elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.restart()
            lives -= 1
        pause(FRAME_RATE)

        # End the game - Game Over
        if lives == 0:
            over = GLabel('Game Over')
            over.font = '-20'
            graphics.window.add(over, x=(graphics.window.width-over.width)/2, y=graphics.window.height)
            break

        # End the game - Win
        if graphics.brick_number == 0:
            win = GLabel('You Win!')
            win.font = '-20'
            graphics.window.add(win, x=(graphics.window.width-win.width)/2, y=graphics.window.height)
            break 

        
 
if __name__ == '__main__':
    main()
