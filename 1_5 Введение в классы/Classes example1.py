class Goat:
    legs_number = 4

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __str__(self):
        s = "weight = {}, height = {}, legs = {}".format(self.weight, self.height, self.legs_number)
        return s


marusya = Goat(60, 40)
notka = Goat(66, 44)
notka.legs_number = 6

a = [marusya, notka]
for i in a:
    print(i)
