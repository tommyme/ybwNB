def xy2wh(x1, x2, y1, y2):
    """x1 ,y1 小点"""
    w = x2-x1
    h = y2-y1
    x = x1
    y = y2
    return x, y, w, h
