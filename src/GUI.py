import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

def plot_median(values):
    generations = np.arange(len(values))
    values = np.array([np.pad(v, (0, max(map(len, values)) - len(v)), 'constant') for v in values])
    median_values = np.median(values, axis=1)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=generations, y=median_values, mode='lines+markers', name='Median', line=dict(color='red', width=2)))
    
    fig.update_layout(
    title="Median",
    xaxis_title='Generations',
    yaxis_title='Values',
    showlegend=True
    )

    pio.write_html(fig, "median.html")

    fig.show()

def plot_dispersion(values):
    
    fig = go.Figure()

    for i, gen_values in enumerate(values):
        fig.add_trace(go.Box(y=gen_values, name=f'Gen {i}', boxpoints='all', jitter=0.3, pointpos=-1.8))

    fig.update_layout(
        title="Dispersion",
        xaxis_title='Generations',
        yaxis_title='Values',
        showlegend=True
    )

    pio.write_html(fig, "dispersion.html")

    fig.show()

def plot_best_routes_animation(city_coordinates, best_routes, generations, best_distances):
    x_coords, y_coords = zip(*city_coordinates.values())
    city_names = list(city_coordinates.keys())

    fig = go.Figure()

    # Add initial scatter plot for cities
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers+text',
        marker=dict(size=20, color='red'),
        text=city_names,
        textposition="top center",
        name="Cities"
    ))

    # Add initial line plot for the first route
    initial_route = best_routes[0]
    bcx_coords, bcy_coords = zip(*[city_coordinates[city] for city in initial_route])
    fig.add_trace(go.Scatter(
        x=bcx_coords,
        y=bcy_coords,
        mode='lines',
        line=dict(color='green', width=2),
        name="Best Route",
        visible=True
    ))

    # Create frames for each generation
    frames = []
    for i, route in enumerate(best_routes):
        bcx_coords, bcy_coords = zip(*[city_coordinates[city] for city in route])
        frames.append(go.Frame(
            data=[
                go.Scatter(
                    x=x_coords,
                    y=y_coords,
                    mode='markers+text',
                    marker=dict(size=20, color='red'),
                    text=city_names,
                    textposition="top center",
                    name="Cities"
                ),
                go.Scatter(
                    x=bcx_coords,
                    y=bcy_coords,
                    mode='lines',
                    line=dict(color='green', width=2),
                    name="Best Route",
                    visible=True
                )
            ],
            name=f"frame{i}",
            layout=go.Layout(
                title=f"TSP Solution - Generation {generations[i]} | Distance: {best_distances[i]:.2f}"
            )
        ))

    fig.update_layout(
        updatemenus=[
            {
                "type": "buttons",
                "showactive": True,
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True, "transition": {"duration": 300, "easing": "quadratic-in-out"}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    },
                ],
                "direction": "left",
                "pad": {"r": 10},
                "x": -0.1,
                "xanchor": "left",
                "y": 0.5,
                "yanchor": "middle"
            }
        ],
        sliders=[{
            "steps": [
                {
                    "args": [
                        [f"frame{i}"],
                        {
                            "frame": {"duration": 300, "redraw": True},
                            "mode": "immediate",
                            "transition": {"duration": 300}
                        }
                    ],
                    "label": f"{generations[i]}",
                    "method": "animate"
                }
                for i in range(len(frames))
            ],
            "x": 0.1,
            "len": 0.9,
            "xanchor": "left",
            "y": -0.3,
            "yanchor": "top",
            "pad": {"b": 10},
            "transition": {"duration": 300, "easing": "cubic-in-out"}
        }]
    )

    fig.update(frames=frames)
    
    pio.write_html(fig, "best_chromosome.html")

    fig.show()

