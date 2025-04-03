import streamlit as st

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

gunite_cost_per_cubic_yd = st.number_input("Enter gunite cost per cubic yard: ", value=50.0)
bench_cost_per_ft = st.number_input("Enter bench cost per ft: ", value=100.0)
tanning_ledge_cost_per_sqft = st.number_input("Enter tanning ledge cost per sq ft: ", value=80.0)
steps_cost_per_sqft = st.number_input("Enter steps cost per sq ft: ", value=90.0)

# Calculate and display results
if st.button("Calculate Costs"):
    bench_cost = calculate_bench_cost(bench_length, bench_cost_per_ft)
    tanning_ledge_cost = calculate_tanning_ledge_cost(tanning_ledge_area, tanning_ledge_cost_per_sqft)
    steps_cost = calculate_steps_cost(steps_area, steps_cost_per_sqft)
    gunite_volume = calculate_gunite_volume(pool_length, pool_width, depth1, depth2, depth3)
    gunite_cubic_yards = gunite_volume / 27

    if gunite_cost_per_cubic_yd != 0:
        gunite_total_cost = gunite_cubic_yards * gunite_cost_per_cubic_yd
    else:
        gunite_total_cost = 0
        st.warning("Gunite Cost per Cubic Yard is zero. Gunite total cost is 0.")

    st.write("## Calculation Results:")
    st.write(f"Bench Cost: ${bench_cost:,.2f}")
    st.write(f"Tanning Ledge Cost: ${tanning_ledge_cost:,.2f}")
    st.write(f"Steps Cost: ${steps_cost:,.2f}")
    st.write(f"Gunite Volume: {gunite_volume:,.2f} cubic feet ({gunite_cubic_yards:,.2f} cubic yards)")
    st.write(f"Total Gunite Cost: ${gunite_total_cost:,.2f}")
