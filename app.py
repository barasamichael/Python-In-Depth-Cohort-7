"""
Accounts
- open
- freeze
- unfreeze
- close

Withdrawing
- overdraft
- cancel a withdrawal

Saving
- earn interest
- set a target
- request withdrawal
- lock savings for a certain period

Deposit
Loans


Accounts
- customer name
- email address
- phone number
- balance
- type of account (Current, Ordinary, Savings)
"""
welcome_message = """
+-----------------------------------------------+
|            WELCOME TO UMOJA BANK              |
+-----------------------------------------------+
| 1. Open an account                            |
| 2. Freeze account                             |
| 3. Unfreeze account                           |
| 4. Close account                              |
| 5. Withdraw                                   |
| 6. Cancel withdrawal                          |
| 7. Deposit                                    |
| 8. Request a loan                             |
| 9. Grant a loan                               |
| 10. Make installment                          |
| 0. Exit                                      |
+-----------------------------------------------+
"""
# Display welcome message
print(welcome_message)

# Display choices
choice = int(input("Select an option from the main menu (0 - 10): "))

if choice == 1:
    print("OPEN AN ACCOUNT")
    
    # Prompt for number of accounts
    number_of_accounts = int(
        input("How many accounts do you want to open? ")
    )
    
    for i in range(number_of_accounts):
        # Keeping track of which record we are adding
        print(f"Account #{i + 1}")
        
        # Prompting the user for account details
        account_type = input("Enter type of account (Current/Ordinary/Savings): ")
        name = input("Enter you name: ")
        id_number = int(input("Enter ID number: "))
        email_address = input("Enter email address: ")
        residential_area = input("Enter area of residence: ")
        
        # Displaying account details
        print(f"Account Type: {account_type}")
        print(f"Name: {name}")
        print(f"ID Number: {id_number}")
        print(f"Residential Area: {residential_area}\n")
        
    print("We are done adding accounts")

elif choice == 2:
    account_status = input("Enter account status (Frozen/Unfrozen): ")
    if account_status.upper() == "FROZEN":
        print("Your account is already frozen")
        
    elif account_status.upper() == "UNFROZEN":
        print("Account frozen successfuly")
        
    else:
        print(f"You entered the wrong account status '{account_status}'")

elif choice == 3:
    account_status = input("Enter account status (Frozen/Unfrozen): ")
    if account_status.upper() == "UNFROZEN":
        print("Your account is not frozen")
        
    elif account_status.upper() == "FROZEN":
        print("Account unfrozen successful. Welcome back")
        
    else:
        print(f"You entered the wrong account status '{account_status}'")


elif choice == 4:
    is_closed = False
    if is_closed:
        print("Account is already closed")
        
    else:
        confirm = input("Enter 'Yes' to confirm: ")
        if confirm.lower() == 'yes' or confirm.lower().startswith('y'):
            print("Account closed successfully")
            
        else:
            print("Account closure cancelled")

elif choice == 5:
    account_balance = int(input("Enter account balance: "))
    amount_to_withdraw = int(input("Enter amount to withdraw: "))
    
    # Amount to withdraw must not be more than account balance
    if amount_to_withdraw > account_balance:
        print("Insufficient funds")
    
    else:
        print("Withdrawal successful")
        print(f"Current balance: Ksh. {account_balance - amount_to_withdraw}")

elif choice == 6:
    account_balance = int(input("Enter account balance: "))
    amount_to_withdraw = int(input("Enter amount to withdraw: "))
    
    # Amount to withdraw must not be more than account balance
    if amount_to_withdraw > account_balance:
        print("Insufficient funds")
    
    else:
        confirm = input("Enter 'cancel' to cancel: ")
        if confirm.lower() == 'cancel' or confirm.lower().startswith('c'):
            print(f"Withdrawal cancel. Current balance is {account_balance}")
            
        else:
            account_balance -= amount_to_withdraw
            print("Withdrawal successful")
            print(f"Current balance: Ksh. {account_balance}")        
    
elif choice == 7:
    account_balance = int(input("Enter account balance: "))
    amount_to_deposit = int(input("Enter amount to deposit: "))
    
    if amount_to_deposit <= 0:
        print(
            f"You cannot deposit Ksh. {amount_to_deposit} since it is " 
              + "less than 1 shilling"
        )
        
    else:
        account_balance += amount_to_deposit
        print(f"Deposit successful. Current balance is Ksh. {account_balance}")
    

elif choice == 8:
    pass

elif choice == 9:
    """
    Criteria for eligibility
    
    1. Must be employed for more than 2 years
    2. Must have a salary at least 1/4 of the amount being loaned
    3. Must have made a total transaction greater or equal to the amount being 
        loaned
    4. Must not be in CRB
    5. Must not have an existing loan with the bank
    """
    # Prompt for amount to loan
    amount_requested = int(input("How much money was requested? "))
    
    # Prompt for eligibility criteria
    is_employed = input("Is the loanee employed (Yes/No): ")
    employment_period = int(input("If yes how long? "))
    salary = int(
        input("How much do they earn? ")
    )
    total_annual_transaction = int(
        input("How much have they transacted in the last one year? ")
    )
    is_in_crb = input("Is the loanee under CRB? (Yes/No) ")
    has_existing_loan = input("Do they have an existing loan? (Yes/No) ")
    
    if (
        is_employed 
        and (employment_period >= 2) 
        and (salary >= amount_requested * 0.25) 
        and (is_in_crb.lower() == "no")
        and (total_annual_transaction >= amount_requested)
        and (has_existing_loan.lower() == "no")
        ):
        print(
            f"Your loan request for Ksh. {amount_requested} has been granted " 
              + "successfully."
        )
        
    else:
        print(
            f"Sorry. You request for a Ksh. {amount_requested} loan has " 
            + "been denied."
        )

elif choice == 10:
    pass

elif choice == 0:
    print("Goodbye! We are exiting the program...")
    exit()
    
else:
    print("You made an invalid option")