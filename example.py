class Example:
    def __init__(self, driver=None):
        self.driver = driver

    def func(self):
        return self.driver.get_name()