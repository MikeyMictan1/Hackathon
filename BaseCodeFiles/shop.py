from player import Player

class Item:
    def __init__(self, category, name, price, effects):
        self.category = category
        self.name = name
        self.price = price
        self.effects = effects

class ShoppingSystem:
    def __init__(self):
        self.cart = []
        self.player = Player()
        self.ownedItems = []
        self.totalCost = 0
        self.happinessLevelIncrease = 0
        self.hungerLevelIncrease = 0
        self.thirstLevelIncrease = 0
        self.items = {
                "Food": [
                Item('Food', 'Breakfast', 5, 10),
                Item('Food', 'Lunch', 5, 10),
                Item('Food', 'Dinner', 5, 10),
                Item('Food', 'Snacks', 5, 10),
                Item('Food', 'Fruits', 5, 10),
                Item('Food', 'Pastries', 5, 10)
            ],

            "Clothes": [
                Item('Clothes', 'Casual', 5, 10),
                Item('Clothes', 'Stylish', 5, 10),
                Item('Clothes', 'Sporty', 5, 10),
                Item('Clothes', 'Bedtime', 5, 10)
            ],

            "Drinks": [
                Item('Drinks', 'Juice', 5, 10),
                Item('Drinks', 'Water', 5, 10),
                Item('Drinks', 'Milk', 5, 10),
                Item('Drinks', 'Hot Chocolate', 5, 10)
            ],

            "Decorations": [
                Item('Decorations', 'Plant', 5, 10),
                Item('Decorations', 'Bowl', 5, 10),
                Item('Decorations', 'Poster', 5, 10),
                Item('Decorations', 'Plushie', 5, 10)
            ]
        }

    def addItemsToCart(self):
        for category, items in self.items.items():
            for item in items:
                decision = input(f"Do you want {item.name}? Y/N ").strip().upper()
                if decision == 'Y':
                    self.cart.append(item)


    def calculateTotals(self):
        for item in self.cart:
            if item.category == 'Food':
                self.hungerLevelIncrease += item.effects
            elif item.category in ('Clothes', 'Decorations'):
                self.happinessLevelIncrease += item.effects
            elif item.category == 'Drinks':
                self.thirstLevelIncrease += item.effects
            self.totalCost += item.price
            if item.name not in self.ownedItems:
                self.ownedItems.append(item.name)
        print("Hunger Level Decrease: ", self.hungerLevelIncrease)
        print("Happiness Level Increase: ", self.happinessLevelIncrease)
        print("Thirst Level Decrease: ", self.thirstLevelIncrease)

    def checkout(self):
        self.calculateTotals()
        if self.totalCost <= self.player.currentBalance:
            self.player.update_balance(-self.totalCost)
            print("Items have been bought.")
        else:
            print("Not enough balance to buy these items.")
        print("Remaining Balance:", self.player.currentBalance)

ShoppingSystem = ShoppingSystem()
ShoppingSystem.addItemsToCart()
ShoppingSystem.calculateTotals()
ShoppingSystem.checkout()
