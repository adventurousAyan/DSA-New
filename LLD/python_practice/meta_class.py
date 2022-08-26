class Foo:
    def show(self):
        print("Hello World")


t = type("Test", (Foo,), {"x": 5})
print(t().show())


class MyMeta(type):
    def __new__(self, name, base, attrs):
        print(attrs)
        return type(name, base, attrs)


class MyClass(metaclass=MyMeta):
    x = 10
    y = 20

    def hello():
        print("Inside main class")


MyClass()
