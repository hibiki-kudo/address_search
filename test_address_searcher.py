import unittest

from address_searcher import AddressSearcher


class TestAddressSearcher(unittest.TestCase):
    def test_岩手県八幡平市大更の地名を郵便番号から取得できる(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="0287111")
        self.assertEqual("岩手県八幡平市大更", actual)

    def test_東京都練馬区豊玉南の地名を郵便番号から取得できる(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="1760014")
        self.assertEqual("東京都練馬区豊玉南", actual)

    def test_あえて郵便番号が存在しないものを入力して該当するデータは見つかりませんでしたと返すようにする(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="9999999")
        self.assertEqual("該当するデータは見つかりませんでした", actual)

if __name__ == "__main__":
    unittest.main()
