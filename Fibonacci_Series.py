def fibonacci():
    first_item, second_item, sum = 0, 1, 0
    yield first_item
    yield second_item
    while True:
        sum = first_item + second_item
        yield sum
        first_item, second_item = sum, first_item
f = fibonacci()

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))