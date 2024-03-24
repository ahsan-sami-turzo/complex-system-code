import math
import turtle


def generate_sierpinski_carpet(n, l):
    # stop condition
    if n == 0:
        turtle.color('green')
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(l)
            turtle.left(90)
        turtle.end_fill()
    # recursive call
    else:
        for _ in range(4):
            generate_sierpinski_carpet(n - 1, l / 3)
            turtle.forward(l / 3)
            generate_sierpinski_carpet(n - 1, l / 3)
            turtle.forward(l / 3)
            turtle.forward(l / 3)
            turtle.left(90)

        turtle.update()


def calculate_fractal_dimension(n):
    N = 8 ** n  # number of self-similar pieces
    S = 3 ** n  # scaling factor
    D = math.log(N) / math.log(S)  # fractal dimension
    return D


if __name__ == "__main__":
    turtle.tracer(0)
    n = 4
    generate_sierpinski_carpet(n, 400)
    D = calculate_fractal_dimension(n)
    print(f"The fractal dimension of the Sierpinski Carpet with n={n} is {D}")
    turtle.done()
