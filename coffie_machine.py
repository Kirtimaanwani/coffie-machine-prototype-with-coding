from data import MENU, resources
# TODO 1:Prompt user by asking “ What would you like? (espresso/latte/cappuccino)"
while True:

    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2:Turn off the Coffee Machine by entering “ off ” to the prompt.
    if coffee_choice.lower() == 'off':
        break

    def report():
        """
        Shows all resources available inside coffee machine
        """
        # TODO 3: Print report.
        if coffee_choice.lower() == 'report':
            for i in resources:
                print(f"{i} : {resources[i]}")
            return True


# TODO 5:Process coins. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01


    def coins():
        """
        takes coins from buyer and sum total its value
        """
        quarters = 0.25
        dimes = 0.10
        nickles = 0.05
        pennies = 0.01
        coin_list = ["quarters", "dimes", "nickles", "pennies"]
        buyer_coin = [int(input(f"How many {c}? ")) for c in coin_list]
        coin_list1 = [quarters, dimes, nickles, pennies]
        buyer_coin_value = [i*j for (i, j) in zip(buyer_coin, coin_list1)]
        return sum(buyer_coin_value)

# TODO 6:Check transaction successful? “ Sorry that's not enough money. Money refunded. ”. profit “report” is triggered.

    # TODO 7: give change if any remaining.“Here is $2.45 dollars in change.”

    def check_transaction():
        """
        compares the actual cost of coffee to the sym total of buyer's coin
        """
        buyer_money = coins()
        resources["money"] = 0
        if buyer_money >= MENU[coffee_choice]["cost"]:
            resources["money"] += MENU[coffee_choice]["cost"]
            if buyer_money >= MENU[coffee_choice]["cost"]:
                change = buyer_money - MENU[coffee_choice]["cost"]
                print(f"Here is ${round(change, 2)} dollars in change")
                return True
        else:
            print("Sorry that's not enough money. Money refunded.")


    # TODO 8: make coffee, resources should be deducted as per type of coffee ordered


    def resource_deduct():
        """
        deducts resources for particular coffee making from available resources
        """
        for supply1 in MENU[coffee_choice]["ingredients"]:
            resources[supply1] -= MENU[coffee_choice]["ingredients"][supply1]

    # TODO 9:“Here is your latte. Enjoy!”
    if report() is True:
        continue

    # TODO 4: Check resources sufficient? “ Sorry there is not enough water. ”

    for supply in MENU[coffee_choice]["ingredients"]:
        if not MENU[coffee_choice]["ingredients"][supply] < resources[supply]:
            print(f"Sorry, there is not enough {supply}. ")
            break
    else:
        if check_transaction() is True:
            resource_deduct()
            print(f"Here is your {coffee_choice}. Enjoy!")
