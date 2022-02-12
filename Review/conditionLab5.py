import random

score = random.randint(0, 100)
if score >= 90:
    print(f"{score} is A.")
elif score >= 80:
    print(f"{score} is B.")
elif score >= 70:
    print(f"{score} is C.")
elif score >= 60:
    print(f"{score} is D.")
else:
    print(f"{score} is F.")