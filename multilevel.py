class parent:
    def name(self, name):
        self.name = name


class Child(parent):
    def age(self, age):
        self.age = age


class GrandChild(Child):
    def gender(self, gender):
        self.gender = gender


gc = GrandChild()
gc.name('jack')
gc.age(21)
gc.gender('Male')

print(gc.name, gc.age, gc.gender)
