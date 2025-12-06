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
