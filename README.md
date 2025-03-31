# AI Strategic UAV Deconfliction in Shared Airspace

## 🚀 Overview
The AI Strategic UAV Deconfliction System is an AI-powered conflict resolution framework designed for autonomous drones operating in shared airspace. It detects potential conflicts, resolves them using A search algorithms*, and visualizes 4D trajectories (3D space + time) using Plotly. The system ensures safe, efficient flight paths, preventing mid-air collisions in dynamic environments. 🚀

---

## 🚀 Features
✅ **4D Visualization (3D + Time)** with interactive **Plotly-based graphs** 📊  
✅ **Conflict Detection & Resolution** 🚁  
✅ **A* Search Algorithm** for computing conflict-free paths 🔍  
✅ **Real-time Simulation** of drone movement and avoidance strategies 🎯  

---

## 📂 Project Structure
```
uav/
│── data/
│   ├── primary_mission.json
│   ├── simulated_drones.json
│── src/
│   ├── conflict_checker.py
│   ├── conflict_resolver.py
│   ├── data_loader.py
│   ├── main.py
│   ├── visualization.py
│── requirements.txt
└── README.md
```

---

# 🖥️ Demonstration

This system is designed to detect and resolve trajectory conflicts between a primary drone and simulated drones in a shared environment. The system uses AI and pathfinding algorithms to suggest optimal, conflict-free paths when needed.

## Architecture Overview

### 1. **Conflict Detection**

The system continuously monitors the trajectories of both the **primary drone** and **simulated drones**. If the trajectories of the primary drone and any simulated drone intersect (indicating a potential collision), the system flags a **conflict**.

- **Conflict Point**: The system identifies the exact point or area where the trajectories intersect and displays the **conflict point**.
![Screenshot from 2025-03-31 22-30-58](https://github.com/user-attachments/assets/38c78c2e-2613-4896-8e51-49b53e436fa6)

### 2. **User Interaction (Conflict Management)**

If a conflict is detected, the system provides the following options in the terminal:
- **Option to Visualize Conflict-Free Path**: 
  - The terminal will prompt you to **press Enter** to visualize the conflict-free path.
  
When you press "Enter":
- The AI system will use the **A* (A-star) algorithm** to suggest an optimal, **conflict-free path** that avoids collisions with simulated drones.
![Screenshot from 2025-03-31 22-34-32](https://github.com/user-attachments/assets/44f7a35b-ecc0-4fa8-a15c-49a0b4338f49)

### 3. **No Conflict Scenario**

If the system detects that there is no intersection or conflict between the primary drone's trajectory and the simulated drones' trajectories, it will display:
- **"No conflict point found, safe to proceed."**

In this case, the drones can continue their respective paths without any modifications.
![Screenshot from 2025-03-31 22-32-54](https://github.com/user-attachments/assets/09a26f9a-3ab5-4327-87dd-bd8b60bb098d)

---

## 📹 Working Video

https://drive.google.com/file/d/1MHYSF-rkZaQaEAq07xGc_y6eMgfsz6lw/view?usp=sharing

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yashbhaskar/AI-Strategic-Drone-Deconfliction.git
   cd uav
   cd src
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulation:
   ```bash
   python3 src/main.py
   ```

---

## 🛠️ Technologies Used
- **Python**🐍 - Core programming language for the deconfliction system.
- **Plotly**📊 – Used for 4D (3D space + time) trajectory visualization with interactive animations.
- **NumPy & SciPy**🔢 – Used for numerical computations, path interpolation, and data handling.
- **A * Algorithm**🏁 – Implements AI-driven path planning and conflict resolution, ensuring safe drone navigation.

---

## ✉️ Contact

📧 Yash Bhaskar – ybbhaskar19@gmail.com
📌 GitHub: https://github.com/yashbhaskar
