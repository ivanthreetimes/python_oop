from project.food.food import Food


class Starter(Food):
    def __init__(self, name, price, grams):
        Food.__init__(self, name, price, grams)

