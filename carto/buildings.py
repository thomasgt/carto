import osmnx as ox


def make_plot(place, point, network_type="drive", edge_color="#FFD500", bldg_color="#3B14AF", bg_colour="#082368", dpi=40,
              dist=805, default_width=4, street_widths=None):
    gdf = ox.buildings_from_point(point=point, distance=dist)
    gdf_proj = ox.project_gdf(gdf)
    fig, ax = ox.plot_figure_ground(point=point, dist=dist, network_type=network_type, default_width=default_width,
                                    street_widths=street_widths, edge_color=edge_color, bgcolor=bg_colour, save=False, show=False, close=True)
    fig, ax = ox.plot_buildings(gdf_proj, fig=fig, ax=ax, color=bldg_color, set_bounds=False,
                                save=True, show=False, close=True, filename=place, dpi=dpi)
