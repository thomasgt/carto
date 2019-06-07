import osmnx as ox

place = "lisbon_buildings"
point = (38.722620, -9.146700)

# edge_color = "#FFD500"
# bg_colour = "#082368"

edge_color = "#000000"
bg_colour = "#FFFFFF"

street_widths = {'footway': 0.5,
                 'steps': 0.5,
                 'pedestrian': 0.5,
                 'path': 0.5,
                 'track': 0.5,
                 'service': 2,
                 'residential': 3,
                 'primary': 5,
                 'motorway': 6,
                 'secondary': 3}

fig, ax = ox.plot_figure_ground(point=point,
                                dist=1200,
                                network_type="drive",
                                default_width=1,
                                street_widths=street_widths,
                                edge_color=edge_color,
                                bgcolor=bg_colour,
                                save=True,
                                show=False,
                                close=True,
                                filename=place,
                                dpi=300)
