print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
count= 0
flag=0
for i in name1:
  if i=='T' or i=='t':
    count = count+1
  if i=='R' or i=='r':
    count = count+1
  if i=='u' or i=='U':
    count = count+1
  if i=='e' or i=='E':
    count = count+1
for i in name2:
  if i=='T' or i=='t':
    count = count+1
  if i=='R' or i=='r':
    count = count+1
  if i=='u' or i=='U':
    count = count+1
  if i=='e' or i=='E':
    count = count+1
for j in name2:
  if j=='l' or j=='L':
    flag = flag+1
  if j=='o' or j=='O':
    flag = flag+1
  if j=='v' or j=='V':
    flag = flag+1
  if j=='e' or j=='E':
    flag = flag+1
for j in name1:
  if j=='l' or j=='L':
    flag = flag+1
  if j=='o' or j=='O':
    flag = flag+1
  if j=='v' or j=='V':
    flag = flag+1
  if j=='e' or j=='E':
    flag = flag+1
love_score1 = str(count)
love_score2 = str(flag)
love_score = love_score1+love_score2
int_love_score = int(love_score)
if 10>int_love_score or int_love_score>90:
  print("Your score is {}, you go together like coke and mentos.".format(int_love_score))
elif 40<int_love_score<50:
  print("Your score is {}, you are alright together.".format(int_love_score))
else:
  print("Your score is {}.".format(int_love_score))
