# Madison Fletcher
# 1868748
space = ''
password = input()
for x in password:
    if x == 'i':
        space = space + '!'
    elif x == 'a':
        space = space + '@'
    elif x == 'm':
        space = space + 'M'
    elif x == 'B':
        space = space + '8'
    elif x == 'o':
        space = space + '.'
    else:
        space = space + x
space = space + 'q*s'
print(space)
