
# Name: Fentahun Reta
# Date: 10/29/15
# Assigment 4------Retirment planning, part1
#
# Description: The program demonstrates how a customer to plan for retirement, and.
#              show the finanal balance after some years using a range of function
#              with a for loop.
#
# the amount_saved is the amount of money saved in each year, 
# interest_rate is in percentage, and starting_age is the intitial 
# age of the person who want to start saving. 
#


def calc_final_balance (starting_age, annual_saving, interest_rate):
    
    initial_age = starting_age  # Age of person to start saving
    balance = 0                 # initial balance was zero when the person plan to save.
    for initial_age in range(starting_age, 70):
         
        balance += annual_saving  # balance in every year is the original balance plus
                                 # amount_saved on that year.
                                    
        balance += balance*interest_rate/100    # it is the balance in the account
                                                  # after each years.
                                                                              
    return balance  # The function return the value referenced by the balance variable
                    # that causes the function to end and send the value back to the program.        
#
# After the loop finishes, display the final calculated balance
def show_table():
    print('Well come to the retirment planning tool!')
    print('Retirment savings Table:')
    annual_saving = int(input('Enter savings (at least $100):'))
    while annual_saving < 100:
        print('Annual saving should be greater than or equal to 100.')
    print('Enter valid saving!')
    print('\nStarting'          '\t'           ' Assumed interest rate')
    print('Age     \t4%        \t6%      \t8%       10%')  
#
    for intitial_age in range (20, 70, 5):
        print(intitial_age, end=' ')
        for interest_rate in range (4,12,2):
            print('    $'+ format(calc_final_balance(intitial_age,annual_saving,interest_rate), '10.2f' ), end=' ')
        print()
    print('\nWhen are YOU going to start saving for retirement?')

show_table()
