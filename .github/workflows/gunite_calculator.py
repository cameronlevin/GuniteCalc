import streamlit as st

def calculate_bench_cost(length):
    # Assume a fixed cost per foot for benches (you can adjust this)
    cost_per_ft = 100.0
    return length * cost_per_ft

def calculate_tanning_ledge_cost(area):
    # Assume a fixed cost per square foot for tanning ledges (you can adjust this)
    cost_per_sqft = 80.0
    return area * cost_per_sqft

def calculate_steps_cost(area):
    # Assume a fixed cost per square foot for steps (you can adjust this)
    cost_per_sqft = 90.0
    return area * cost_per_sqft

def calculate_gunite_volume(length, width, depth1, depth2, depth3, waste_factor=1.15):
    avg_depth = (depth1 + depth2 + depth3) / 3
    volume_ft = length * width * avg_depth
    return volume_ft * waste_factor

def calculate_gunite_total_cost(gunite_cubic_yards):
    #Assume a fixed cost per cubic yard of gunite.
    gunite_cost_per_cubic_yd = 50.0
    return gunite_cubic_yards * gunite_cost_per_cubic_yd

st.title("Gunite Pool Calculator")

# User inputs using Streamlit widgets
pool_length = st.number_input("Enter pool length (ft): ", value=20.0)
pool_width = st.number_input("Enter pool width (ft): ", value=10.0)
depth1 = st.number_input("Enter shallow depth (ft): ", value=3.0)
depth2 = st.number_input("Enter middle depth (ft): ", value=5.0)
depth3 = st.number_input("Enter deep depth (ft): ", value=8.0)

bench_length = st.number_input("Enter total bench length (ft): ", value=5.0)
tanning_ledge_area = st.number_input("Enter tanning ledge area (sq ft): ", value=20.0)
steps_area = st.number_input("Enter steps area (sq ft): ", value=10.0)

# Calculate and display results
if st.button("Calculate Costs"):
    bench_cost = calculate_bench_cost(bench_length)
    tanning_ledge_cost = calculate_tanning_ledge_cost(tanning_ledge_area)
    steps_cost = calculate_steps_cost(steps_area)
    gunite_volume = calculate_gunite_volume(pool_length, pool_width, depth1, depth2, depth3)
    gunite_cubic_yards = gunite_volume / 27
    gunite_total_cost = calculate_gunite_total_cost(gunite_cubic_yards)

    st.write("## Calculation Results:")
    st.write(f"Bench Cost: ${bench_cost:,.2f}")
    st.write(f"Tanning Ledge Cost: ${tanning_ledge_cost:,.2f}")
    st.write(f"Steps Cost: ${steps_cost:,.2f}")
    st.write(f"Gunite Volume: {gunite_volume:,.2f} cubic feet ({gunite_cubic_yards:,.2f} cubic yards)")
    st.write(f"Total Gunite Cost: ${gunite_total_cost:,.2f}")
