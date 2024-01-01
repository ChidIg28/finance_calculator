import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount of you'll have to pay on a home loan")
print()
calculation = input("Do you want to calculate an investment or a bond? ").lower() #lower function to allow any entries of the word that are upper and lower case
if calculation == "bond":
# All variables to account for the entries by the user to conduct the calculation
  house = int(input("How much is value of the house? "))
  interest = int(input("What is the annual interest rate? "))
  months = int(input("How many months over should the bond be repaid? "))
  bond_calculation = ((interest/100/12)*house)/(1-(1+(interest/100/12))**(-months)) # calculation
  print("You will have to repay £{} each month".format(bond_calculation)) # format method to insert answer to the calculation
elif calculation == "investment": # elif statement to allow users to conduct investment calculation also
  interest_calculation = input("Do you want to calculate simple or compound interest? ").lower()
elif interest_calculation == "compound": # elif statement to allow users to conduct compound interest calculation
# All variables to account for the entries by the user to conduct the calculation
  deposit = int(input("How much are you depositing? "))
  rate = int(input("How much is the interest rate? "))
  time = int(input("How many years are you investing? "))
  compound_calc = deposit * math.pow((1+(rate/100)),time)
  print("The amount after the interest would be £{}".format(compound_calc))
elif interest_calculation == "simple": # elif statement to allow users to conduct simple interest calculation
  deposit = int(input("How much are you depositing? "))
  rate = int(input("How much is the interest rate? "))
  time = int(input("How many years are you investing? "))
  simple_calc = deposit *(1 + (rate/100)*time)
  print("The amount after the interest would be £{}".format(simple_calc))


