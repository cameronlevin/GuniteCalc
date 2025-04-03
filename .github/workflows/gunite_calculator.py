import streamlit as st

def calculate_gunite_volume(length, width, depth1, depth2, depth3, bench_length, tanning_ledge_area, waste_factor=1.15):
    """Calculates gunite volume including benches and tanning ledge."""

    # Adjust depths for extra 3 inches
    depth1_adjusted = depth1 + (3 / 12)  # Add 3 inches in feet
    depth2_adjusted = depth2 + (3 / 12)
    depth3_adjusted = depth3 + (3 / 12)

    avg_depth = (depth1_adjusted + depth2_adjusted + depth3_adjusted) / 3
    pool_volume_ft = length * width * avg_depth

    # Bench volume (18 inches wide = 1.5 feet)
    bench_volume_ft = bench_length * 1.5 * avg_depth

    # Tanning ledge volume (9 inches deep = 0.75 feet)
    tanning_ledge_volume_ft = tanning_ledge_area * 0.75

    total_volume_ft = pool_volume_ft + bench_volume_ft + tanning_ledge_volume_ft
    return total_volume_ft * waste_factor

st.title("Gunite Pool Calculator (Cubic Yards)")

# User inputs using Streamlit widgets
pool_length = st.number_input("Enter pool length (ft): ", value=20.0)
pool_width = st.number_input("Enter pool width (ft): ", value=10.0)
depth1 = st.number_input("Enter shallow depth (ft): ", value=3.0)
depth2 = st.number_input("Enter middle depth (ft): ", value=5.0)
depth3 = st.number_input("Enter deep depth (ft): ", value=8.0)
bench_length = st.number_input("Enter total bench length (ft): ", value=5.0)
tanning_ledge_area = st.number_input("Enter tanning ledge area (sq ft): ", value=20.0)

# Calculate and display results
if st.button("Calculate Gunite"):
    gunite_volume = calculate_gunite_volume(pool_length, pool_width, depth1, depth2, depth3, bench_length, tanning_ledge_area)
    gunite_cubic_yards = gunite_volume / 27

    st.write("## Gunite Calculation Results:")
    st.write(f"Gunite Volume: {gunite_cubic_yards:,.2f} cubic yards")
