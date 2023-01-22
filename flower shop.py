class Flower:
    def __init__(self, name, color, price, stock):
        self.name = name
        self.color = color
        self.price = price
        self.stock = stock
    
    def check_stock(self):
        if self.stock < 10:
            print(f'Reorder {self.name}')
    def update_stock(self,new_stock):
        self.stock = new_stock
        self.check_stock()

class Bouquet:
    def __init__(self, name, flowers):
        self.name = name
        self.flowers = flowers

    def calculate_price(self):
        total_price = 0
        for flower in self.flowers:
            total_price += flower.price
        return total_price

class Shop:
    def __init__(self, name, bouquets):
        self.name = name
        self.bouquets = bouquets

    def display_bouquets(self):
        for bouquet in self.bouquets:
            print(f"{bouquet.name}: ${bouquet.calculate_price()}")

    def process_order(self, bouquet_name):
        for bouquet in self.bouquets:
            if bouquet.name == bouquet_name:
                for flower in bouquet.flowers:
                    flower.stock -= 1
                    flower.check_stock()
                break

flower1 = Flower("Rose", "Red", 2.50, 50)
flower2 = Flower("Lilac", "Purple", 3.75, 40)
flower3 = Flower("jasmine", "white", 3.50, 10)
flower4 = Flower("orchid", "white", 3, 40)
flower5 = Flower("mogra", "white", 2.11, 9)
flower6 = Flower("rose", "baby pink", 3.9, 60)
flower7 = Flower("marigold", "orange", 2.0, 30)
flower8 = Flower("Lily", "purple", 3.75, 20)

bouquet1 = Bouquet("Ro-Bouquet", [flower1, flower2, flower6, flower7])

shop = Shop("Flower Shop", [bouquet1])
shop.display_bouquets()
shop.process_order("Ro-Bouquet")
