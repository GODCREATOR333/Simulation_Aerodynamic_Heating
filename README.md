# Simulation of Aerodynamic Heating for MIRV Trajectory Analysis

## Defence Research and Development Organisation (DRDO-DRDL), Hyderabad
**Project Intern | Sept 2023 - Oct 2023**  
**Under the guidance of Shaik Ismail, Scientist ‘F’, DRDO-DRDL**

## 🚀 Project Overview
This project focuses on analyzing aerodynamic heating challenges encountered by **Multiple Independently Targetable Reentry Vehicles (MIRVs)** during atmospheric reentry. Using **Python, NumPy, SciPy, and PyROOT (CERN’s Python interface for ROOT)**, I developed optimized computational models to enhance trajectory calculations and heat transfer assessments.

### **Key Contributions:**
- **Analyzed 13,000+ data points** across **25+ parameters** to study aerodynamic heating effects on MIRVs.
- **Transitioned from MATLAB to Python**, leveraging **NumPy/SciPy** for faster numerical simulations of heat transfer and trajectory modeling.
- **Implemented PyROOT** to process large datasets efficiently, enabling high-speed computation of:
  - Isentropic flow parameters
  - Stagnation temperature calculations
  - Standard atmospheric parameters (density, pressure, temperature, speed of sound) across altitudes.
- **Developed data visualization tools** to analyze transient heat behavior and skin temperature variations across different altitudes.

---

## 📌 Technical Stack
- **Programming Languages:** Python
- **Libraries & Tools:** NumPy, SciPy, Matplotlib, PyROOT (CERN), Pandas, ROOT Framework
- **Concepts Covered:** Computational Aerodynamics, Isentropic Flow, Stagnation Temperature, Transient Heat Transfer, Standard Atmosphere Model

---

## 📊 Simulation Approach
### **1️⃣ Atmospheric Model Implementation**
- Used **standard atmospheric equations** to compute density, pressure, temperature, and speed of sound at different altitudes.
- Developed a Python-based **atmospheric model** replacing MATLAB scripts for enhanced efficiency.

### **2️⃣ Aerodynamic Heating Analysis**
- Implemented **isentropic flow relations** to compute stagnation temperature variations at hypersonic speeds.
- Simulated heat flux variations across the vehicle surface using **Python-based numerical solvers**.

### **3️⃣ Data Processing & Visualization with PyROOT**
- Leveraged **ROOT’s TTree & TGraph** for high-performance data storage and visualization.
- Generated plots comparing **stagnation temperature rise vs free stream velocity** for various altitudes.

---

## 📈 Key Results & Insights
✅ Optimized Python-based models significantly **reduced computational time** compared to MATLAB.  
✅ **New insights** into **skin temperature distribution and transient heat behavior** at different reentry speeds.  
✅ **PyROOT integration** enabled faster processing of large-scale aerodynamic datasets, improving analysis precision.  
✅ The approach provides a **robust framework for future trajectory simulations and hypersonic vehicle design studies**.  

---

## 🔥 Future Work
🔹 Extend analysis to include **radiative heat transfer effects** at hypersonic speeds.  
🔹 Implement **parallel computing** with ROOT’s RDataFrame for enhanced performance.  
🔹 Develop **3D visualization tools** for better interpretation of reentry heat maps.  

---

## 🏆 Acknowledgments
I extend my sincere gratitude to **Shaik Ismail, Scientist ‘F’, DRDO-DRDL**, for his invaluable mentorship and guidance throughout this project. This research has provided a deep understanding of **hypersonic aerodynamics and computational methods in aerospace engineering**.

---


