import streamlit as st

def calculate_gunite(perimeter, min_depth, max_depth, wall_thickness=0.5, floor_thickness=0.5, niche_lights=0, drains=0):
    """Calculates the approximate gunite needed for a pool or spa."""

    average_depth = (min_depth + max_depth) / 2
    wall_area = perimeter * average_depth
    floor_area = 144  # Rough 12x12 approx.
    wall_volume = wall_area * wall_thickness
    floor_volume = floor_area * floor_thickness
    total_volume_feet = wall_volume + floor_volume
    total_volume_yards = total_volume_feet / 27
    total_volume_yards += niche_lights + drains
    total_volume_yards *= 1.15
    return total_volume_yards

st.title("Gunite Calculator")

# Input fields
perimeter = st.number_input("Perimeter (feet)", value=80.0)
min_depth = st.number_input("Minimum Depth (feet)", value=3.0)
max_depth = st.number_input("Maximum Depth (feet)", value=6.0)
wall_thickness = st.number_input("Wall Thickness (feet)", value=0.5)
floor_thickness = st.number_input("Floor Thickness (feet)", value=0.5)
niche_lights = st.number_input("Number of Niche Lights", value=0, step=1)
drains = st.number_input("Number of Drains", value=0, step=1)

# Calculate and display results
if st.button("Calculate Gunite"):
    gunite_needed = calculate_gunite(perimeter, min_depth, max_depth, wall_thickness, floor_thickness, niche_lights, drains)
    st.write(f"Approximate gunite needed: {gunite_needed:.2f} cubic yards")

st.markdown("---")
st.markdown("## Instructions")
st.markdown("1. Enter the pool's perimeter, minimum depth, and maximum depth.")
st.markdown("2. Enter the wall and floor thicknesses.")
st.markdown("3. Enter the number of niche lights and drains.")
st.markdown("4. Click the 'Calculate Gunite' button.")
st.markdown("5. The approximate gunite needed will be displayed.")

st.markdown("### Important Notes")
st.markdown("- This calculator provides an *approximation*. For precise estimates, consult a professional.")
st.markdown("- The floor area is a rough estimate. Use actual floor area for better accuracy.")
st.markdown("- The 15% waste buffer can vary.")
