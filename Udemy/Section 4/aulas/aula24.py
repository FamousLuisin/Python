iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()

print(next(iterator))
print(next(iterator))
print(next(iterator))


iterable = 'noki'
iterator = iterable.__iter__()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

