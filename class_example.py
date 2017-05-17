class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    A = person('mayuri',5)
    B = person('anay',2)
    print(A.age)
    print(B.name)
