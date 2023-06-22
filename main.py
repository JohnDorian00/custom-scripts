from example import ExampleClass


# сюды не смотри, тут просто симуляция класса драйвер
# как я понял - у тебя просто есть уже готовый объект driver, который я создаю ниже
class Driver:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# делаем объект драйвер, проверяем как работает из main
driver = Driver('driver_name')
driver.get_name()

# создаем объект класса ExampleClass, через этот объект есть доступ ко всем функциям
my_object_with_functions = ExampleClass(driver)

# юзаем функцию, выводим результат
print(my_object_with_functions.func())
