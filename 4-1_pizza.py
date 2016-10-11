#!/bin/python3
pizzas = ["meat", "cheese", "mushroom"]

def pizza(x):
    for i in x:
        print(i)
        print("I like " + i + " pizza")

pizza(pizzas)

print("I like " + pizzas[0] + ", " +  pizzas[2] + ", and " + pizzas[1] + " pizza")
