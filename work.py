y=int(input("birth year"))
age = 2019 - y
print(age) 

if age <= 18:
   print("minor")

elif age < 36:
   print("youth")

else:
   print("elder")  
