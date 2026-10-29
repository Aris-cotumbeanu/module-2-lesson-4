amount = int(input("Enter withdrawal amount: "))

if amount <= 0 or amount % 100 !=0:
    print("please enter a amount in hundreds! ")
else:
    notes = [500,200,100]

    for note in notes:
        count = 0
        while amount>=note:
            amount = amount - note
            count = count + 1
        if count > 0:
            print(note, "notes:", count)
    print(" please collect your cash!")