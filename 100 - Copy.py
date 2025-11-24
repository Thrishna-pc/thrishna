num=input("enter integer:")
display=num.split()
for i in range(len (display)):
     if int(display[i])>100:
        display[i]="over"
print(display)
