#Biggest, Smallest and Average
numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
print (6,1,915,-2,(7+6+23+8.18+18+8+7.2+85+915+12)/10)

iLikePesto = []
otherFoods = []

# Loop to ask 8 people about their favorite food
for i in range(8):
    food = input("What is your favorite food? ").strip()  
    if food.lower() == "pesto":
        iLikePesto.append(food)
    else:
        otherFoods.append(food)
n = len(iLikePesto)
print(f"Pesto is loved by {n} people!")
for _ in range(n):
    print("I like Pesto!")
print("Other Foods:")
for food in otherFoods:
    print(food.capitalize())

#List of (good) Cereals
Clist = []
A = False
while not A:
    Cereal = input("Enter cereal: ").strip().lower()
    if Cereal == "sultana and bran" or Cereal == "weetbix":
        A = True
    else:
        Clist.append(Cereal)
for cereal in Clist:
    print(cereal.capitalize())
