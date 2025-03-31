# UAV Strategic Deconfliction in Shared Airspace

## 🚀 Overview
UAV Strategic Deconfliction in Shared Airspace is an AI-powered system designed to ensure safe drone navigation in dynamic environments. Using **real-time conflict detection** and **automated path correction**, it prevents mid-air collisions and optimizes UAV trajectories.

## ✨ Features
- **4D Visualization (3D + Time)** with interactive **Plotly-based graphs** 📊
- **Conflict Detection & Resolution** using AI-driven algorithms 🚁
- **A* Search Algorithm** for computing conflict-free paths 🔍
- **Real-time Simulation** of drone movement and avoidance strategies 🎯
- **Terminal-Based UI** for launching simulations and monitoring conflicts 🖥️

## 📂 Project Structure
```
├── src/
│   ├── main.py                # Main execution file
│   ├── conflict_detection.py  # Identifies and resolves conflicts
│   ├── path_planner.py        # Implements A* search for new paths
│   ├── visualization.py       # Generates 4D drone trajectory graphs
│   ├── drone_data.json        # Simulated drone waypoints & times
│   ├── utils.py               # Helper functions
└── README.md
```

## 🎥 Demonstration
- **Conflict Scenario:** Initial UAV paths are visualized with potential conflicts.
- **Resolution Phase:** AI identifies conflicts and generates a new safe path.
- **Final Scenario:** The updated paths are simulated, ensuring conflict-free navigation.

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/UAV-Deconfliction-System.git
   cd UAV-Deconfliction-System
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulation:
   ```bash
   python3 src/main.py
   ```

## 🛠️ Technologies Used
- **Python** 🐍
- **Plotly** for 4D visualization 📊
- **ROS2 (Optional for real UAVs)** 🤖
- **A* Algorithm** for path planning 🏁

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to open issues, submit PRs, or suggest improvements! 🚀
