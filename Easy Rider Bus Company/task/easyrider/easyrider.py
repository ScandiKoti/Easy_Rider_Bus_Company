import json


def main():
    input_data = json.loads(input())
    print("Arrival time test:")
    errors = []
    last_id = ''
    last_time = "00:00"
    output = ""
    for record in input_data:
        if not record["bus_id"] in errors and last_id == record["bus_id"] and last_time >= record["a_time"]:
            output += "bus_id line {}: wrong time on station {}\n".format(str(record["bus_id"]), record["stop_name"])
            errors.append(record["bus_id"])
        last_id = record["bus_id"]
        last_time = record["a_time"]
    print(output if output else "OK")


if __name__ == "__main__":
    main()
