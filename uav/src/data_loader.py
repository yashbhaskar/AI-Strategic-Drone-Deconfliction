import json

def load_flight_data(primary_file, simulated_file):
    """Loads flight data from JSON files."""
    with open(primary_file, 'r') as f:
        primary_mission = json.load(f)
    
    with open(simulated_file, 'r') as f:
        simulated_drones = json.load(f)

    return primary_mission, simulated_drones

