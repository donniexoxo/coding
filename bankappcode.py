def paycheckfilter(payrate, hours,  daysworked):
    checkingaccount = 0
    retirmentaccount = 0
    savingsaccount = 0

    payback = payrate * hours * daysworld

    savingsaccount += paycheck / 4
    retirementaccount += paycheck / 4
    checkingaccount += paycheck * .5

    

    print("my pay check for working" + str(daysworked)+ 'day(s) will be $' + str(paycheck))
    print("savings account blance: " + str(savingsaccount))
    print("retirementaccount account blance: " + str(retirementaccount))
    print("checking  account blance: " + str(checkingaccount))

paycheckfilter(30.00, 6, 4)