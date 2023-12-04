import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# The smallest number was 5, the biggest was 20.
# The smallest number that i have seen was 3, the largest was 9. No, it couldnt produced a 4,
# because the range starts at 3 with the step of 2. (3,5,7,9 are possible outputs)
# The smallest number was 2.6218617986724038, the largest was 5.168570323881752

print(random.randint(1, 100))  # prints random number from 1 to 100 inclusive
