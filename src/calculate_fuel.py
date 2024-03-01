def calculate_fuel(distance):
    # Type your code
    fuel = distance * 10

    if fuel < 100:
        fuel = 100
    return fuel if distance > 0 else 0