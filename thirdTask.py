numbers = [i for i in range(1, 16)]

print("Before swap:", numbers)

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("After first swap:", numbers)

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("After second swap:", numbers)