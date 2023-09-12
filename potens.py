bas_str = input("Skriv potens bas: ") 
bas=int(bas_str)

exp_str = input("Skriv exponenten: ") 
exp=int(exp_str)

potens=1

for x in range(0, exp):
    potens = potens * bas

print(f"Potensens värde är: {potens}")





