import os
from termite import Chars

class Frame:
    def __init__(self, focused, wd, ht, x, y, h, s, v, containees):
        self.focused = focused
        self.size = [wd, ht]  # Width and height in terminal blocks
        self.pos = [x, y]
        self.color = [h, s, v] # HSV color
        self.containees = containees  # May be frames or widgets
        self.layer = 0
        term_size = os.get_terminal_size()
        self.term_wd = term_size[0]
        self.term_ht = term_size[1]

    def get_width(self):
        return self.size[0]
    
    def get_height(self):
        return self.size[1]

    def render(self):
        drawstr = ""
        
        # Create the top border
        drawstr += Chars.OUTER_TOPLEFT + Chars.OUTER_HORIZONTAL * (self.wd-2) + Chars.OUTER_TOPRIGHT

        # Create the left and right borders
        for y in range(self.ht-2):
            drawstr += Chars.OUTER_VERTICAL + Chars.I_WS * (self.wd-2) + Chars.OUTER_VERTICAL

        # Create the bottom border
        drawstr += Chars.OUTER_BOTLEFT + Chars.OUTER_HORIZONTAL * (self.wd-2) + Chars.OUTER_BOTRIGHT
        
        return drawstr

    def render_all(self):
        renders = [self.render()]

        for c in self.containees:
            renders.append(c.render())

        return renders

class Positioned(Frame):
    def __init__(self, focused, wd, ht, x, y, h, s, v, containees):
        super().__init__(focused, wd, ht, x, y, h, s, v, containees)

    
    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]
    
    def set_pos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def render(self):
        drawstr = ""

        # Define whitespace
        blank_lines_above = self.pos[1]
        blank_lines_below = self.term_ht - blank_lines_above - self.size[1]
        blank_width_before = self.pos[0]
        blank_width_after = self.term_wd - blank_width_before - self.size[0]
        
        # Create the top border
        drawstr += Chars.T_WS * self.term_wd * blank_lines_above
        drawstr += Chars.L_WS * blank_width_before
        drawstr += Chars.INNER_TOPLEFT
        drawstr += Chars.INNER_HORIZONTAL * (self.size[0]-2)
        drawstr += Chars.INNER_TOPRIGHT
        drawstr += Chars.R_WS * blank_width_after

        # Create the left and right borders
        for y in range(self.size[1]-2):
            drawstr += Chars.L_WS * blank_width_before + Chars.INNER_VERTICAL + Chars.I_WS*(self.size[0]-2) + Chars.INNER_VERTICAL + Chars.R_WS * blank_width_after

        # Create the bottom border
        drawstr += Chars.L_WS*blank_width_before
        drawstr += Chars.INNER_BOTLEFT
        drawstr += Chars.INNER_HORIZONTAL * (self.size[0]-2)
        drawstr += Chars.INNER_BOTRIGHT
        drawstr += Chars.B_WS * self.term_wd * blank_lines_below
        drawstr += Chars.R_WS * blank_width_after

        return drawstr

class Full(Frame):
    def __init__(self, h, s, v, containees):
        super().__init__(True, -1, -1, 0, 0, h, s, v, containees)
        self.wd = self.term_wd
        self.ht = self.term_ht