phoneshipmeny ={}


for x in range(10):
    print("1 make phone case")
    print("2 - solder motherboard and chips to case")
    print("3 - put screen on caseing")
    print("4 - check to confirm phone can turn on")
    if doesphonework != 'true':
        phone = 'this is phone number:' + str(x)
        print('this phone does not work')
        defectivephones.append(phones)

else:
    print("5 - place phone in shipment box")
    phone = "this is phone number:" + str(x)
    phoneshipment.append(phone)
    print(phoneshipment)