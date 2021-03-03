# Madison Fletcher
# 1868748
# equation ax + by = c
a = int(input())
b = int(input())
c = int(input())
# Equation dx + ey = f
d = int(input())
e = int(input())
f = int(input())
true_or_false = False  # used to check if the conditional statement is true or not
# before I used this statement it would just print "No solution" until the for loop was done
for x in range(-10, 10):
    for y in range(-10, 10):
        if a * x + b * y - c == 0 and d * x + e * y - f == 0:
            true_or_false = True
            print(x, y)
if not true_or_false:
    print("No solution")
