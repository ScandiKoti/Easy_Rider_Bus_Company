import json


def main():
    input_data = json.loads(input())
    for bus_id in set(rec['bus_id'] for rec in input_data):
        if sum(rec['stop_type'] == 'S' for rec in input_data if rec['bus_id'] == bus_id) != 1 \
                or sum(rec['stop_type'] == 'F' for rec in input_data if rec['bus_id'] == bus_id) != 1:
            print(f'There is no start or end stop for the line: {bus_id}')
            exit()

    start_stops = set(rec['stop_name'] for rec in input_data if rec['stop_type'] == 'S')
    print(f'Start stops: {len(start_stops)} {sorted(list(start_stops))}')

    transfer_stops = set(trans['stop_name'] for trans in input_data if sum(rec['stop_name'] == trans['stop_name'] for rec in input_data) > 1)
    print(f'Transfer stops: {len(transfer_stops)} {sorted(list(transfer_stops))}')

    finish_stops = set(rec['stop_name'] for rec in input_data if rec['stop_type'] == 'F')
    print(f'Finish stops: {len(finish_stops)} {sorted(list(finish_stops))}')


if __name__ == "__main__":
    main()
