meal = float(input('Enter you meal amount'))
tip = int(input('Enter your tip %:'))
tax = .1

food = '\nChicken & Waffles' '\nShrimp & Grits' '\nFried Chicken with Mac n Cheese ' '\nand' '\nHamburger with Smoked Beacon and Frence Fries'
cw = 'Chicken & Waffles'
sg = 'Shrimp & Grits'
cmc = 'Fried Chicken with Mac n Cheese '
hf = 'Hamburger with Smoked Beacon and Frence Fries'

cw_price = 25
sg_price = 25
cmc_price = 25
hf_price = 25



# calcs
tip_amount = int(meal * tip/100)
tax_amount = meal * tax
total = meal + tip_amount + tax_amount
total_split = meal + tip_amount + tax_amount / 3

print(f'\nYour meal was ${meal:.2f} and your tip was ${tip_amount}.')
print(f'Your total with tax is ${total:.2f}')

# Greet guest and welcome them to restaurant.( Used a string)
greeting = 'Good evening! \n\nWelcome to Mr.Barber restaurant.\nMy name is Terrance and I will be your server this evening.'
print(greeting)

# Ask guest would they like to start off with a drink.
drinks = '\nPepsi \nSprite \nRootbeer \nCrush \nand \nWater'
# split_drinks = drinks.split(',')
#print(split_drinks) # this will convert the single string to a list of strings
#for drink in drinks:
    #print(drink)

pep = 'pepsi' 
spr = 'sprite' 
root = 'rootbeer'
cru = 'crush'  
water = 'water' 


pep_price = 2
spr_price = 2
root_price = 2
cru_price =  2
water_price =  2



drink_menu = f'on our menu we have: {drinks} \nAll of our drinks are $2 that includes water.'
extra_time = 'I will give you a few more moments.'
drink_ready = input('\nCan I start you off with some drinks?')

y = 'yes'  
n = 'no' 

if drink_ready == y:
    print(f'Tonight {drink_menu}') 

elif  drink_ready == n:
    print(extra_time)
    print(input(f'Are you ready to order now?'))
    print(drink_menu)
        
else:
    print('I can only take a yes or no answers')

drink_input = input('What would you like to drink?')


if drink_input == (pep):
    print('I will have that for you in a few moents')
elif drink_input == spr:
    print('okay')
elif drink_input == root:
    print('No problem')
elif drink_input == cru:
    print('I will have that for you in a few moents')
elif drink_input == water:
    print('Sure')
else:
    print('We dont have that on the menu' )




food_menu = f'\nTonight we are serving: \n{food}'
order = input('\nAre you ready to order dinner yet?\n\n')

if order == y:
    print(food_menu) 
elif order == n:
    print(extra_time)
    print(order)
    if order == y:
            print(food_menu)
    else:
            print('I can only take a yes or no answers')    
#elif drink_ready == n:
    #print(ready)    
else:
    print('I can only take a yes or no answers')


food_order = input(f'\nWhat would you like to order? (To sucessfully place order, please follow the following instructions)\nFor: Chicken & Waffles type= cw \nFor: Shrimp & Grits type= sg \nFor: Fried Chicken with Mac n Cheese type= cmc  \nand \nFor: Hamburger with Smoked Beacon and Frence Fries type= hf\n Please, enter your order.')

print('\nGive us about thirty minutes and your food will be up')

how_was_food = input('How was the food good?')
g= 'good'
ok= 'okay'
bad= 'bad'
nas = 'nasty'
horr= 'horrible'
if how_was_food == g :
    print('Im glad that you enjoyed it')
elif how_was_food == ok:
    print('I will let the chef know, that the food was not cooked to perfection')
elif how_was_food == bad:
    print('I will have your food remaid')
elif how_was_food == horr :
    print('I will give you a free desert, and I want to apologize on behalf to the chef and all the staff.')
else :
    print('Please, let me know how the meal was')
    print(how_was_food)


print('Im going to sit the bill right here. \nThe total reflect all three drinks and all three meals. \nEach meal is $25 a piece and the drinks are $2')

soda_total= float(pep_price * 3)  
meal_toal = float(cw_price * 3)
food_final_price = soda_total + meal_toal
print(f'{food_final_price} \nNOT INCLUDING TAXES')


tip = int(input('Enter your tip %:'))

tip_amount = int(food_final_price * tip/100)
print(f'${tip_amount} is the total amount including the tip.')


bill_split = input('Will you be spltting the bill? ')
how_many_ways = int(input('How many ways'))
total_split = food_final_price + tip_amount + tax_amount / 3
print(total_split)


tax_amount = food_final_price * tax
total = food_final_price + tip_amount + tax_amount
print(f'{total}')






bill_split = input('Will you be spltting the bill? ')
how_many_ways = int(input('How many ways'))
total_split = meal + tip_amount + tax_amount / 3
print(total_split)

# tip_amount = int(meal * tip/100)
# tax_amount = meal * tax
# total = meal + tip_amount + tax_amount
# total_split = meal + tip_amount + tax_amount / 3




#print(bill_split)

#####\nAll of our meals are $25 with a .7% sales tax###
#elif drink_ready == n:
    #print(ready)

#drink_ready_answer = drink_ready('Yes')
#print(f'What would you like to drink?')

#drink_menu = f'On our menu we have{drinks}'
#extra_time = 'I will give you a few more moments.'



# drink_ready_answer =

# drink_menu = f'On our menu we have{drinks}'
# drink_order = 'What would you like to drink?'



# Read drink menu to guest
# Ask guest if they are ready to order
# Read guest food menu
# Take guest order
# Let guest know how long it will take to bring food
# Print out total bill (including tip)
# After a tip has been calculated, your program should ask the user if they would like to enter another tip, and run again if the answer is yes. (convert integer into float)
# Ask guest if they will be splitting the bill
# Bill is be divided amongst 3 people
# Print out amout to be paid when split into 3
# # Thank guest for coming
# ## The Tip Calculator

