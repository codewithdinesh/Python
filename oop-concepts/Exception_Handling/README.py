
# 1
# class CreditCard:
#     def __init__(self, card_no, balance):
#         self.card_no = card_no
#         self.balance = balance


# class Customer:
#     def __init__(self, cards):
#         self.cards = cards

#     def purchase_item(self, price, card_no):
#         if price < 0:
#             raise Exception()
#         if card_no not in self.cards:
#             raise Exception()
#         if price > self.cards[card_no].balance:
#             raise Exception()


# card1 = CreditCard(101, 800)
# card2 = CreditCard(102, 2000)
# cards = {card1.card_no: card1, card2.card_no: card2}
# c = Customer(cards)
# while(True):
#     card_no = int(input("Please enter a card number"))
#     try:
#         c.purchase_item(1200, card_no)
#         break
#     except Exception as e:
#         print("Something went wrong. "+str(e))


# 2

class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance


class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception("Invalid Price")
        if card_no not in self.cards:
            raise Exception("Wrong card")
        if price > self.cards[card_no].balance:
            raise Exception("Wrong card")


card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = {card1.card_no: card1, card2.card_no: card2}
c = Customer(cards)
while(True):
    card_no = int(input("Please enter a card number"))
    try:
        c.purchase_item(1200, card_no)
        break
    except Exception as e:
        if str(e) == "Invalid Price":
            print("Product price is wrong")
            break
        if str(e) == "Wrong card":
            continue


# Extending Excpection class
class InvalidPrice(Exception):
    pass


class WrongCard(Exception):
    pass


class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance


class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise InvalidPrice("The price is wrong")
        if card_no not in self.cards:
            raise WrongCard("Card is invalid")
        if price > self.cards[card_no].balance:
            raise WrongCard("Card has insufficient balance")


card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = {card1.card_no: card1, card2.card_no: card2}
c = Customer(cards)
while(True):
    card_no = int(input("Please enter a card number"))
    try:
        c.purchase_item(1200, card_no)
        break
    except InvalidPrice as e:
        print(str(e))
        break
    except WrongCard as e:
        print(str(e))
        continue
    except Exception as e:
        print("Something went wrong. "+str(e))


# handling excpection in class
class InvalidUsername(Exception):
    def __init__(self, username):
        msg = 'The given given username '+username+' is invalid'
        super().__init__(msg)


try:
    username = '1abc'
    if not username[0].isalpha():
        raise InvalidUsername(username)
except InvalidUsername as e:
    print(e)

# The parent class except blocks must always come after the child class except block.


class InvalidPrice(Exception):
    pass


class WrongCard(Exception):
    pass


try:
    raise InvalidPrice()
except InvalidPrice:
    print("InvalidPrice")
except WrongCard:
    print("WrongCard")
except Exception as e:
    print("Exception")


# Custom exceptions are created by inheriting the Exception class

# Custom exception classes give greater flexibility in handling exceptions

# The parent class exception must come after the child class exceptions in the except clause
