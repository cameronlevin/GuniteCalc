import streamlit as st

def calculate_gunite(perimeter, min_depth, max_depth, wall_thickness_inches, floor_thickness_inches, niche_lights, drains):
    """Calculates the approximate gunite needed for a pool or spa, accounting for a 12x12 beam."""

    wall_thickness_feet = wall_thickness_inches / 12.0
    floor_thickness_feet = floor_thickness_inches / 12.0

    # Calculate the beam volume (12x12 inches around the entire perimeter)
    beam_thickness_feet = 1.0  # 12 inches = 1 foot
    beam_volume = perimeter * 1.0 * 1.0  # perimeter * height * width

    # Calculate the wall volume (tapered from 12 inches to the chosen thickness)
    average_wall_thickness_feet = (1.0 + wall_thickness_feet) / 2.0
    average_depth = (min_depth + max_depth) / 2
    wall_area = perimeter * average_depth
    wall_volume = wall_area * average_wall_thickness_feet

    # Calculate the floor volume
    floor_area = 144  # Rough 12x12 approx.
    floor_volume = floor_area * floor_thickness_feet

    # Calculate total volume in cubic feet
    total_volume_feet = beam_volume + wall_volume + floor_volume

    # Convert to cubic yards
    total_volume_yards = total_volume_feet / 27

    # Add extra gunite for niche lights and drains
    total_volume_yards += niche_lights + drains

    # Add 15% for waste and overspray
    total_volume_yards *= 1.15

    return total_volume_yards

st.title("Gunite Calculator (with 12x12 Beam)")

# Input fields (inches)
perimeter = st.number_input("Perimeter (feet)", value=80.0)
min_depth = st.number_input("Minimum Depth (feet)", value=3.0)
max_depth = st.number_input("Maximum Depth (feet)", value=6.0)
wall_thickness_inches = st.number_input("Wall Thickness (inches)", value=6.0)
floor_thickness_inches = st.number_input("Floor Thickness (inches)", value=6.0)
niche_lights = st.number_input("Number of Niche Lights", value=0, step=1)
drains = st.number_input("Number of Drains", value=0, step=1)

# Calculate and display results
if st.button("Calculate Gunite"):
    gunite_needed = calculate_gunite(perimeter, min_depth, max_depth, wall_thickness_inches, floor_thickness_inches, niche_lights, drains)
    st.write(f"Approximate gunite needed: {gunite_needed:.2f} cubic yards")

st.markdown("---")
st.markdown("## Instructions")
st.markdown("1. Enter the pool's perimeter, minimum depth, and maximum depth.")
st.markdown("2. Enter the wall and floor thicknesses in *inches*.")
st.markdown("3. Enter the number of niche lights and drains.")
st.markdown("4. Click the 'Calculate Gunite' button.")
st.markdown("5. The approximate gunite needed will be displayed.")

st.markdown("### Important Notes")
st.markdown("- This calculator provides an *approximation*. For precise estimates, consult a professional.")
st.markdown("- The floor area is a rough estimate. Use actual floor area for better accuracy.")
st.markdown("- The 15% waste buffer can vary.")
st.markdown("- This calculation assumes a 12x12 inch beam around the entire perimeter, tapering to the user input wall thickness.")
