from example import Example


class Driver:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


driver = Driver('driver_name')

my_object = Example(driver)
print(my_object.func())
