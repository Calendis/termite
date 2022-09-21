'''
    Termite example usage
'''
import os, time
from termite import Frame, Compositor

if __name__ == "__main__":
    inner_frame_1 = Frame.Positioned(True, 16, 9, 10, 12, 0, 0, 0, [])
    inner_frame_2 = Frame.Positioned(True, 20, 13, 50, 10, 0, 0, 0, [])
    inner_frame_3 = Frame.Positioned(True, 30, 9, 60, 25, 0, 0, 0, [])
    inner_frame_4 = Frame.Positioned(True, 8, 20, 120, 2, 0, 0, 0, [])
    outer_frame = Frame.Full(0, 0, 0, [inner_frame_1, inner_frame_2, inner_frame_3, inner_frame_4])

    term_wd = os.get_terminal_size()[0]
    term_ht = os.get_terminal_size()[1]
    dx = 1
    dy = 1
    while True:
        x = inner_frame_1.get_x()
        y = inner_frame_1.get_y()
        w = inner_frame_1.get_width()
        h = inner_frame_1.get_height()
        
        if (x + dx + w > term_wd):
            dx *= -1
        elif (x + dx < 0):
            dx *= -1

        if (y + dy + h > term_ht):
            dy *= -1
        elif (y + dy < 0):
            dy *= -1
        
        inner_frame_1.set_pos(x+dx, y+dy)

        renders = outer_frame.render_all()
        render = Compositor.compose(*renders)
        print(render, end="")
