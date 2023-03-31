print("Meal Calculator:")
child = float(input( "What is the price of a child's meal? $"))
adult = float(input( "What is the price of an adult's meal? $"))
children = int(input( "How many children are there? "))
adult_there = int(input( "How many adults are there? "))
tax = float(input( "What is the sales tax rate? "))
print(" ")

Subtotal = child * children + adult * adult_there
tax_rate = tax / 100
total = tax_rate * Subtotal
total_total = total + Subtotal
print("Subtotal: $" + str(Subtotal))
print("Sales tax: $" + str(total))
print("Total: $" + str(total_total))
print(" ")
amount = float(input("What is the payment amount? $"))
change = amount - total_total
print("Change: $" + str(round(change,2)))
print(" ")
print("Thanks for visiting our Restaurant. We hope to see you again!")
