# Mario Quiroz
#Lab 3 Programming Recap
# October 31 2021

#Question 1 
print("Question 1")
print('Enter the principal amount:')
Princ_Amount = float (input () )
print("Enter the rate of interest:")
Int_Rate = float(input())
Year1 = 1
Year2 = 2
Year3 = 3
Simp_Int1 = (Princ_Amount*Year1*Int_Rate)/100
Simp_Int2 = (Princ_Amount*Year2*Int_Rate)/100
Simp_Int3 = (Princ_Amount*Year3*Int_Rate)/100
print("The Simple Interest in year 1 is:",Simp_Int1)
print("The Simple Interest in year 2 is:", Simp_Int2)
print("The Simple Interest in year 3 is:", Simp_Int3)
Quart_Payment = Simp_Int1 / 4 
print("The Quarterly Payment would be :", Quart_Payment)
print(" ")

#Question 2
print("Question 2")
print("Please enter the amount of quarter:")
Quarter = int(input())
print("Please enter the amount of dimes:")
Dimes = int(input())
print("Please enter the amount of nickles")
Nickles = int(input())
print("Please enter the amount of pennies")
Pennies = int(input())
Total_Sum = 0.25 * Quarter + 0.1 * Dimes + 0.05 * Nickles + .01 * Pennies
print("Your total change is $ ",Total_Sum)

#Question 3 
pi = 3.14
print("Question 3")
print("Please enter the radius of the pizza inch:")
Radius_Pizza = float(input())
print("Please enter the cost per square inch of pizza in dollars:")
Cost_of_Pizza = float(input())
Area = pi + Radius_Pizza + Radius_Pizza
print("The area of pizza in square inch is:", Area)
Price_6 = Area * Cost_of_Pizza / 6.0
print("The price of a slice cut in 6 slices is :",Price_6)
Price_8 = Area * Cost_of_Pizza / 8.0
print("The price of a slice cut in 8 slices is:", Price_8)
print(" ")

#Question 4 
print("Question 4")
Cost_of_Coffee = 10.50
Shipping_Per_pound = 0.86
Fixed = 1.50
print("Enter the amount of pounds of coffee you desire")
Coffee=float(input())

Total= (Cost_of_Coffee + Shipping_Per_pound ) * Coffee + Fixed
print("The total price will be", Total)

#Question 5
print("Question 5")
print("Enter the cover price of a book")
Book_Price = float(input())
print("Enter the number of books you want ")
Copies =int(input())
Shipping = 3.00
Price_per_copy = 0.75
discount = .10 * (Copies * Book_Price) 
Total_Price = (Copies * Book_Price) - discount
Total_Shipping = Shipping +((Copies-1) * Price_per_copy )
Total_Outcome = Total_Shipping + Total_Price
print("Your total outcome will be ", Total_Outcome)


#Question 6 
print("Question 6")
print("Enter a number from 1-86400")
Num = int(input())

seconds = Num % 60
minutes = Num / 60
hours = minutes / 60
minutes = minutes % 60 
print("Total converted time is ", hours +"Hours", minutes + "Minutes" , seconds + "Seconds")




