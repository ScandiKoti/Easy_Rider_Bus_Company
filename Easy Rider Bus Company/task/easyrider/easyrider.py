import json
from collections import Counter


def main():
    bus_id_counter = Counter([value for el in json.loads(input()) for key, value in el.items() if key == 'bus_id'])
    print('Line names and number of stops:')
    print('\n'.join(f'bus_id: {key}, stops: {value}' for key, value in bus_id_counter.items()))


if __name__ == "__main__":
    main()
