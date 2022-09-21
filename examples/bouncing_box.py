'''
    Termite example usage
'''
import os, time
from termite import Frame

if __name__ == "__main__":
    test_frame_0 = Frame.Full(0, 0, 0, [])
    test_frame_1 = Frame.Positioned(True, 16, 9, 10, 10, 0, 0, 0, [])
    render_0 = test_frame_0.render()
    render_1 = test_frame_1.render()

    term_wd = os.get_terminal_size()[0]
    term_ht = os.get_terminal_size()[1]
    dx = 1
    dy = 1
    while True:
        x = test_frame_1.get_x()
        y = test_frame_1.get_y()
        w = test_frame_1.get_width()
        h = test_frame_1.get_height()
        
        if (x + dx + w > term_wd):
            dx *= -1
        elif (x + dx < 0):
            dx *= -1

        if (y + dy + h > term_ht):
            dy *= -1
        elif (y + dy < 0):
            dy *= -1
        
        test_frame_1.set_pos(x+dx, y+dy)

        render_1 = test_frame_1.render()
        print(render_1, end="")
        time.sleep(0.1)