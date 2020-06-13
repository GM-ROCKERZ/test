# def create_cubes(n):
# 	result = []
# 	for x in range(n):
# 		yield x**3

# for x in create_cubes(10):
# 	print(x)

# def generate_fibbon(n):

# 	a=1
# 	b=1
# 	for i in range(n):
# 		yield a
# 		a,b = b,a+b

# for number in generate_fibbon(10):
# 	print(number)


#next() function

# def simple_gen():
# 	for x in range(3):
# 		yield x

# for number in simple_gen():
# 	print(number)

# g= simple_gen()

# print(g)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#iter() function

s = 'hello'

for letter in 'hello':
	print(letter)

# print(next(s))

str_obj = iter(s)

print(next(str_obj))
print(next(str_obj))
print(next(str_obj))
print(next(str_obj))




