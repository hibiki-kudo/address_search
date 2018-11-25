import requests


class AddressSearcher:
    def __init__(self):
        self.base_url = "http://zipcloud.ibsnet.co.jp/api/search?"

    def search(self, postal_code):
        url = self.base_url + "zipcode=" + postal_code
        # if requests.get(url).json()["results"] is not None:
        try:
            response = self.request(url)
            location = response['address1'] + response['address2'] + response['address3']
            return f"{location}"

        except TypeError:
            return "該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。"

        except:
            return "予期せぬエラーが発生しました。管理者に問い合わせてくだい。"

    def request(self, url):
        return requests.get(url).json()["results"][0]
