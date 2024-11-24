import svgwrite

def create_die_svg(base_file_name, side_length=50, pip_radius=5):
    # Define pip positions for a standard die (1-6)
    pip_positions = {
        1: [(0.5, 0.5)],
        2: [(0.25, 0.25), (0.75, 0.75)],
        3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
        4: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)],
        5: [(0.25, 0.25), (0.75, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.75)],
        6: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.5), (0.75, 0.5), (0.25, 0.75), (0.75, 0.75)]
    }

    # Loop over each face of the die
    for side in range(1, 7):
        # Create SVG drawing for each die face
        file_name = f"{base_file_name}_face_{side}.svg"
        dwg = svgwrite.Drawing(file_name, profile='tiny', size=(side_length, side_length))

        # Draw a square for the die face
        dwg.add(dwg.rect((0, 0), (side_length, side_length), fill='white', stroke='black', stroke_width=2))

        # Add pips based on position
        for (px, py) in pip_positions[side]:
            cx = px * side_length
            cy = py * side_length
            dwg.add(dwg.circle(center=(cx, cy), r=pip_radius, fill='black'))
        
        # Save the SVG file for each die face
        dwg.save()

# Generate SVG files for dice faces 1 to 6
create_die_svg("dice", side_length=50, pip_radius=5)
