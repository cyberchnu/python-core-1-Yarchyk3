def calculate_fuel(distance):
    # Розрахунок обсягу палива
    fuel = distance * 10
    # Перевірка, щоб обсяг палива був не менше 100
    if fuel < 100:
        fuel = 100
    return fuel if distance > 0 else 0