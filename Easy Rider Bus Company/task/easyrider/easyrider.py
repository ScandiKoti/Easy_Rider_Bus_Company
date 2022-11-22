import json


def main():
    check_dict = json.loads(input())
    bus_id_dict = dict()
    for catalog in check_dict:
        if catalog['bus_id'] not in bus_id_dict:
            bus_id_dict[catalog['bus_id']] = 0
        bus_id_dict[catalog['bus_id']] += 1
    print('Line names and number of stops:')
    for key, value in bus_id_dict.items():
        print(f'bus_id: {key}, stops: {value}')


if __name__ == "__main__":
    main()
