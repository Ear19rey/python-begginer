#水果類別
class Fruits:
    #建構式
    def __init__(self,color,taste):
        self.color = color #顏色屬性
        self.taste = taste #口味屬性
    #方法(Method)
    def describe(self):
        print(f"This fruit's color is {self.color} ,and it tastes {self.taste}!")

watermelon = Fruits("green","sweet, crispy")
grape = Fruits("purple","sweet, soft")

watermelon.describe()
grape.describe()

fruit = ['apple','banana', 'guava', 'mango']
color = ['red', 'yellow', 'green', 'yellow']
taste = ['sweet, hard', 'sweet, soft', 'sweet, hard', 'sour, soft']

for i in range(4):
    fruit[i] = Fruits(color[i],taste[i])

apple.describe()
