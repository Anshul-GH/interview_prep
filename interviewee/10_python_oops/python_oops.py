# ref: https://www.youtube.com/watch?v=Ej_02ICOIgs

# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = 

# print(item1)
# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# item1 = Item("Phone", 100, 5)
# item1.pay_rate = 0.9
# item1.apply_discount()
# print(item1.price)
# print(item1.calculate_total_price(item1.price, item1.quantity))
# print(item1.name, item1.price, item1.quantity)
# print(item1.calculate_total_price())

# item2 = Item("Laptop", 1000, 3)
# item2.apply_discount()
# print(item2.price)
# print(item2.calculate_total_price(item2.price, item2.quantity))
# print(item2.name, item2.price, item2.quantity)
# print(item2.calculate_total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# __dict__ to fetch all attributes
# print(Item.__dict__)
# print(item1.__dict__)
# print(item2.__dict__)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 4)
# item5 = Item("Keyboard", 75, 6)

# print(Item.all)

# for instance in Item.all:
#     print(instance)

# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_an_integer(7))
# print(Item.is_an_integer(7.0))
# print(Item.is_an_integer(7.5))


import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []

    def __init__(self, myname: str, myprice: float, myqty=0) -> None:
        # run validations on the receivced args
        assert myprice >= 0, f"Price {myprice} is not a positive integer."
        assert myqty >= 0, f"Quantity {myqty} is not a positive integer."

        # assign to instance attributes 
        self.name = myname
        self.price = myprice
        self.quantity = myqty

        # append to the all list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        csv_path = r"/mnt/crucial/data/Code/Repositories/interview_prep/interviewee/10_python_oops/items.csv"
        with open(csv_path, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                myname=item.get('name'),
                myprice=float(item.get('price')),
                myqty=int(item.get('quantity'))
            )

    @staticmethod
    def is_an_integer(num):
        if isinstance(num, float):
            # check for floats with 0 as decimal 
            # and treat them as int. Example: 7.0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

class Phone(Item):
    # all = []
    def __init__(self, myname: str, myprice: float, myqty=0, mybrknph=0) -> None:
        # call to super to access Item
        super().__init__(myname, myprice, myqty)
        # run validations on the receivced args
        assert mybrknph >= 0, f"Broken Phone Count {mybrknph} is not a positive integer."

        # assign to instance attributes 
        self.broken_ph = mybrknph

        # append to the all list
        # Phone.all.append(self)

phone1 = Phone("abcPhonev1", 500, 5, 2)
phone1.broken_phone = 2
phone2 = Phone("abcPhonev2", 700, 3, 1)
phone2.broken_phone = 1

print(Phone.all)
print(phone1.calculate_total_price())
print(phone2.calculate_total_price())
