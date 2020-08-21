import math
def pi(f_x):
    return math.exp(f_x) / (1 + math.exp(f_x))
def fx(x1, x2, x3):
    return (-7 + x1*0.1 + x2*1 + x3*(-0.04))

print(pi(fx(32, 3, 12))) #0.21755
print(fx(44.8, 3, 12))
print(4.48-7)
print(pi(-1.28))