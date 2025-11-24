name=("amala","gayathri","tarun","sachi","ebran")
count=sum(name.lower().count('a') for name in name)
print(f"Total occurance of 'a':{count}")
