class Computer:
    def __init__(self, model , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.memory = 128
class Display:
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.resolution = "4K"
class SmartPhone(Display, Computer):
    def print_info(self):
    print(self.resolution)
    print(self.memory)
    print(self.model)

