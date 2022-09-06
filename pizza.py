print("welcome to technio pizza shop")
size = input("what size pizza you want? S,M,L")
add_peperoni = input("do you want pepperoni ? Y or N")
extra_chesse = input("do you want extra cheese? Y or N ")
bill = 0
if size == "S":
 bill += 15
elif size == "M":
 bill += 20
elif size == "L":
 bill += 25
else:
 bill += 25
 if add_peperoni == "Y":
  if  size == "s":
   bill += 3
   if extra_chesse == "Y":
    bill += 1
print(f"your're final bILL is {bill}")
k=input("press close to exit") 
