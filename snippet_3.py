def get_square(number):
    return number ** 2

def get_cubes(numbers):
    cubes = []
    for number in numbers:
        cubes.append(number ** 3)
    return cubes

my_numbers = [1, 2, 3, 4, 5]

squares = []
for number in my_numbers:
    squares.append(get_square(number))

cubes = get_cubes(my_numbers)
