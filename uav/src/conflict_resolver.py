import heapq
import numpy as np

def heuristic(a, b):
    """Heuristic function: Euclidean distance"""
    return np.linalg.norm(np.array(a) - np.array(b))

def a_star_search(start, goal, obstacles, grid_size=1):
    """A* algorithm to find shortest, conflict-free path"""
    start, goal = tuple(start), tuple(goal)  # Convert to tuple
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        neighbors = [
            (current[0] + grid_size, current[1], current[2]), 
            (current[0] - grid_size, current[1], current[2]),
            (current[0], current[1] + grid_size, current[2]),
            (current[0], current[1] - grid_size, current[2]),
            (current[0], current[1], current[2] + grid_size), 
            (current[0], current[1], current[2] - grid_size)
        ]

        for neighbor in neighbors:
            neighbor = tuple(neighbor)  # Convert to tuple for hashing

            if neighbor in obstacles:
                continue  # Avoid conflicts

            temp_g_score = g_score[current] + heuristic(current, neighbor)

            if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found


def resolve_conflict(primary_mission, simulated_drones):
    """Find new conflict-free path using A* and store original waypoints"""
    start = tuple(primary_mission["waypoints"][0])
    goal = tuple(primary_mission["waypoints"][-1])

    # Store original path for visualization
    primary_mission["original_waypoints"] = primary_mission["waypoints"][:]  # Copy original

    # Collect conflict points as obstacles
    obstacles = set()
    for drone in simulated_drones:
        for waypoint in drone["waypoints"]:
            obstacles.add(tuple(waypoint))

    # Run A* search
    new_path = a_star_search(start, goal, obstacles)

    if new_path:
        print("\n✅ New Conflict-Free Path Found!\n")
        primary_mission["waypoints"] = [list(point) for point in new_path]  # Convert to list
    else:
        print("\n⚠️ Unable to find a conflict-free path. Manual intervention required.\n")

    return primary_mission

