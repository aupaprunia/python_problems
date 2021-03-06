# A pizza shop offers n pizzas along with m toppings. A customer plans to spend around x coins. The customer should order exactly one pizza, and may order zero, one or two toppings. Each topping may be order only once.
#
# Given the lists of prices of available pizzas and toppings, what is the price closest to x of possible orders? Here, a price said closer to x when the difference from x is the smaller. Note the customer is allowed to make an order that costs more than x.
#
# Example 1:
#
# Input: pizzas = [800, 850, 900], toppings = [100, 150], x = 1000
# Output: 1000
# Explanation:
# The customer can spend exactly 1000 coins (two possible orders).
# Example 2:
#
# Input: pizzas = [850, 900], toppings = [200, 250], x = 1000
# Output: 1050
# Explanation:
# The customer may make an order more expensive than 1000 coins.
# Example 3:
#
# Input: pizzas = [1100, 900], toppings = [200], x = 1000
# Output: 900
# Explanation:
# The customer should prefer 900 (lower) over 1100 (higher).
# Example 4:
#
# Input: pizzas = [800, 800, 800, 800], toppings = [100], x = 1000
# Output: 900
# Explanation:
# The customer may not order 2 same toppings to make it 1000.
# Constraints:
#
# Customer's budget: 1 <= x <= 10000
# Number of pizzas: 1 <= n <= 10
# Number of toppings: 0 <= m <= 10
# Price of each pizza: 1 <= pizzas[i] <= 10000
# Price of each topping: 1 <= toppings[i] <= 10000
# The total price of all toppings does not exceed 10000.

def closest(pizzas, toppings, x):
    toppings.append(0)
    close = abs((pizzas[0] + toppings[0]) - x)
    result = pizzas[0] + toppings[0]
    for pizza in pizzas:
        for top in toppings:
            value = abs((pizza + top) - x)
            if value < close:
                result = pizza + top
                close = value
            elif value == close:
                result = min(pizza + top, result)
    print(result)


pizzas = [1100, 900]
toppings = [200]
x = 1000
closest(pizzas, toppings, x)