import math
line1 = 'xxxxxxxxxxxxxxxxxxxx'
line2 = 'x                  x'
line3 = '     HELLO WORLD    '

print(line1)
print(line2)
print(line3)
print(line2)
print(line1)
one = 1
print(one)
print(1)

# if statement
age_limit = 21

if age_limit > 19:
    print('Access grant')
else: 
    print('Access denied')

# ternary operation
age_limit = 17
print('Access grant') if age_limit > 18 else print('Access denied')

kiki = ('yh' , 'yh' ,'yh')
print(type(kiki))

phrase = 'I\'m good'
print(phrase)

menu = "menu".upper()
print(menu.center(100, "x"))
print("hayhay".ljust(14, '-') + "$2")


print(round(math.pi))

print(int(math.sqrt(64)))
print(math.pow(3 , 3))
deci_num = 3.17
print(round(deci_num ,0))

wwe = 123
print(wwe)

# coll = input('Please enter your age:\n')
# print(coll)

anime = 'gogo'.upper()
print(anime.center(24, "="))

x = 23.6
y = 17
print(x)
print(y)

print(float(y))
print(round(x))

# nums = list(range(0,101))
# print(nums)
# nums.remove(70)
# print(nums)
# nums.append(101)
# print(nums)

nums_2 = [5, 7, 8, 3, 9, 10, 5, 6, 4, 1, 0, 6, 88, 777, 3632, 7086, 656, 33, 7, 9]
#nums_2.sort(reverse=True)
#:print(nums_2)

print(nums_2)

print(sorted(nums_2, reverse=True))

print(nums_2)

nums_3 = [36, 70, 47, 687, 20, 346, 69,]
print(max(nums_3))

num_4 = 8
if num_4 > 0:
    print('positive')
elif num_4 == 0:
    print("zero")
elif num_4 < 0:
    print('negative')
else:
    print('invalid numer')