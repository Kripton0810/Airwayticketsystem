import datetime
rootName = "STS"
def makePnr():
    x = datetime.datetime.now()
    return rootName+x.strftime("%H%M%S%f")
'''
The price of your ticket consists of a number of things.
Base fare
Taxes and airport fees
Fuel surcharge
Service fee to issue
Food
Seat selection
Baggage
'''
def calculatePrice(dis,clas):
    if clas == 1:
        base = 2000
        airline_fule = 700
        cute = 50
        service = 239
        user_dev = 150
        if dis<500:
            base = 2000
        elif dis>=500 and dis<2000:
            base = 4000
        elif dis>=2000 and dis<4000:
            base = 7000
        else:
            base = dis*500
        amount = base + airline_fule + cute + service + user_dev 
        gst_calce = amount * 0.05
        total = gst_calce + 12 +amount
        return total
    elif clas == 2:
        base = 8000
        airline_fule = 2800
        cute = 200
        service = 700
        user_dev = 400
        if dis<500:
            base = 8000
        elif dis>=500 and dis<2000:
            base = 16000
        elif dis>=2000 and dis<4000:
            base = 30000
        else:
            base = dis*1500
        amount = base + airline_fule + cute + service + user_dev 
        gst_calce = amount * 0.12
        total = gst_calce + 100 +amount
        return total
    else:
        return -1
    




def main():
    print(makePnr())

if __name__ == '__main__':
    main()