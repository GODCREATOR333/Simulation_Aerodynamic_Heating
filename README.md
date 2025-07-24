# Simulation of Aerodynamic Heating for MIRV Trajectory Analysis

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

## 📊 Simulation Results

### **Figure 1: ISA upto 30,000 meters**
<img src="https://github.com/user-attachments/assets/5de6aa73-5d24-48db-9f4f-cd76a13fc83b" width="600"/>

### **Figure 2: Pressure, Density, Temperture upto 30,000 meters**
<img src="https://github.com/user-attachments/assets/aa02feef-3916-4e99-bdf7-3365abec5435" width="600"/>

### **Figure 3: ISA Model Output**
<img src="https://github.com/user-attachments/assets/5f6ce088-3369-43d6-818f-1c7b2177a8f2" width="600"/>

### **Figure 4: Isentropic Flow Parameters**
<img src="https://github.com/user-attachments/assets/eef85ebe-5cce-405a-8106-c8d0ffccbdf9" width="600"/>

### **Figure 5: Pressure-Altitude Curve**
<img src="https://github.com/user-attachments/assets/9430f957-8a35-4467-ac2f-0713ec2d5dee" width="600"/>



## 🔥 Future Work
🔹 Extend analysis to include **radiative heat transfer effects** at hypersonic speeds.  
🔹 Implement **parallel computing** with ROOT’s RDataFrame for enhanced performance.  
🔹 Develop **3D visualization tools** for better interpretation of reentry heat maps.  

---


