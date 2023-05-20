
    name=input('Enter your name: ')
    # bid=input('What is your bid?: ')
    bid=int(input('What is your bid?: $'))
    new=input('Is there any bidder? Type "yes" or "no" ').lower()
    # if new=='yes':
    #     name=input('Enter your name: ')
    #     bid=int('What is your bid?: $')
    newData={
        'Name':name,
        'Bid':'$'+str(bid)
    }
    biddersData.a