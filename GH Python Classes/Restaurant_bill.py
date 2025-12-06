# Bill without input

totalGuests = float(5)
totalBill = float(120)
tips_percent = float(22)
billForEachGuest = totalBill/totalGuests
tip_Amount = (tips_percent/100)*totalBill
billForEachGuestwTips = billForEachGuest + tip_Amount
print(billForEachGuest, " is a total bill before tips per each guest")
print(tip_Amount, " is a tip amount")
print(billForEachGuestwTips, " is a bill with tips")

#Bill with input

totalGuests2 = int(input("Enter total number of guests "))
totalBill2 = int (input("Now add total bill "))
tip_Percent = int(input("finally, add tip % "))
TipAmount = (tip_Percent/100)*totalBill2
billForEachGuestwTips2 = totalBill2/totalGuests2 + TipAmount
print(TipAmount, " is a total tip amount")
print(billForEachGuestwTips2, " and its a total bill w tips")

