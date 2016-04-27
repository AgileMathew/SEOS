import csv

def process_orders(orders):
    d = {}
    for data in orders:
        if not d.has_key(data[1]):
           d[data[1]] = {'Buy': 0, 'Sell': 0}
        if data[0] == 'Buy':
           d[data[1]]['Buy'] += int(data[2])
        else:
           d[data[1]]['Sell'] += int(data[2])
    return d
           
def compare_orders(data, orders):
    result = []
    for i, order in enumerate(orders):
        action = order[0]
        value = int(order[2])
        company = order[1]
        total = 0
        if action == 'Buy':
            total = data[company]['Sell']
            action = "Sell"
        else:
            total = data[company]['Buy']
            action = "Buy"
        status = ""
        if total >= value:
           total = total - value
           value = 0
           status = "Closed"
        else:
           value = value - total
           total = 0 
           status = "Open"
        data[company][action] = total
        line  = map(str, [i+1, order[0], company, order[2], value, status])  
        result.append(','.join(line)) 
    return result

# reading data csv and process data
def stock_handler():           
    with open('input.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        header = ""
        orders = []
        for row in spamreader:
            #print row
            if not header:
               header = ','.join(row) + "\n"
            else:
               orders.append(row[1:])
            print ', '.join(row)
        data = process_orders(orders)
        result = compare_orders(data, orders)
        print header + '\n'.join(result)
        with open('out.txt', 'w') as f:
          f.write(header)
          f.write('\n'.join(result))

if __name__ == "__main__":
    stock_handler()
   
