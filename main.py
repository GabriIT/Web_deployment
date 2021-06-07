from flat import Bill, Flatmate
from reports import PdFReport, FileSharer

amount = float(input("Hi, pls enter the bill amount: "))
print("this is the amount", amount)

period = input("pls enter the period, e.g. October 2021")
print("this is the period", period)

name1 = input("What is your name ? ")
days_in_house1 = float(input(f"Pls input a integer, How many days {name1} stay in the house during the bill period ? "))

name2 = input("What is the name of the other flatmate ? ")
days_in_house2 = float(input(f"Pls input a integer, How many days {name2} stay in the house during the bill period ? "))

the_bill = Bill(period,amount)
flatmate1 = Flatmate(days_in_house1, name1)
flatmate2 = Flatmate(days_in_house2, name2)

print(f"{name1} pays ", flatmate1.pays(the_bill, flatmate2),f"{name2} pays ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdFReport(filename=f"{the_bill.period}.pdf" )
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())



















