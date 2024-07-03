from cardHolder import cardHolder

def print_menu():
    # Print Options
    print("PLease choose anyone of the following...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would u like to deposit:")) 
        cardHolder.set_balance(cardHolder.get_balance()+deposit)
        print("Thank you for $$. Your new balance is : ",str(cardHolder.get_balance()))
    except:
        print("Invalid input")   

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw : "))
        ## checking enough money present or not 
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient Balance:(")
        else:
            cardHolder.set_balance(cardHolder.get_balance()-withdraw)
            print("You have sufficient Balance! You can go for it :)")
    except:
        print("Invalid input")


def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ =="__main__":
    current_user = cardHolder("","","","","")

    ## Create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("56790233456789",2345,"Abhishek","Gandipadala",30000.40))
    list_of_cardHolders.append(cardHolder("23345678956743",1236,"Hadassah","Gandipadala",3000.00))
    list_of_cardHolders.append(cardHolder("89765432670923",7896,"Bhaskara Rao","Gandipadala",400000.80))
    list_of_cardHolders.append(cardHolder("78653421986764",5679,"Rebecca","Gandipadala",200000.70))


    #Prompt user 
    debitCardNum = ""
    while True:
        try: 
            debitCardNum = input("Please insert your Card Number : ")
            #check in repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                 print("Card number not recognized . Please try again.")    
        except:
            print("Card number not recognized . Please try again.")  

    ## Prompt for pin
    while True:
        try:
            userPin = int(input("PLease Enter your Pin:").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("Invalid PIN. Please try again.")

    ## Print Options
    print("Welcome ", current_user.get_firstname(), " :)")
    option = 0
    while (True):
        print_menu()
        try:
            option = int(input())
        except: 
            print("Invalid input. Please try Again")

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0

print("Thank You Have a Great Day")