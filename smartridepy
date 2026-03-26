import random
def calculate_taxi_fare(distance_km, vehicle_type, waiting_fee_per_min,   waiting_time_minutes, round_trip=False):
    
    vehicle_data = {
        "HATCHBACK": {"base": 50, "per_km": 14, "speed": 40, "capacity": 4},
        "SEDAN": {"base": 80, "per_km": 17, "speed": 50, "capacity": 4},
        "SUV": {"base": 120, "per_km": 21, "speed": 45, "capacity": 6},
        "PREMIUM SEDAN": {"base": 200, "per_km": 38, "speed": 60, "capacity": 4}
    }

    vehicle_type = vehicle_type.upper()
    if vehicle_type not in vehicle_data:
        vehicle_type = "HATCHBACK"

    data = vehicle_data[vehicle_type]
    total_distance = distance_km * 2 if round_trip else distance_km
    traffic_multiplier = random.uniform(0.9, 1.4)
    travel_time = (total_distance / data["speed"]) * 60 * traffic_multiplier
    fare = data["base"] + (data["per_km"] * total_distance)
    waiting_cost = waiting_fee_per_min * waiting_time_minutes
    total_cost = fare + waiting_cost
    return total_cost, travel_time, data["capacity"]


def suggest_best_option(distance_km, passengers, priority):
    vehicle_list = ["HATCHBACK", "SEDAN", "SUV", "PREMIUM SEDAN"]
    results = []
    for vehicle in vehicle_list:
        fare, time, capacity = calculate_taxi_fare(
            distance_km, vehicle, 2, 5
        )
        if passengers > capacity:
            continue

        results.append({
            "vehicle": vehicle,
            "fare": fare,
            "time": time
        })

    if not results:
        return None, []
    if priority == "cost":
        best_choice = min(results, key=lambda x: x["fare"])
    else:
        best_choice = min(results, key=lambda x: x["time"])
    return best_choice, results
def main():
    print("\n # Smart Taxi Recommendation System\n")
    try:
        distance = float(input("Enter distance (km): "))
        passengers = int(input("Enter number of passengers: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    print("\nChoose preference:")
    print("1. Lowest Cost")
    print("2. Fastest Time")
    option = input("Enter choice: ").strip()
    priority = "cost" if option == "1" else "time"
    best, options = suggest_best_option(distance, passengers, priority)

    if not options:
        print("No suitable vehicle available for given passengers.")
        return
    print("\nAvailable Options:")
    for opt in options:
        print(f"{opt['vehicle']} → ₹{opt['fare']:.2f}, {opt['time']:.1f} mins")
    print("\nRecommended Choice:")
    print(f"{best['vehicle']} → ₹{best['fare']:.2f}, {best['time']:.1f} mins")
if __name__ == "__main__":
    main()
