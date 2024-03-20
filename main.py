from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = float(input("Hey user. What is the bill amount: "))
bill_period =input("Ok. Then what is the period of the bill: ")
flatmate1_name = input("Thanks. What is the name of the first flatmate: ")
flatmate1_days = int(input(f"Ok. How long did {flatmate1_name} stayed in the house: "))
flatmate2_name = input("Alright. Now give the name the second flatmate: ")
flatmate2_days = int(input(f"And how long did {flatmate2_name} stayed in the house: "))
print("Thank you. I am processing the data you report will appear soon...")

bill = Bill(bill_amount, bill_period)
flatmate1 = Flatmate(flatmate1_name, flatmate1_days)
flatmate2 = Flatmate(flatmate2_name, flatmate2_days)

pdf = PdfReport(f"{bill_period}.pdf")
pdf.generate(flatmate1, flatmate2, bill)
