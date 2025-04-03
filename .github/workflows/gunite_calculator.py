def calculate_bench_cost(length, cost_per_ft):
    return length * cost_per_ft

def calculate_tanning_ledge_cost(area, cost_per_sqft):
    return area * cost_per_sqft

def calculate_steps_cost(area, cost_per_sqft):
    return area * cost_per_sqft

def calculate_gunite_volume(length, width, depth1, depth2, depth3, waste_factor=1.15):
    avg_depth = (depth1 + depth2 + depth3) / 3
    volume_ft = length * width * avg_depth
    return volume_ft * waste_factor

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:  # Ensure non-negative values
                return value
            else:
                print("Input must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print("Welcome to the Gunite Pool Calculator!")

pool_length = get_float_input("Enter pool length (ft): ")
pool_width = get_float_input("Enter pool width (ft): ")
depth1 = get_float_input("Enter shallow depth (ft): ")
depth2 = get_float_input("Enter middle depth (ft): ")
depth3 = get_float_input("Enter deep depth (ft): ")

bench_length = get_float_input("Enter total bench length (ft): ")
tanning_ledge_area = get_float_input("Enter tanning ledge area (sq ft): ")
steps_area = get_float_input("Enter steps area (sq ft): ")

gunite_cost_per_cubic_yd = get_float_input("Enter gunite cost per cubic yard: ")
bench_cost_per_ft = get_float_input("Enter bench cost per ft: ")
tanning_ledge_cost_per_sqft = get_float_input("Enter tanning ledge cost per sq ft: ")
steps_cost_per_sqft = get_float_input("Enter steps cost per sq ft: ")

gunite_volume = calculate_gunite_volume(pool_length, pool_width, depth1, depth2, depth3)
gunite_cubic_yards = gunite_volume / 27

if gunite_cost_per_cubic_yd != 0:
    gunite_total_cost = gunite_cubic_yards * gunite_cost_per_cubic_yd
else:
    gunite_total_cost = 0
    print("Gunite Cost per Cubic Yard is zero. Gunite total cost is 0.")

bench_cost = calculate_bench_cost(bench_length, bench_cost_per_ft)
tanning_ledge_cost = calculate_tanning_ledge_cost(tanning_ledge_area, tanning_ledge_cost_per_sqft)
steps_cost = calculate_steps_cost(steps_area, steps_cost_per_sqft)

print("\nCalculation Results:")
print(f"Bench Cost: ${bench_cost:,.2f}")
print(f"Tanning Ledge Cost: ${tanning_ledge_cost:,.2f}")
print(f"Steps Cost: ${steps_cost:,.2f}")
print(f"Gunite Volume: {gunite_volume:,.2f} cubic feet ({gunite_cubic_yards:,.2f} cubic yards)")
print(f"Total Gunite Cost: ${gunite_total_cost:,.2f}")
