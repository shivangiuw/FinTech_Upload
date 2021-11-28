import csv
from pathlib import Path

# Part 1: Automating the Calculations for the loan portfolio summaries.

loan_costs = [500, 600, 200, 1000, 450]

#1. the total number of loans in the loan_costs list
number_of_loans = len(loan_costs)
print (f"The total number of loans is {number_of_loans}.")

#2. the total of all loans(loan_costs)
total_loan_costs = sum(loan_costs)
print (f"The total of all loans is ${total_loan_costs}.")

#3.Average loan price
average_loan_price = total_loan_costs / number_of_loans
print (f"The average loan price is ${average_loan_price}.")

# Part 2: Analysing the loan to determine the investment evaluation.

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
#@NOTE:
# **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
# **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

#1. Extracting and saving variables, **Future Value** and **Remaining Months** and printing them
future_value = loan.get("future_value")
print (f"Future value: ${future_value}")
remaining_months = loan.get("remaining_months")
print (f"Remaining months: {remaining_months}")

# 2. Calculation of Present value for fair value of the loan
# using formula: Present Value = Future Value / (1+ Annual_Discount_Rate/12)**Months
# Using return of 20% as the discount rate and extracted values above
discount_rate = 0.20
present_value = future_value / (1 + discount_rate/12)**remaining_months
print (f"Fair value of the loan using present value formula is ${present_value}")

#3. Analysing if loan is worth buying

loan_cost= loan.get("loan_price")

# If the present value of the loan is greater than or equal to the cost,
# printing a message- the loan is worth at least the cost to buy it.
if present_value >= loan_cost:
    print ("The loan is worth at least the cost to buy it.")
# Else, the present value of the loan is less than the loan cost,
# printing message - "the loan is too expensive and not worth the price.
else:
    print ("The loan is too expensive and not worth the price.")

#@NOTE:As, Present Value represents the loan's fair value at required minimum return of 20%,
# It makes sense to buy the loan at its current cost


# Part 3: Financial Calculations.

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000
}
# Defining a new function to calculate present value of loan
# function includes parameters for future_value`, `remaining_months`and the `annual_discount_rate`
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value_newloan = future_value / (1+annual_discount_rate/12)**remaining_months
    return present_value_newloan

#present value of new loan at an annual_discount_rate of 0.20
annual_discount_rate = 0.20
#calling the function for the new_loan
present_value_newloan = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The Present value of new loan is ${present_value_newloan}")

# Part 4: Conditionally filter lists of loans

#using a loop to iterate through the series of loans and select only the inexpensive loans.

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
# creating an empty list, inexpensive_loans
inexpensive_loans = []
# Using for loop to select each loan from the list of loans to determine loan_price
for loan in loans:
    loan_price = loan["loan_price"]
# using if-statement to determine if the loan_price in each loan from the list is less than or equal to 500
# If the loan_price is less than or equal to 500,adding that loan to `inexpensive_loans` list using append function
    if loan_price <= 500:
        inexpensive_loans.append(loan)
# Printing the list of inexpensive_loans
for inexpensive_loan in inexpensive_loans:
    print  (inexpensive_loan)

# Part 5: Saving the results.

#Output this list of inexpensive loans to a csv file

# Setting the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
#opening a new csv file in write mode
with open ('Inexpensive_Loans','w' , newline='') as csvfile:

#Using the csv library and `csv.writer` to write the header row 
    csvwriter = csv.writer(csvfile)
    # Writing header as first row
    csvwriter.writerow(header)
# writing each row of `loan.values()` from the `inexpensive_loans` list.
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

        # Set the output file path
output_path = Path("Inexpensive_Loans.csv")