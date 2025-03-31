import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import random

def visualize_conflicts(primary, simulated_drones, conflicts):
    """ Visualizes UAV conflict zones in 3D space using Plotly. """
    fig = go.Figure()

    fig.update_layout(
        template="plotly_dark",  
        scene=dict(
            xaxis=dict(backgroundcolor="black", gridcolor="white", color="white"),
            yaxis=dict(backgroundcolor="black", gridcolor="white", color="white"),
            zaxis=dict(backgroundcolor="black", gridcolor="white", color="white"),
        ),
        paper_bgcolor="black",
        plot_bgcolor="black",
        font=dict(color="white")
    )

    # **Plot Primary Drone's Original Trajectory** (Blue)
    fig.add_trace(go.Scatter3d(
        x=[p[0] for p in primary["original_waypoints"]],
        y=[p[1] for p in primary["original_waypoints"]],
        z=[p[2] for p in primary["original_waypoints"]],
        mode='lines+markers',
        name="Original Path",
        marker=dict(size=5, color='blue'),
        line=dict(width=8, color='blue')  # Thicker line
    ))

    # **Plot Conflict-Free Path** (Green)
    fig.add_trace(go.Scatter3d(
        x=[p[0] for p in primary["waypoints"]],
        y=[p[1] for p in primary["waypoints"]],
        z=[p[2] for p in primary["waypoints"]],
        mode='lines+markers',
        name="New Conflict-Free Path",
        marker=dict(size=5, color='lime'),
        line=dict(width=8, color='lime')
    ))


    # **Assign unique colors to each simulated drone**
    colors = ["green","orange","yellow","blue","white"]


    # **Plot Simulated Drones**
    for idx, drone in enumerate(simulated_drones):
        color = colors[idx % len(colors)]  # Ensure unique colors
        fig.add_trace(go.Scatter3d(
            x=[p[0] for p in drone["waypoints"]],
            y=[p[1] for p in drone["waypoints"]],
            z=[p[2] for p in drone["waypoints"]],
            mode='lines+markers',
            name=f"Drone {drone['id']}",
            marker=dict(size=5, color=color),
            line=dict(width=8, color=color)
        ))

    # **Highlight Conflict Points (Bright Red)**
    for conflict in conflicts:
        cx, cy, cz = conflict["location"]
        fig.add_trace(go.Scatter3d(
            x=[cx], y=[cy], z=[cz],
            mode='markers',
            marker=dict(size=12, color='red', symbol='cross'),
            name="Conflict Point"
        ))

    fig.show()



