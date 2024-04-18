print('Hello World, Welcome to Bullet.io!')
print('This is the basics of my code')

fruits = ['mango','apple','orange','kiwi']
#Basic operations
print(2 + 8)
print(10 / 2)
print(320)

name = 'Manasseh'
print(name)
#Printing single values in a string 
name = 'Photosynthesis'
print(name[0])
print(name[-8])
print(name[5:])
print(name[:5])

#defining a function
gogo = 'telegram'
print(gogo)

nums = (2, 4,6,-8)
#Conbining list and single strings 
exist = [name, nums, gogo]
print(exist)

print(nums)
#Editing the contents of a single string
print('Wow'+ name[5:])
#Using operators on a tuple
print(min(nums))
print(max(nums))
print(sum(nums))
#Using functions associated with list
letters = ['a', 'b', 'c', 'd', 'e', 'f']

slide = letters[1:3]
print(slide)

define = list([2,3,4,5])
print(type(define))
print(define)

numerics = [1, 2, 3, 4, 5, 6]

bread = letters[1:4]
print(bread)
#Changing values in a list
whole_nums = [1, 2, 3, 4, 5, 6]

whole_nums[0:2] = ['g', 'h']
print(whole_nums)
#Testing True or False statements and list datas
print('pine'in fruits)
print(list(fruits))
#Creating a Dictionary
cloud = {99:'venus',77:'mars'}
print(cloud)
#A list of words and their meanings to form Dictionary
words = {'cat':'The cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae and is commonly referred to as the domestic cat or house cat to distinguish it from the wild members of the family. Wikipedia','dog':"The dog is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct Pleistocene wolves, and the modern wolf is the dog's nearest living relative. Dogs were the first species to be domesticated by hunter-gatherers over 15,000 years ago before the development of agriculture."}
#Dictionary of planets
planets = {1:'Mercury',2:'Venus',3:'Earth',4:'Mars',5:'Jupiter',6:'Saturn',7:'Uranus',8:'Neptune'}
#Run codes for cloud Dictionary
print(cloud.get(99))
print(cloud.get(77))
print(cloud.get(3))
print(cloud.get(3,'saturn'))

cloud[3] = 'saturn'
print(cloud)

#List
h_bodys = ['mars','earth','neptune']
solids = ['books','stone','coal']
#Zipping together keys and values
mega_mix = dict(zip(h_bodys,solids))
print(mega_mix)
#Adding values to a Dictionary
mega_mix['jupiter'] = 'sand'
print(mega_mix)
#Single print a value out of Dictionary
print(mega_mix['mars'])
#Using the del function
del mega_mix['mars']
print(mega_mix)
#Below are keys to above codes
#Enter planet №in the space below
print(planets[7])
#Enter values either 'dog' or 'cat'
print(words['cat'])
#Testing id and types
data = 101
print(id(data))
print(type(data))
#Testing the len in-built function
raw_fact = [100,100100,62872,82728,27266,7265,462,1322,2309,26283,72725282,4678,354,46422,578536,4642,4646,577,864,133,46453,864,23354,7676,342,13243,7545,333,742,13456,543,3435,343535,8654,3453,45456765,242,555,532,777,3422,545,321,7543,56465,77464,56535,2323,313235455,98766,790686,7560]
print(len(raw_fact))
#Checking complex data
com = 5 + 2j
print(type(com))
#Testing the bool(true /false) function
k = 101
m = 297
print(k<m)
print(k>m)
print(k + m)
#Changing float to int and vice versal
a = 75
b = float(a)
print(b)

p = int(b)
print(p)

x = 31
#Changing to complex value
print(complex(p,x))

#Testing the function range
range(34)
print(list(range(0,34,2)))
#Assignment operators
x = 2
y = 4
m = x + y
print(m)
#shortcut of Adding values
m+= 2
print(m)
m-= 4
print(m)
#Assigning two values at once
a,b = 1,2
print(a)
print(b)
#Unary operators
b = 9
print(-b)
#Logic operators
r = 12
k = 21
print(r < k)
print(k < r)

print(r == k)

print(r <= k)
#Using not(!) function
print(k != r)
#Using And function
e = 6
f = 9
print(e < 12 and f > 8)
        #Number systems
#Changing a base 10 № to binary
print(bin(12))
#Changing back to base 10
print(0b1100)
#Using the octal data type
print(oct(62))
#Changing back to decimal 
print(0o76)
#Using HexaDemical number systems
print(hex(22))

      #Test
print(bin(31))
print(bin(52))
print(bin(65))

print(0b110011010)
#Swaping 2 variables
x = 9
y = 7

swap = x
x = y
y = swap
print(x)
print(y)
print(0b11000)
print(13 ^ 20)
#Bitwise operations
print(~15)

#And bitwise operator
print(52 & 23)

#Or bitwise operator
print(12 | 13)

#XOR bitwise operator
print(15 ^ 13)

#Left shift bitwise operator
print(0b11000)

#deleting a value from a list
kk = [1, 2, 3, 4, 5, 'ddk', 'hello']
del kk[2]
print(kk)


ppl = 'msk'
print(id(ppl))
