#entered instructions for how to use tip calculator.
print('\nEnter Numbers below to decide how to split a restaurant bill amoung friends.')


#created variables for inputs asking user to enter numbers.
total_bill = float(input('What is the total bill?: '))
percentage_tip = int(input('What % tip would you like to give?: '))
number_of_people = int(input('How many people are splitting the bill?: '))


#this is how and where the math formulas calculated the results.
tax = .10
taxed_bill = (total_bill * tax) + total_bill
gratuity = taxed_bill * (percentage_tip /100)
grand_total = taxed_bill + gratuity 
each_diner_pays = grand_total / number_of_people


#Final print statement showing tip calculation and thanking diners for using,
print(f'\nThank you for using our simple Tip calculator\nThe grand total is ${grand_total:,.2f}\nEach member of the party is responsible for paying ${each_diner_pays:,.2f}.')

