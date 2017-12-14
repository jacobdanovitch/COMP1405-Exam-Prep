class Product():
    def __init__(self, description, price, inventory ):
        self.description = description
        self.inventory = inventory
        self.price = price

    def getPrice(self):
        return self.price

    def getInventory(self,size):
        return self.inventory[size]

    def purchase(self, size, n):
        self.inventory[size] -= n
        return n*self.price

    def shippment(self, size, n):
        self.inventory[size] += n

    def sale(self, pct):
        self.price *= (1-pct)

shirt = Product("shirt", 4.95, {
    "S":10,
    "M":15,
    "L":15,
    "XL":10
})

print(shirt.getPrice(), shirt.getInventory("L"))
shirt.sale(0.2)
print("Buying 5 L shirts")
print(shirt.purchase("L", 5), shirt.getInventory("L"))
print("Shippment for 10 S shirts")
shirt.shippment("S",10)
print(shirt.getInventory("S"))