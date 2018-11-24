from address_searcher import AddressSearcher


def main():
    input_postal_code = input("郵便番号(7ケタ)？: ")
    location_name = AddressSearcher()
    print(location_name.search(input_postal_code))


if __name__ == "__main__":
    main()
