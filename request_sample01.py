import requests


def requests_address(address: str):
    return requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=" + address)

if __name__ == "__main__":
    address = requests_address("0287111").json()

    print(address["results"][0]["address1"] + address["results"][0]["address2"] + address["results"][0]["address3"])
