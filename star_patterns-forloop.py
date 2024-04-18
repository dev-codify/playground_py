 #star pattern rectangle
for i in range(4):
    print()
    for i in range(4):
        print('* ', end="")

print('')
print('')
# star pattern right angle triangle
for r in range(4):
    print()
    for r in range(1+r):
        print('* ',end="")
print('')
print('')
# star pattern inverse right triangle
for ir in range(4):
    print()
    for ir in range(4-ir):
        print('* ',end="")