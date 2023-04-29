import logo
print(logo.logo)
print('Welcome to the Secret Auction Program')
new='yes'
biddersData=[]
# def theSecretAuction(name,bid):
biggestBid=0
while new=='yes':
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
    biddersData.append(newData)
    for biggestBid in biddersData:
        if biddersData[bid]>biggestBid:
            biggestBid=biddersData[biggestBid]
        
# def theSecretAuction(name,bid):
#     while new=='yes':
#         name=input('Enter your name: ')
#         # bid=input('What is your bid?: ')
#         bid=int(input('What is your bid?: $'))
#         new=input('Is there any bidder? Type "yes" or "no" ').lower()
#         # if new=='yes':
#         #     name=input('Enter your name: ')
#         #     bid=int('What is your bid?: $')
#         newData={
#             'Name':name,
#             'Bid':'$'+str(bid)
#         }
#         biddersData.append(newData)

# name=input('Enter your name: ')
# bid=int(input('What is your bid?: $'))
# theSecretAuction(name,bid)
print(f'{name} is the winner with bid of &{bid}')


