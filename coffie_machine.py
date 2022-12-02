from data import MENU, resources

IsMachineOnline = True
import time
class CoffieMachine:
    
    def __init__(self, ismachineonline:IsMachineOnline):
        
        self.coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        self.running_status = ismachineonline
        if self.coffee_choice.lower() == 'off':
            print("Thank you for Visiting")
            self.running_status = False
            
        
    def report(self):
        """
        Shows all resources available inside coffee machine
        """
        # TODO 3: Print report.
        if self.coffee_choice.lower() == 'report':
            for i in resources:
                print(f"{i} : {resources[i]}")
            return True
    
    def coins(self):
        """
        takes coins from buyer and sum total its value
        """
        quarters = 0.25
        dimes = 0.10
        nickles = 0.05
        pennies = 0.01
        coin_list = ["quarters", "dimes", "nickles", "pennies"]
        buyer_coin = [int(input(f"How many {c}? ")) for c in coin_list]
        coin_value = [quarters, dimes, nickles, pennies]
        buyer_coin_value = [i*j for (i, j) in zip(buyer_coin, coin_value)]
        return sum(buyer_coin_value)
    
    def check_transaction(self, menu:MENU):
        """
        compares the actual cost of coffee to the sym total of buyer's coin
        """
        buyer_money = self.coins()
        resources["money"] = 0
        if buyer_money >= menu[self.coffee_choice]["cost"]:
            resources["money"] += menu[self.coffee_choice]["cost"]
            if buyer_money >= menu[self.coffee_choice]["cost"]:
                change = buyer_money - menu[self.coffee_choice]["cost"]
                print(f"Here is ${round(change, 2)} dollars in change")
                return True
        else:
            print("Sorry that's not enough money. Money refunded.") 

    
    def resource_deduct(self, menu:MENU):
        """
        deducts resources for particular coffee making from available resources
        """
        for supply1 in menu[self.coffee_choice]["ingredients"]:
            resources[supply1] -= menu[self.coffee_choice]["ingredients"][supply1]
    

while IsMachineOnline:
    coffiemachine = CoffieMachine(IsMachineOnline)
    if not coffiemachine.running_status:
        break
    if coffiemachine.report():
        continue

    for supply in MENU[coffiemachine.coffee_choice]["ingredients"]:
        if not MENU[coffiemachine.coffee_choice]["ingredients"][supply] < resources[supply]:
            print(f"Sorry, there is not enough {supply}. ")
            break
    
    else:
        if coffiemachine.check_transaction(menu=MENU):
            coffiemachine.resource_deduct(menu=MENU)
            print(f"Here is your {coffiemachine.coffee_choice}. Enjoy!")
            print("Resetting in 5 seconds...\n\n")
            time.sleep(5)