import random

start = random.randint(1,10)
end = random.randint(30,40)

sum = 0
for num in range(start,end+1):
    if num % 2 == 0:
       sum += num
print(f"Sum from {start} to {end} : {sum}")