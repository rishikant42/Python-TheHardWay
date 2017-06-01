import csv
from sys import argv

def main():
    fileName = argv[1]
    openFile = open(fileName)

    id_product_price = {}

    given_products = argv[2:]

    readFile = csv.reader(openFile)

    for row in readFile:
        id = int(row[0])
        shopids = id_product_price.keys()
        if id in shopids:
            id_product_price[id].append((row[1:]))
        else:
            id_product_price[id] = [row[1:]]

    shop_ids = id_product_price.keys()

    total_cost_with_shopid = []

    for id in shop_ids:
        items = id_product_price[id]
        price = [float(item[0]) for item in items]
        avilable_products = [item[1:] for item in items]
        all_avilable_products = [val for sublist in avilable_products for val in sublist]
        if set(given_products).issubset(set(all_avilable_products)):
            cost = 0
            i = 0
            for p in given_products:
                try:
                    cost += price[all_avilable_products.index(p)]
                except IndexError:
                    #"Need to work here"
                    if i == 0:
                        cost += 6.0
                        i = 1
                    else:
                        cost += 0
            total_cost_with_shopid.append((cost, id))

    total_cost_with_shopid.sort()

    if total_cost_with_shopid:
        shopid = total_cost_with_shopid[0][0]
        cost = total_cost_with_shopid[0][1]
        return "%r, %r" %(cost, shopid)
    else:
        return None

if len(argv) < 3:
    print "Pass csv file & products list"
else:
    print main()


################# TESTS #########################
#################################################


# $ python2 code.py data.csv teddy_bear baby_powder
# 2, 11.5
# 
# $ python2 code.py data.csv pampers_diapers baby_soap
# None
# 
# $ python2 code.py data.csv scissor bath_towel
# 6, 11.0
# 
# $ python2 code.py data.csv scissor powder_puff cotton_balls
# 6, 11.0
