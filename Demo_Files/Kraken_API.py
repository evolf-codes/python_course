import requests

# url = 'https://api.kraken.com/0/public/AssetPairs'
# response = requests.get(
#     url,
#     headers={'Accept': 'application/json'},
#     params={'pair': 'XXBTZUSD,XETHXXBT',
#             'fees':'fee schedule'}
# )
#
# data = response.json()
# print(data)


#  1. Parse the order book snapshot in the REST API or the  WebSockets
#  API and ensure the top ask price is greater than the top bid  price.

list_of_currnecy_pairs=['XBTUSD','XBTEUR','XBTCAD','ETHUSD','ETHCAD']

for x in list_of_currnecy_pairs:

    url = 'https://api.kraken.com/0/public/Depth'
    response = requests.get(
        url,
        headers={'Accept': 'application/json'},
        params={'pair': x}
    )

    book_data = response.json()
    #print(book_data)
    currency_key = list(book_data['result'].keys())[0]

    asks = book_data['result'][currency_key]['asks'][0]
    a=(asks[0])

    bids = book_data['result'][currency_key]['bids'][0]
    b=(bids[0])

    if a > b:
        print(f"SUCCESS ======== {currency_key} ask: {a} > bid: {b}")
    else:
        print(f"ERROR ============= {currency_key} bid: {b} >= ask: {a}")
    #asks = book_data['result'][currency_key]

# 4. Parse various JSON messages used in the API responses and  check
# that the values have the correct data types.


url = 'https://api.kraken.com/0/public/Assets'
response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'asset': 'XBT'}
)


print(response.json())
data = response.json()

# check if the KEYS are OBJECTS
keys = list(data.keys())
for x in keys:
    if (isinstance(data[x],object)):
        print(f"{x} is on OBJECT")


# check if the KEYS inside the ASSET belong to the correct types

keys_result = list(data['result']['XXBT'])
print(keys_result)

for x in keys_result:
    print (type(data['result']['XXBT'][x]))