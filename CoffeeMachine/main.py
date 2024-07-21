from modules import MENU, resources

choice = input("\nWhat would you like? (Espresso, Latte, Cappuccino or Report): ").lower()


def my_ingredients(flavor=choice):
    ingredients = MENU[flavor]["ingredients"]
    return ingredients


def my_cost(flavor=choice):
    cost = MENU[flavor]["cost"]
    return cost


def machine_capacity():
    capacity = resources
    return capacity


can_get_coffee = True
while can_get_coffee:
    remaining_capacity = machine_capacity()

    if choice == "report":
        print(f"\n *** Available Resources *** \n\t\tWater: {remaining_capacity['water']} \n\t\tMilk: "
              f"{remaining_capacity['milk']} \n\t\tCoffee: {remaining_capacity['coffee']}")
        break
    elif choice == "off":
        print("Machine shutting down. Goodbye!")
        break

    print(f"{choice.title()} will cost you ${'{:.2f}'.format(my_cost(choice))}. Please pay using coins.\n")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    sum_of_coins = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)

    water_milk_coffee = my_ingredients(choice)
    item_cost = my_cost(choice)

    if choice == "latte" or choice == "cappuccino":
        if water_milk_coffee["milk"] > remaining_capacity["milk"]:
            print("\nSorry there is not enough milk. Bye!")
            break
    if water_milk_coffee["water"] > remaining_capacity["water"]:
        print("\nSorry there is not enough water. Bye!")
        break
    elif water_milk_coffee["coffee"] > remaining_capacity["coffee"]:
        print("\nSorry there is not enough coffee. Bye!")
        break
    else:
        if item_cost <= sum_of_coins:
            change = sum_of_coins - item_cost
            print(f"\nHere is ${'{:.2f}'.format(change)} in change.")
            print(f"Enjoy your cup of {choice} ☕️. Cheerio!")
        elif sum_of_coins < item_cost:
            amount_short = item_cost - sum_of_coins
            print(f"\nSorry, you're short of ${f'{amount_short:.2f}'} of coins. "
                  f"An amount of ${f'{sum_of_coins:.2f}'} has been refunded.")
            break

    for key in remaining_capacity.keys():
        if choice == "latte" or choice == "cappuccino":
            remaining_capacity[key] = remaining_capacity[key] - water_milk_coffee[key]
        else:
            remaining_capacity["water"] = remaining_capacity["water"] - water_milk_coffee["water"]
            remaining_capacity["coffee"] = remaining_capacity["coffee"] - water_milk_coffee["coffee"]

    choice = input("\nWhat would you like? (Espresso, Latte or Cappuccino): ").lower()
