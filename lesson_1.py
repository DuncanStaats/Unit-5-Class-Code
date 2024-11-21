"""
Name: Duncan Staats
Date: 11/6/24
Topic: Functions
"""


def main():
    # all of your code goes in here
    print("Hello!")


if __name__ == "__main__":
    main()

def rainy():
    print("On a rainy day, galoshes are appropriate footwear.")

def sunny():
    print("On a sunny day, sandals are appropriate footwear.")

def snowy():
    print("On a snowy day, boots are appropriate footwear.")

weather = input("What is the weather? (sunny, rainy, snowy): ")

if weather == "rainy":
    rainy()
elif weather == "sunny":
    sunny()
elif weather == "snowy":
    snowy()


def calculate_area(side_length=10):
    area = side_length ** 2
    print(f"The area of a square with sides of length {side_length} is {area}.")

