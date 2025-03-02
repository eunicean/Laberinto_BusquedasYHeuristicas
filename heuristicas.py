def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidiana(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5