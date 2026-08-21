numbers = [1,2,3,4,5]

square = [number **2 for number in numbers]
print(square)

cube = [number ** 3 for number in numbers]
print(cube)

#if contion

results = [number for number in numbers if number % 2 == 0]
print(results)
