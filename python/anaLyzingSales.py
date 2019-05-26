# Name: Fentahun Reta
# Date: 11/24/15
# Working with Lists numbers and  writing functions that return a value.
#
# Discription: The program allows the user to enter a series of numbers, monthly sales amount for
#              for one division, and places the numbers in a list. It uses a sentinel-controlled
#              loop to get an input from the user and place each value entered into the list. when
#              a NEGATIVE value is entered, the loop stop.
#
def main():
    # creat an empty list to hold monthlty sales amount
    sales_list = []
    
    # Get the monthly sales from the user
    monthly_sales = float(input('Enter the amount of monthly sales: '))
    
    #create a variable to control the loop.
    while monthly_sales >=  0:

        # Append each amount of the sale to the monthly sale_list
        sales_list.append(monthly_sales)
        
        # update and allow the user to enter more monthly sales
        monthly_sales = float(input('Enter the amount of monthly sales: '))
        
        # As soon as any negative value is entered, stop the loop.
    print('\nThis is your monthly sale list\n')
    print(sales_list)
    print('\nThe new formatted monthly sale list is: ')
    print()
    print(string(sales_list), '}')
    
    # ask the user to enter the threshold amount of the sale. so, it decides
    # the value of the new list that is  greater than or equal to this value
    # (threshold).
    threshold = float(input('\nEnter the threshold amount: '))

    # out put
    #      It display the sale list entered by the user in one list, list 
    #      that contain value >= the tthreshold value maximum, minimum, 
    #      total and average value of the sale list.
    
    print('\nThe monthly sales list that are greater than or equal to the threshold value is: \n') 
    print(thresh(sales_list,threshold))
    print('\nThe maximum value using "built-in max" for monthly sales is:', max(sales_list ))
    print('\nThe maximum value using the "loop" for monthly sales is:',max2(sales_list ))
    print('\nThe minimum value using "built-in min" for monthly sales is:',min(sales_list ))
    print('\nThe minimum  value using the "loop" for monthly sales: is',min2(sales_list ))
    print('\nThe total value for monthly sales:',sum(sales_list ))
    print('\nThe average value for monthly sales is: ' + format(average(sales_list ), '.2f') +'\n')
     
    
   
    # function definition that uses a loop and a string accumulator    
def string(sales_list):
    string_accumul ='{$'+ format(sales_list[0], '.2f')
    for i in range (len(sales_list)):
        #string_accumul +='$' + str(sales_list[i]) + ', '
        #string_accumul.append(format(str(sales_list[i])), '.2f')
        
        string_accumul +=', '+'$' +format(sales_list[i], '.2f') 
         
    return string_accumul
#
# function that evaluate the maximum value of the monthly sales using a loop 
def max2(sales_list):
    max2 = sales_list[0]
    for i in range(len(sales_list)):
        if sales_list[i] > max2:
            max2 = sales_list[i]
    return max2  # return maximum value

# function that evaluate the minimum value of the monthly sales  
def min2(sales_list):
    min2 = sales_list[0]
    for x in range(len(sales_list)):
        if sales_list[x] < min2:
            min2 = sales_list[x]
    return min2  # return minimum value
#
# function that evaluate the total amount of the monthly sales 
def sum(sales_list):
    total = 0
    for y in sales_list:
        total += y
    return total   # return total sales
#
# function that evaluate the average amount of the monthly sales 
def average(sales_list):
    average = sum(sales_list)/(len(sales_list))
    return average    # return average value of the sales
#
# A function that takes a list and the threshold as parameters, and returns a
# new list that contains all values in the original list that are greater than
# or equal to the threshold 

def thresh(sales_list ,threshold):
    new_threshold = []
    for z in sales_list:
      if z >= threshold:
          new_threshold.append(z)
    new_threshold.sort()  # sort the sale value 
    return new_threshold  # return values >= threshold value
    
        
main()
##########################################################################################
# Test case
# values entered by the user
#
# Enter the amount of monthly sales: 12.95
# Enter the amount of monthly sales: 1234.56
# Enter the amount of monthly sales: 100.00
# Enter the amount of monthly sales: 20.50
# Enter the amount of monthly sales: -2
###################################################################
#The out put generated immedately when negative number entered is 
#
# This is your monthly sale list
# [12.95, 1234.56, 100.0, 20.5]
#
#
# The new formatted monthly sale list is: 

# {$12.95, $1234.56, $100.00, $20.50 }
# 
# Enter the threshold amount: 12.95
#
# The monthly sales list that are greater than or equal to the threshold value is: 
# [12.95, 20.5, 100.0, 1234.56]
#
#
# The maximum value using "built-in max" for monthly sales is:  1234.56
# The maximum value using the "loop" for monthly sales is:  1234.56
# The minimum value using "built-in min" for monthly sales is:  12.95
# The minimum  value using the "loop" for monthly sales: is  12.95
# The total value for monthly sales: 1368.01
# The average value for monthly sales is: 342.00
