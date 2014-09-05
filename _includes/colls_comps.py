__author__ = 'cap10'

for y in [x*2 for x in range(-5, 50) if x > 0]:
    print(y)

squares = {x:x**2 for x in range(10)}
print("square map dict comprehension:", squares)

evensquares = {x:x**2 for x in range(10) if x % 2 == 0}
print("even squares map:", evensquares)

setcomp = {x % 2 for x in range(10)}
print("set comprehension", setcomp)