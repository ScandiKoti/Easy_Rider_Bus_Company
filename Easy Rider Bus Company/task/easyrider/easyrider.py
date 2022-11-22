import json
import re


def main():
    check_dict = json.loads(input())
    err = {key: 0 for key in check_dict[0].keys()}
    for catalog in check_dict:
        for key, value in catalog.items():
            if key == 'stop_name':
                if not isinstance(value, str) or len(value) < 1:
                    err[key] += 1
                elif not re.search(r'([A-Z][a-z]+ )+(Street|Avenue|Boulevard|Road)$', str(value)):
                    err[key] += 1
            elif key == 'stop_type':
                if not isinstance(value, str) or len(value) > 1:
                    err[key] += 1
                elif not re.match('[SOF]?$', str(value)):
                    err[key] += 1
            elif key == 'a_time':
                if not isinstance(value, str) or len(value) < 5:
                    err[key] += 1
                elif not re.match(r'(2[0-3]|[01]\d):[0-5]\d$', str(value)):
                    err[key] += 1
    print(f'Format validation: {sum(err.values())} errors')
    for key, value in err.items():
        if key in ('stop_name', 'stop_type', 'a_time'):
            print(f'{key}: {value}')


if __name__ == "__main__":
    main()
