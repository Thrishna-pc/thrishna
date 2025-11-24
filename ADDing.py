text=input("enter the string:")
if text[-3:] =="ing":
    text +="ly"
else:
    text +="ing"
print("Modified string:",text)
