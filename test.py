class test:
    def __init__(self, first_name, last_name):
        test.first_name = first_name
        test.last_name = last_name

    def name(self):
        print(
            f"my first name is {self.first_name} and my last name is {self.last_name}"
        )


myname = test("Jesse", "Akasia")

print(myname.name())
