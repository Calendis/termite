'''
    Termite example usage
'''
import os
from termite import Frame

if __name__ == "__main__":
    test_frame_1 = Frame.Positioned(True, 16, 9, 10, 10, 0, 0, 0, [])
    test_frame_0 = Frame.Full(0, 0, 0, [test_frame_1])
    render_0 = test_frame_0.render()
    
    print(render_0)
    print("Rendering done. Info:")
    print("Render length:", len(render_0))