import random

beg = 0
end = 1

# random_integer = random.randint(beg, end)
# random_float = random.random()
# print(random_float)
# print(random_integer)

# love_score = random.randint(beg, end)
# print(f"Your love score is {love_score}")
random_gen = random.randint(beg, end)
if random_gen == 0:
    print("Heads")
else:
    print("Tails")
