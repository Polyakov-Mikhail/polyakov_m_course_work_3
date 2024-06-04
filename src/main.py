from functions import data_json, date_formatting_operation, hide_and_split


def main():
    last_five_operations = data_json("../operations.json")
    for operation in last_five_operations:
        # print(operation)
        print(f"{date_formatting_operation(operation['date'])} {operation['description']}")
        if 'from' in operation:
            print(f"{hide_and_split(operation['from'])} -> {hide_and_split(operation['to'])}")
            print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
        else:
            print(f"{hide_and_split(operation['to'])}")
            print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")


if __name__ == "__main__":
    main()
