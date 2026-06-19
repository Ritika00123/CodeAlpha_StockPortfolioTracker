stocks={'AAPL':180,'TSLA':250,'GOOG':150}
total=0
while True:
    name=input("Stock name (or 'done'): ").upper()
    if name=='DONE':
        break
    qty=int(input('Quantity: '))
    if name in stocks:
        total += stocks[name]*qty
print('Total Investment Value:', total)
