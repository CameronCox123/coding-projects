nameAsk = input("What is your name? ")
print(f"Hello {nameAsk}! You have just delved into Python.")

print()

celciusAsk = int(input("Enter a temperature in degrees Celsius: "))
cFConversion = celciusAsk * 1.8 + 32
print(f"{celciusAsk} Celsius is {cFConversion} Fahrenheit")

print()

bill, gratuityRate = eval(input("Enter the bill and gratuity rate: "))
gratuity = (round((bill * (gratuityRate/100)), 2))
total = bill + gratuity
print(f"The gratuity is ${gratuity} and the total is ${total}")
      
print()

numberAsk = int(input("Enter a number between 0 and 999: "))

firstNum = numberAsk%10
secondNum = int(numberAsk/10)%10
thirdNum = int(numberAsk/100)

print(f"The sum of the digits is {firstNum + secondNum + thirdNum}")

print()

principleAsk = int(input("Enter your investment amount ($): "))
timeAsk = int(input("Enter your investment length (years): "))

finalAmount = principleAsk * (1 + 0.07) ** timeAsk
print(f"After {timeAsk} years, you will have ${finalAmount:.2f}")

print()

ageAsk = int(input("Enter your age: "))

harBtRng = (220 - ageAsk)
print(f"Your target heart rate is {0.5 * harBtRng:.0f} - {0.85 * harBtRng:.0f} bpm")
