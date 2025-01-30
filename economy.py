import random

def display_status(balance, inventory, market, loan, debt, investments, businesses):
    print("\nYour Balance: $", balance)
    print("Your Loan Debt: $", debt)
    print("Your Inventory:")
    for item, quantity in inventory.items():
        print(f"  {item}: {quantity}")
    print("\nMarket Prices:")
    for item, price in market.items():
        print(f"  {item}: ${price}")
    print("\nInvestments:")
    for country, amount in investments.items():
        print(f"  {country}: ${amount}")
    print("\nBusinesses:")
    for biz, profit in businesses.items():
        print(f"  {biz}: ${profit} daily profit")

def generate_market():
    return {
        "Gold": random.randint(50, 150),
        "Silver": random.randint(10, 50),
        "Oil": random.randint(30, 100),
        "Wheat": random.randint(5, 20),
    }

def main():
    balance = 1000 
    inventory = {"Gold": 0, "Silver": 0, "Oil": 0, "Wheat": 0}
    market = generate_market()
    debt = 0
    loan = False
    investments = {"USA": 0, "China": 0, "Germany": 0, "Japan": 0}
    businesses = {}
    
    while True:
        display_status(balance, inventory, market, loan, debt, investments, businesses)
        print("\nOptions: [B]uy, [S]ell, [N]ext Market Cycle, [L]oan, [P]ay Debt, [I]nvest, [T]ake Profit, [O]pen Business, [Q]uit")
        choice = input("Choose an action: ").strip().lower()
        
        if choice == 'b':
            item = input("What do you want to buy? ").strip().capitalize()
            if item in market:
                amount = int(input(f"How many units of {item} do you want to buy? "))
                cost = amount * market[item]
                if cost <= balance:
                    balance -= cost
                    inventory[item] += amount
                    print(f"You bought {amount} units of {item} for ${cost}.")
                else:
                    print("Not enough balance!")
            else:
                print("Invalid item!")
        
        elif choice == 's':
            item = input("What do you want to sell? ").strip().capitalize()
            if item in market:
                amount = int(input(f"How many units of {item} do you want to sell? "))
                if amount <= inventory[item]:
                    revenue = amount * market[item]
                    balance += revenue
                    inventory[item] -= amount
                    print(f"You sold {amount} units of {item} for ${revenue}.")
                else:
                    print("Not enough stock!")
            else:
                print("Invalid item!")
        
        elif choice == 'n':
            market = generate_market()
            print("Market prices updated!")
            for biz in businesses:
                balance += businesses[biz]
            print("Your businesses have generated income!")
        
        elif choice == 'l':
            if not loan:
                loan_amount = int(input("How much would you like to loan? ($100 - $1000): "))
                if 100 <= loan_amount <= 1000:
                    balance += loan_amount
                    debt += loan_amount * 1.1 
                    loan = True
                    print(f"You took a loan of ${loan_amount}. You need to repay ${debt}.")
                else:
                    print("Invalid loan amount!")
            else:
                print("You already have an outstanding loan!")
        
        elif choice == 'p':
            if debt > 0:
                if balance >= debt:
                    balance -= debt
                    debt = 0
                    loan = False
                    print("You fully repaid your loan!")
                else:
                    print("Not enough balance to repay the loan!")
            else:
                print("No outstanding debt!")
        
        elif choice == 'i':
            country = input("Which country do you want to invest in? (USA, China, Germany, Japan): ").strip().capitalize()
            if country in investments:
                amount = int(input(f"How much do you want to invest in {country}? "))
                if amount <= balance:
                    balance -= amount
                    investments[country] += amount
                    print(f"You invested ${amount} in {country}.")
                else:
                    print("Not enough balance!")
            else:
                print("Invalid country!")
        
        elif choice == 't':
            total_profit = sum(investments.values()) * 0.05  
            balance += total_profit
            print(f"You collected ${total_profit} from your investments!")
        
        elif choice == 'o':
            biz_name = input("Enter the name of your new business: ").strip()
            cost = random.randint(200, 500)
            if balance >= cost:
                balance -= cost
                businesses[biz_name] = random.randint(20, 100)
                print(f"You opened {biz_name}! It generates ${businesses[biz_name]} per market cycle.")
            else:
                print("Not enough balance to open a business!")
        
        elif choice == 'q':
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
