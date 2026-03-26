# 🚖 Smart ride : AI-Based Taxi Fare Optimization and Recommendation System

## 📌 Project Overview
SmartRide is an AI-based taxi fare estimation and recommendation system developed using Python. The system calculates the total fare for different vehicle types and suggests the best option based on user preference — either lowest cost or fastest travel time.

This project simulates real-world conditions like traffic and helps users make intelligent travel decisions.


## 🎯 Objectives
- To estimate taxi fare based on distance, vehicle type, and waiting time  
- To recommend the best vehicle based on:
  - 💰 Minimum Cost  
  - 🚀 Minimum Travel Time  
- To simulate real-world traffic conditions  
- To demonstrate basic AI decision-making and optimization  

## 🧠 Technologies Used
- Python  
- Basic AI Concepts (Rule-Based System, Greedy Algorithm)  
- Random Module (for traffic simulation)  

## ⚙️ Features
- 🚗 Multiple vehicle options (Hatchback, Sedan, SUV, Premium Sedan)  
- 💸 Fare calculation based on distance and vehicle type  
- ⏱️ Travel time estimation using speed and traffic factor  
- 🤖 Intelligent recommendation system  
- 👥 Passenger-based vehicle filtering  
- 🔁 Round trip support  
- ⏳ Waiting time charges  

## 🧩 How It Works
1. User inputs:
   - Distance (in km)
   - Number of passengers
   - Preference (Cost / Time)

2. System:
   - Calculates fare for all vehicle types  
   - Estimates travel time using simulated traffic  
   - Filters vehicles based on passenger capacity  

3. Output:
   - Displays all available options  
   - Recommends the best vehicle  

 🧮 Algorithm Used

# 1. Rule-Based System
Fare is calculated using predefined formulas:

Fare = Base Fare + (Rate per km × Distance) + Waiting Charges

# 2. Greedy Optimization Algorithm
- Selects the best option based on:
  - Minimum cost OR
  - Minimum time  

# 3. Simulation
- Random traffic factor is used to mimic real-world conditions  


# How to Run
1. Install Python (if not installed)  
2. Copy the code into a `.py` file  
3. Run the file:
python smartride.py

 🚀 Future Enhancements
- Integration with real-time traffic APIs  
- Machine Learning model for fare prediction  
- GUI using Tkinter or Web App  
- Route optimization using maps  

📌 Conclusion
This project demonstrates how basic AI concepts like decision-making, optimization, and simulation can be applied to solve real-world problems such as taxi fare estimation and ride selection.

