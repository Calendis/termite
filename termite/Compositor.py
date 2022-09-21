from termite import Chars

def compose(*renders):
    initial_compose = True
    composed_render = ""
    
    for r in renders:
        
        if initial_compose:
            composed_render = Chars.C_WS * len(r)
            initial_compose = False

        composed_render = compose_binary(composed_render, r)

    return composed_render

def compose_binary(s1, s2):
    if len(s1) != len(s2):
        print("Rendering error in compose_binary: render strings of unequal length:", len(s1), len(s2))
        return 1

    composed_render = ""
    for i in range(len(s1)):
        composed_render += compose_chars(s1[i], s2[i])

    return composed_render

def compose_chars(c1, c2):
    cs = sorted([c1, c2], key=char_sort)
    ks = [char_sort(c) for c in cs]

    if (ks[0] == 1):
        return cs[1]
    
    elif (ks[1] == 1):  # This should never happen!!! But if it does, I need to know
        print("Rendering error in compose_chars: render string not sorted!")
        return 2
    
    else:
        return "?"

def char_sort(c):
    ordering = {
    Chars.T_WS: 1,
    Chars.B_WS: 1,
    Chars.L_WS: 1,
    Chars.R_WS: 1,
    Chars.I_WS: 1,
    Chars.C_WS: 1
    }

    if c not in ordering:
        return 99
    
    return ordering[c]