def convert_to_1D(x, y, size):
    result = (x - 1) * size + y - 1
    return result

def convert_to_2D(point, size):
    y = point % size
    x = point // size
    x += 1
    x += 1
    return (x, y)