print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
if size=='S':
  total = 15
  if add_pepperoni=='Y':
    total = 15+2
elif size=='M':
  total = 20
  if add_pepperoni=='Y':
    total = 20+3
elif size=='L':
  total = 25
  if add_pepperoni=='Y':
    total = 25+3
else:
  print("enter correct details")
if extra_cheese=='Y':
  total = total+1
print("Your final bill is: ${}.".format(total))
