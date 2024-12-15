import plotly.graph_objects as go

def plot_route(city_coordinates, route, generation, best_distance):

    x_coords, y_coords = zip(*city_coordinates.values())
    bcx_coords, bcy_coords = zip(*route.values())
    city_names = list(city_coordinates.keys())

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers+text',
        marker=dict(size=20, color='red'),
        text=city_names,
        textposition="top center",
        name="Cities"
    ))

    fig.add_trace(go.Scatter(
        x=bcx_coords,                  
        y=bcy_coords,                  
        mode='lines',        
        line=dict(color='blue', width=2),          
        name="Best Route"           
    ))

    fig.update_layout(
        title=f"TSP Solution - Generation {generation} | Distance: {best_distance:.2f}",
        xaxis_title="X Coordinate",
        yaxis_title="Y Coordinate",
        legend=dict(
            x=0.85, y=1.1,            
            bgcolor="rgba(255,255,255,0.5)"  
        ),
        template="plotly_white"       
    )

    fig.show()