def plot_worst_routes_animation(city_coordinates, worst_routes, generations, worst_distances):
    x_coords, y_coords = zip(*city_coordinates.values())
    city_names = list(city_coordinates.keys())

    fig = go.Figure()

    # Add initial scatter plot for cities
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers+text',
        marker=dict(size=20, color='red'),
        text=city_names,
        textposition="top center",
        name="Cities"
    ))

    # Add initial line plot for the first route
    initial_route = worst_routes[0]
    bcx_coords, bcy_coords = zip(*[city_coordinates[city] for city in initial_route])
    fig.add_trace(go.Scatter(
        x=bcx_coords,
        y=bcy_coords,
        mode='lines',
        line=dict(color='orange', width=2),
        name="Worst Route",
        visible=True
    ))

    # Create frames for each generation
    frames = []
    for i, route in enumerate(worst_routes):
        bcx_coords, bcy_coords = zip(*[city_coordinates[city] for city in route])
        frames.append(go.Frame(
            data=[
                go.Scatter(
                    x=x_coords,
                    y=y_coords,
                    mode='markers+text',
                    marker=dict(size=20, color='red'),
                    text=city_names,
                    textposition="top center",
                    name="Cities"
                ),
                go.Scatter(
                    x=bcx_coords,
                    y=bcy_coords,
                    mode='lines',
                    line=dict(color='orange', width=2),
                    name="Worst Route",
                    visible=True
                )
            ],
            name=f"frame{i}",
            layout=go.Layout(
                title=f"TSP Solution - Generation {generations[i]} | Distance: {worst_distances[i]:.2f}"
            )
        ))

    fig.update_layout(
        updatemenus=[
            {
                "type": "buttons",
                "showactive": True,
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True, "transition": {"duration": 300, "easing": "quadratic-in-out"}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    },
                ],
                "direction": "left",
                "pad": {"r": 10},
                "x": -0.1,
                "xanchor": "left",
                "y": 0.5,
                "yanchor": "middle"
            }
        ],
        sliders=[{
            "steps": [
                {
                    "args": [
                        [f"frame{i}"],
                        {
                            "frame": {"duration": 300, "redraw": True},
                            "mode": "immediate",
                            "transition": {"duration": 300}
                        }
                    ],
                    "label": f"{generations[i]}",
                    "method": "animate"
                }
                for i in range(len(frames))
            ],
            "x": 0.1,
            "len": 0.9,
            "xanchor": "left",
            "y": -0.3,
            "yanchor": "top",
            "pad": {"b": 10},
            "transition": {"duration": 300, "easing": "cubic-in-out"}
        }]
    )

    fig.update(frames=frames)
    
    pio.write_html(fig, "worst_chromosome.html")

    fig.show()

def plot_median_routes_animation(city_coordinates, median_routes, generations, median_distances):
    x_coords, y_coords = zip(*city_coordinates.values())
    city_names = list(city_coordinates.keys())

    fig = go.Figure()

    # Add initial scatter plot for cities
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers+text',
        marker=dict(size=20, color='red'),
        text=city_names,
        textposition="top center",
        name="Cities"
    ))

    # Add initial line plot for the first route
    initial_route = median_routes[0]
    bcx_coords, bcy_coords = zip(*[city_coordinates[city] for city in initial_route])
    fig.add_trace(go.Scatter(
        x=bcx_coords,
        y=bcy_coords,
        mode='lines',
        line=dict(color='blue', width=2),
        name="Median Route",
        visible=True
    ))

    # Create frames for each generation
    frames = []
    for i, route in enumerate(median_routes):
        bcx_coords, bcy_coords = zip(*[city_coordinates[city] for city in route])
        frames.append(go.Frame(
            data=[
                go.Scatter(
                    x=x_coords,
                    y=y_coords,
                    mode='markers+text',
                    marker=dict(size=20, color='red'),
                    text=city_names,
                    textposition="top center",
                    name="Cities"
                ),
                go.Scatter(
                    x=bcx_coords,
                    y=bcy_coords,
                    mode='lines',
                    line=dict(color='blue', width=2),
                    name="Median Route",
                    visible=True
                )
            ],
            name=f"frame{i}",
            layout=go.Layout(
                title=f"TSP Solution - Generation {generations[i]} | Distance: {median_distances[i]:.2f}"
            )
        ))

    fig.update_layout(
        updatemenus=[
            {
                "type": "buttons",
                "showactive": True,
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True, "transition": {"duration": 300, "easing": "quadratic-in-out"}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    },
                ],
                "direction": "left",
                "pad": {"r": 10},
                "x": -0.1,
                "xanchor": "left",
                "y": 0.5,
                "yanchor": "middle"
            }
        ],
        sliders=[{
            "steps": [
                {
                    "args": [
                        [f"frame{i}"],
                        {
                            "frame": {"duration": 300, "redraw": True},
                            "mode": "immediate",
                            "transition": {"duration": 300}
                        }
                    ],
                    "label": f"{generations[i]}",
                    "method": "animate"
                }
                for i in range(len(frames))
            ],
            "x": 0.1,
            "len": 0.9,
            "xanchor": "left",
            "y": -0.3,
            "yanchor": "top",
            "pad": {"b": 10},
            "transition": {"duration": 300, "easing": "cubic-in-out"}
        }]
    )

    fig.update(frames=frames)
    
    pio.write_html(fig, "med_chromosome.html")

    fig.show()