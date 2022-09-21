from termite import Frame, Compositor

def main():
    inner_frame_1 = Frame.Positioned(True, 16, 9, 15, 10, 0, 0, 0, [])
    inner_frame_2 = Frame.Positioned(True, 32, 10, 20, 14, 0, 0, 0, [])
    outer_frame = Frame.Full(0, 0, 0, [inner_frame_1, inner_frame_2])
    renders = outer_frame.render_all()
    render = Compositor.compose(*renders)
    print(render)

if __name__ == "__main__":
    main()