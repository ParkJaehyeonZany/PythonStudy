class Person:

    def __init__(self, name, id, age, height,weight):
        self.name = name
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"이름 : {self.name} 나이 : {self.age} 키 : {self.height} 몸무게 : {self.weight}"


print(Person('박재현', 'Zany', 27, 178, 65))
