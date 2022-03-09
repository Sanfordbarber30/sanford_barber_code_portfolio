# Below is a variable labeled greeting along with the print geeting statement.
# User greeting
greeting = 'Good evening! \n\nWelcome, to Sanford\'s Tip Calculator, where I will be calculating your tip, adding your tax, and splitting your bill!\n\nDon\'t be afraid to have fun with the calculator!.'
print(greeting)

# User instructions
print('\nPlease, proceed by following the following instructions:')

# Variables for user input (meal amount, tip, tax)
meal = float(input('\nEnter you meal amount $'))
tip = int(input('\nTip % \n**ATTENTION**\nValue must be 0 or greater \nEnter your tip % :'))
tax = .1

# Tip + meal calculations converted into integer
tip_amount = int(meal * tip/100)
tax_amount = meal * tax
total = meal + tip_amount + tax_amount



print(f'\nYour meal was ${meal:.2f} and your tip was ${tip_amount}.')
print(f'Your total with a 10% tax is ${total:.2f}')
number_of_people_splitting = int(input('How many people will be splitting the bill? '))
total_split =  float(total / number_of_people_splitting)
print(f'The total for each person will be ${total_split:.2f}')

another_tip = input('Would you like to put another tip amount?')
#new_tip_amount = int(meal * another_tip/100)
#variable_1 = f'\nYour meal was ${meal:.2f} and your tip was ${new_tip_amount}. \nYour total with a 10% tax is ${total:.2f}'

#what_is_new_tip = int(input('\nEnter your tip % :'))

y = 'yes' 
n = 'no' 





     




while 'yes' in another_tip:
   
    print(f'\n{meal}')
    print(f'\n{tip}%')
    print(total)    
    break


     
if another_tip == y:
    print(meal)
    print(tip)
    print()
    #print(variable_1) 

elif another_tip == n:
    print('Have a good evening! \n Thank you, for using my Tip calculator!')
        
else:
    print(f'Invalid enter. {another_tip}')














# how_many_ways = int(input('How many ways'))
# total_split = food_final_price + tip_amount + tax_amount / 3
# print(total_split)


# tax_amount = food_final_price * tax
# total = food_final_price + tip_amount + tax_amount
# print(f'{total}')

#while tip < 0:
    #print('Please enter a valid entry!')
   # print(tip)
#except ValueError:
    #print('You did not enter a valid entry. \nPlease enter a valid entry!')

















