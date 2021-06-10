from flask import Flask
from flask import request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

order = {}


def checkOrderID(orderId):
    return orderId in order


@app.route('/Order', methods=['POST'])
def receive_data():
    print("begin")

    form= request.get_json()
    Customer = form['Customer']
    Quantity = form['Quantity']
    soapType = form['Type']
    Fragrance = form['Fragrance']
    Color = form['Color']
    availablekey = False
    print("Goros")
    while availablekey == False:
        print("lolsito")
        OrderID = random.randrange(1000,9999,1)
        if checkOrderID(OrderID) == False:
            availablekey = True
    print("metalefs")
    print('Received order', Customer, Quantity, soapType, Fragrance, Color, OrderID)
    OrderCreated = {'Customer': Customer, 'Quantity': Quantity, 'soapType': soapType, 'Fragrance': Fragrance, 'Color': Color, 'OrderID': OrderID}
    order[OrderID] = OrderCreated
    print(order)
    return OrderCreated


app.run()