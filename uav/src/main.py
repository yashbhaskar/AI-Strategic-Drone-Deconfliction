from data_loader import load_flight_data
from visualization import plot_4d_trajectories, animate_trajectories, visualize_conflicts
from conflict_resolver import resolve_conflict
from conflict_checker import check_conflicts
import matplotlib.pyplot as plt

# Load data
primary_mission, simulated_drones = load_flight_data(
    "/home/yash/uav/data/primary_mission.json",
    "/home/yash/uav/data/simulated_drones.json"
)

conflicts = check_conflicts(primary_mission, simulated_drones)

# Run conflict check
conflicts = check_conflicts(primary_mission, simulated_drones)

plt.ion()  

# Static 4D Visualization (3D Space + Conflict Points)
plot_4d_trajectories(primary_mission, simulated_drones, conflicts)

# Print results
if conflicts:
    print("⚠️ Conflict Detected!")
    for conflict in conflicts:
        print(f"Time: {conflict['time']}s, Location: {conflict['location']}, Drone: {conflict['conflicting_drone']}")
        primary_mission = resolve_conflict(primary_mission, simulated_drones)

        # User confirmation before visualizing the new path
        
        input("\n🔍 Press Enter to visualize the new conflict-free path...")
        visualize_conflicts(primary_mission, simulated_drones, conflicts)


else:
    print("✅ No conflicts detected. Safe to proceed.")

plt.ioff()
plt.show()

