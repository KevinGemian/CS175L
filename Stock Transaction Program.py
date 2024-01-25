#Stocks
#Kevin Gemian
#CS 175L
cmsnratepurchase = float(input('Enter commission rate persentage on stock purchase: '))
cmsnratesale = float(input('Enter commission rate percentage on stock sale: '))
shares_purchased = float(input('Enter number of shares purchased: '))
shares_sold = float(input('Enter number of shares sold: '))
purchase_price = float(input('Enter Purchase price per share: '))
sell_price = float(input('Enter sell price per share: '))
print (f'Amount paid for the stock: ${purchase_price * shares_purchased:,.2f}')
purchase_cost = purchase_price * shares_purchased
print (f'Commission paid on the purchase: ${purchase_cost * cmsnratepurchase:,.2f}')
purchase_cmsn = purchase_cost * cmsnratepurchase
print (f'Amount the stock sold for: ${shares_sold * sell_price:,.2f}')
sale = shares_sold * sell_price
print (f'Commission paid on the sale: ${sale * cmsnratesale:,.2f}')
cmsnprofit = sale * cmsnratesale
print(f'Profit (or loss if negative): ${sale - purchase_cost - purchase_cmsn - cmsnprofit:,.2f}')
