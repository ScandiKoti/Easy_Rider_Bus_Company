import json


def main():
    input_data = json.loads(input())
    start_stops = set(record['stop_name'] for record in input_data if record['stop_type'] == 'S')
    transfer_stops = set(i['stop_name'] for i in input_data if sum(record['stop_name'] == i['stop_name'] for record
                                                                   in input_data) > 1)
    finish_stops = set(record['stop_name'] for record in input_data if record['stop_type'] == 'F')
    union_stops = start_stops | transfer_stops | finish_stops
    error_stops = set(record['stop_name'] for record in input_data if record['stop_type'] == 'O' and record['stop_name']
                      in union_stops)
    print('On demand stops test:')
    print(f'Wrong stop type: {list(sorted(error_stops)) if error_stops else "OK"}')


if __name__ == "__main__":
    main()
