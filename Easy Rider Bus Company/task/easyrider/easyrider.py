import json


def main():
    check_dict = json.loads(input())
    err = {key: 0 for key in check_dict[0].keys()}
    for catalog in check_dict:
        for key, value in catalog.items():
            if key in ('bus_id', 'stop_id', 'next_stop'):
                if not isinstance(value, int):
                    err[key] += 1
            elif key in ('stop_name', 'a_time'):
                if not isinstance(value, str) or len(value) < 1:
                    err[key] += 1
            elif key == 'stop_type':
                if not isinstance(value, str) or len(value) > 1:
                    err[key] += 1
                elif isinstance(value, str) and value not in 'SOF':
                    err[key] += 1
    print(f'Type and required field validation: {sum(err.values())} errors')
    for key, value in err.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    main()