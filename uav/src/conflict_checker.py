import numpy as np

SAFETY_DISTANCE = 4.0  # Adjust as needed
TIME_THRESHOLD = 2 # Allowable time difference in seconds

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def check_conflicts(primary_mission, simulated_drones):
    """Check if primary mission conflicts with simulated drone paths."""
    conflicts = []

    print("\n🚀 PRIMARY DRONE WAYPOINTS:")
    for i, (px, py, pz) in enumerate(primary_mission["waypoints"]):
        print(f"   Waypoint {i+1}: ({px}, {py}, {pz}) at {primary_mission['times'][i]}s")

    print("\n🛸 SIMULATED DRONES WAYPOINTS:")
    for drone in simulated_drones:
        print(f"\nDrone {drone['id']} Path:")
        for j, (dx, dy, dz) in enumerate(drone["waypoints"]):
            print(f"   Waypoint {j+1}: ({dx}, {dy}, {dz}) at {drone['times'][j]}s")

    print("\n🔍 CHECKING FOR CONFLICTS...")

    # Iterate over primary mission waypoints
    for i, (px, py, pz) in enumerate(primary_mission["waypoints"]):
        pt = primary_mission["times"][i]

        for drone in simulated_drones:
            for j, (dx, dy, dz) in enumerate(drone["waypoints"]):
                dt = drone["times"][j]

                distance = euclidean_distance((px, py, pz), (dx, dy, dz))
                time_diff = abs(pt - dt)

                # Debugging print
                print(f"🔍 Comparing: Primary ({px}, {py}, {pz}) at {pt}s | Drone {drone['id']} ({dx}, {dy}, {dz}) at {dt}s")
                print(f"   Distance = {distance:.2f}, Time Difference = {time_diff}s")

                # Check for conflict
                if distance < SAFETY_DISTANCE and time_diff < TIME_THRESHOLD:
                    print(f"⚠️ CONFLICT DETECTED with {drone['id']} at ({dx}, {dy}, {dz})")
                    conflicts.append({
                        "location": (dx, dy, dz),
                        "time": dt,
                        "conflicting_drone": drone["id"]
                    })
    
    return conflicts

