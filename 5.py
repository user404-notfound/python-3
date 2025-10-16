from pprint import pprint

def build_car_list():
    car_list = []

    try:
        # Read car models and mileage from input.txt
        cars_data = []
        with open("C:\\Users\\Administrator\\Desktop\\input1.txt", newline='') as f:
            
            for line in f:
                parts = line.strip().split()
                if len(parts) < 2:
                    continue
                model = parts[0]
                miles_str = parts[1]
                try:
                    miles = int(miles_str)
                    cars_data.append({'model': model, 'miles': miles})
                except ValueError:
                    # skip invalid mileage
                    continue

        # Read car IDs from car-ids.txt
        car_ids = []
        with open("C:\\Users\\Administrator\\Desktop\\car-ids.txt", newline='') as f:

            for line in f:
                line = line.strip()
                if line.isdigit():
                    car_ids.append(int(line))

        # Combine IDs with car data
        for cid, car in zip(car_ids, cars_data):
            car_list.append({'id': cid, 'miles': car['miles'], 'model': car['model']})

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
        return []

    return car_list


# Usage
def ex5():
    car_list = build_car_list()
    pprint(car_list)


# Run
ex5()
