# Класс с функциями
class ExampleClass:
    # Это конструктор, сюда передаем объект драйвер, когда создаем наш объект в main.py
    def __init__(self, driver=None):
        self.driver = driver

    def func(self):
        # тут self.driver тоже самое, что driver в main.py (ну мы его и передали при создании объекта)
        # есть доступ ко всем полям и методам объекта
        return self.driver.get_name()