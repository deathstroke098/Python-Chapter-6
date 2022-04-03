text = input("Enter the text\n")

if("screw you" in text):
    spam = True
elif("fuck you" in text):
    spam = True
elif("damn you" in text):
    spam = True
elif("lick this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam moron")
else:
    print("This text is not fucking spam")