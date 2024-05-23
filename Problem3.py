import requests

class Payload:
    def __init__(self, symbol, price, time_stamp) -> None:
        self.symbol = symbol
        self.price = price
        self.time_stamp = time_stamp

    def sendPayLoad(self):
        response = requests.post('https://mock-node-wgqbnxruha-as.a.run.app/broadcast', json={
            "symbol":self.symbol,
            "price":self.price,
            "timestamp":self.time_stamp
        })
        return response.json()
    
    def getPayLoad(self):
        hash = self.sendPayLoad()["tx_hash"]
        response = requests.get(f"https://mock-node-wgqbnxruha-as.a.run.app/check/{hash}")
        return response.json()

payload1 = Payload("ETH", 4500, 1678912345)
print(Payload("ETH", 4500, 1678912345).sendPayLoad())
print(Payload("ETH", 4500, 1678912345).getPayLoad())

"""
Document

Class Payload require
* 1. Symbol
* 2. Price
* 3. Time Stamp

First step to use all the feature of this class is you have to create your payload first by

Payload(symbol, price, time stamp)

after that inorder to "POST" the payload we will use


"""