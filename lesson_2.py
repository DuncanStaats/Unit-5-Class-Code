"""
Name: Duncan Staats
Date: 11/8/24
Topic: Functions
"""

def main(name, color = "Yellow"):
    print(f"{name} the fierce, {color} eyed warrior.")

main("john")
main("Ed", "Brown")

def blackjack(a, b, c):
    valid_numbers = 1<=a<11 and 1<=b<11 and 1<=c<11
    if not valid_numbers:
        print("Error")
        return
    sum = a + b + c
    if sum <= 21:
        print(sum)

    elif sum >= 21 and (a ==11 or b ==11 or c ==11):
        print(sum - 10)

    elif sum >= 21:
        print("Bust")


blackjack(2, 5, 8)
blackjack(5, 12, 8)
blackjack(10, 10, 3)
blackjack(11, 10, 2)
