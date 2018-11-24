import requests


class AddressSearcher:
    def __init__(self):
        self.base_url = "http://zipcloud.ibsnet.co.jp/api/search?"

    def search(self, postal_code):
        url = self.base_url + "zipcode=" + postal_code
        if requests.get(url).json()["results"] != None:
            response = requests.get(url).json()["results"][0]
            都道府県 = response['address1']
            市町村 = response['address2']
            町域 = response['address3']
            return f"{都道府県}{市町村}{町域}"

        return "該当するデータは見つかりませんでした"
