import re

brunch = {
'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}


early_bird = {
'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner = {
'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = {
'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}


class Menu:
    def __init__(self,name,items,start_time,end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return("{a} menu available from {b} to {c}".format(a = self.name, b = self.start_time, c = self.end_time))
    
    def calculcate_bill(self,purchased_items):
        total=0.0
        for item in purchased_items:
            total += self.items[item]
        return total

class Franchise:
    def __init__(self,address,menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return("Located at {a}".format(a = self.address))

    def available_menus(self, time):
      available_menus=[]
      update_x=[]
      print("avail menus\n")
      for menus in self.menus:
        #print(type(menus))
        x = re.split("\D", str(menus)) 
        for e in x:
          if (e != ""):
            update_x.append(e)
        print(update_x)
        #print(menus)
      print("END avail menus\n")
    

brunch = Menu('Brunch',brunch,'11am','4pm')
early_bird = Menu('Early Bird',early_bird,'3pm','6pm')
dinner = Menu('Dinner',dinner,'3pm','6pm')
kids = Menu("Kid's",kids,'1am','9pm')

flagship=Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
juniors=Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

print(flagship)
print(juniors)

print(flagship.available_menus('11am'))

print("%.2f" %brunch.calculcate_bill(['pancakes', 'home fries', 'coffee']))
print("%.2f" %early_bird.calculcate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
print(kids)
