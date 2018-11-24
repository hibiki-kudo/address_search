import requests


class AddressSearcher:
    def search(self, postal_code):
        url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=" + postal_code
        response = requests.get(url).json()["results"][0]
        都道府県 = response['address1']
        市町村 = response['address2']
        町域 = response['address3']
        return f"{都道府県}{市町村}{町域}"