def plot_4d_trajectories(primary, simulated_drones, conflicts):
    """Plots 4D (3D + Time) UAV trajectories with Conflict Points using Plotly."""
    data = []

    # Ensure `times` exist and match waypoints
    if "times" in primary and len(primary["times"]) == len(primary["waypoints"]):
        for i, (x, y, z) in enumerate(primary["waypoints"]):
            data.append({"Drone": "Primary", "X": x, "Y": y, "Z": z, "Time": primary["times"][i]})
    else:
        print("⚠️ Warning: `primary['times']` missing/mismatched. Using index as time.")
        for i, (x, y, z) in enumerate(primary["waypoints"]):
            data.append({"Drone": "Primary", "X": x, "Y": y, "Z": z, "Time": i})

    # Add Simulated Drones' waypoints
    for drone in simulated_drones:
        if "times" in drone and len(drone["times"]) == len(drone["waypoints"]):
            for i, (x, y, z) in enumerate(drone["waypoints"]):
                data.append({"Drone": f"Drone {drone['id']}", "X": x, "Y": y, "Z": z, "Time": drone["times"][i]})
        else:
            print(f"⚠️ Warning: `Drone {drone['id']}` times missing/mismatched. Using index as time.")
            for i, (x, y, z) in enumerate(drone["waypoints"]):
                data.append({"Drone": f"Drone {drone['id']}", "X": x, "Y": y, "Z": z, "Time": i})

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Assign unique colors to each drone
    drone_colors = {
        "Primary": "red",
        "Drone 1": "blue",
        "Drone 2": "green",
        "Drone 3": "orange"
    }

    fig = go.Figure()

    # Plot trajectories for each drone
    for idx, drone in enumerate(df["Drone"].unique()):
        drone_df = df[df["Drone"] == drone]
        color = drone_colors.get(f"Drone {idx+1}", "white")

        fig.add_trace(go.Scatter3d(
            x=drone_df["X"], y=drone_df["Y"], z=drone_df["Z"],
            mode='lines+markers',
            name=drone,
            line=dict(width=8, color=color),
            marker=dict(size=5, color=color)
        ))

    # ✅ **Add Conflict Points (Large Red "X")**
    if conflicts:
        for conflict in conflicts:
            cx, cy, cz = conflict["location"]
            fig.add_trace(go.Scatter3d(
                x=[cx], y=[cy], z=[cz],
                mode='markers',
                marker=dict(size=12, color='red', symbol='x'),
                name="Conflict Point"
            ))
    else:
        print("⚠️ No conflict points found!")

    # Apply black theme
    fig.update_layout(
        template="plotly_dark",
        title="4D UAV Trajectories",
        scene=dict(
            xaxis=dict(backgroundcolor="black", gridcolor="white", color="white"),
            yaxis=dict(backgroundcolor="black", gridcolor="white", color="white"),
            zaxis=dict(backgroundcolor="black", gridcolor="white", color="white"),
        ),
        paper_bgcolor="black",
        plot_bgcolor="black",
        font=dict(color="white")
    )

    fig.show()




def animate_trajectories(primary, simulated_drones):
    """ Creates an animated UAV flight visualization with connected trajectories. """
    frames = []
    all_times = sorted(set(primary["times"] + [t for drone in simulated_drones for t in drone["times"]]))

    for t in all_times:
        data = []

        # Primary Drone Path Up to Current Time
        past_waypoints = [primary["waypoints"][i] for i in range(len(primary["times"])) if primary["times"][i] <= t]
        if past_waypoints:
            data.append(go.Scatter3d(
                x=[p[0] for p in past_waypoints],
                y=[p[1] for p in past_waypoints],
                z=[p[2] for p in past_waypoints],
                mode="lines+markers",
                marker=dict(size=5, color="blue"),
                line=dict(color="blue", width=8),
                name="Primary Drone"
            ))

        # Simulated Drones Paths Up to Current Time
        for drone in simulated_drones:
            past_waypoints = [drone["waypoints"][i] for i in range(len(drone["times"])) if drone["times"][i] <= t]
            if past_waypoints:
                data.append(go.Scatter3d(
                    x=[p[0] for p in past_waypoints],
                    y=[p[1] for p in past_waypoints],
                    z=[p[2] for p in past_waypoints],
                    mode="lines+markers",
                    marker=dict(size=5, color="red"),
                    line=dict(color="red", width=8),
                    name=f"Drone {drone['id']}"
                ))

        frames.append(go.Frame(data=data, name=str(t)))

    fig = go.Figure(
        data=[go.Scatter3d(x=[], y=[], z=[], mode="lines+markers")],
        layout=go.Layout(
            title="UAV Flight Animation",
            scene=dict(
                xaxis=dict(backgroundcolor="black", gridcolor="gray", color="white"),
                yaxis=dict(backgroundcolor="black", gridcolor="gray", color="white"),
                zaxis=dict(backgroundcolor="black", gridcolor="gray", color="white"),
            ),
            paper_bgcolor="black",
            plot_bgcolor="black",
            font=dict(color="white"),
            updatemenus=[{
                "buttons": [
                    {"args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                     "label": "Play", "method": "animate"},
                    {"args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                     "label": "Pause", "method": "animate"}
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }]
        ),
        frames=frames
    )

    fig.show()

