##Calculate area of a pentagon
##Print payroll statement

import math

radiusAsk = float(input("Enter the length from the center to a vertex: "))

sideLen =(2 * radiusAsk) * (math.sin(math.pi/5))
pentArea = ((3 * math.sqrt(3)) / 2) * (sideLen**2)

print(f"The area of the pentagon is {pentArea:.2f}")

print()

empName = input("Enter employee’s name: ")
workHours = float(input("Enter number of hours worked this week: "))
wage = float(input("Enter hourly pay rate: "))
fedTax = input("Enter federal tax withholding rate (%): ")
stateTax = input("Enter state tax withholding rate (%): ")

print()

grossPay = (wage * workHours)
hoursSentence = f"{workHours}"
paySentence = f"${wage:.2f}"
grossPaySentence = f"${grossPay:.2f}"

print(f"Weekly Pay Statement for {empName}")
print(f"Hours Worked: {hoursSentence:^12}")
print(f"Pay Rate: {paySentence:^18}")
print(f"Gross Pay: {grossPaySentence:^15}")

print("Deductions:")

fedTotal = grossPay * (float(fedTax)/100)
stateTotal = grossPay * (float(stateTax)/100)

fedSentence = f"Federal Withholding ({fedTax}%):"
stateSentence = f"State Withholding ({stateTax}%):"

fedEnding = f"${fedTotal:.2f}"
stateEnding = f"${stateTotal:.2f}"

netPay = (grossPay - (fedTotal + stateTotal))

print(f"  {fedSentence:<26}{fedEnding:>8}")
print(f"  {stateSentence:<26}{stateEnding:>8}")
print(f"Net Pay: ${netPay:.2f}")






