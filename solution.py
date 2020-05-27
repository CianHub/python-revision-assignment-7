# 1
class Food:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print(f'name: {self.name}, kind: {self.kind}')


# 2

class Food2:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    @classmethod
    def describe_class(cls, name, kind):
        print(f'name: {name}, kind: {kind}')

    @staticmethod
    def describe_static(name, kind):
        print(f'name: {name}, kind: {kind}')


apple = Food2('apple', 'apple')
apple.describe_class(apple.name, apple.kind)


# 3

class Meat(Food):

    def cook(self):
        print(f'I\'m cooking this {self.name}')


class Fruit(Food):

    def clean(self):
        print(f'I\'m cleaning this {self.name}')

# 4


class Food3:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print(f'name: {self.name}, kind: {self.kind}')

    def __repr__(self):
        return str(self.__dict__)


choc = Food3('Chocolate', 'Sweet')
print(choc)
