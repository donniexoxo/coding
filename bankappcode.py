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

#paycheckfilter(30.00, 6, 4)





def ridesharecalculator(miles, surgeprice, discount):
    base_fare = 3.00
    surge_fare =3.75
    cost_per_mile = 2.00


    total = base_fare + miles * cost_per_mile


    if surgeprice == true:
        print("the final price for this ride is $" + str(base_fare + surgerpricing (miles* cost_per_mile)))

    else:
        print("the final price for this ride is $" + str(base_fare + surgerpricing (miles* cost_per_mile)))

    if disccount == true:
         discountprice = total * total* .15
         print("the final price for this ride is $" + str(base_fare + surgerpricing (miles* cost_per_mile)))
    else:
        print("the final price for this ride is $" + str(base_fare + surgerpricing (miles* cost_per_mile)))





    
ridesharecalculator(3, false,false)