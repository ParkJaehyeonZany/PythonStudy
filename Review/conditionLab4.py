import random

grade = random.randint(1,6)
if grade == 1 or grade == 2 or grade == 3:
    print(f"{grade} grade is the lower grade")
else:
    print(f"{grade} grade is the upper grade")