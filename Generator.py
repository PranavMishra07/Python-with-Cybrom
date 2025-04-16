def gen():
    yield 'A'
    yield 'B'
    yield 'C'
g=gen()
print(type(g))
print(next(g))#A
print(next(g))#B
print(next(g))#C
