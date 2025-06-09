# 📊 Real-Time Stock Dashboard

## Overview

This project presents a responsive and interactive dashboard built with Dash, Plotly, and Dash Bootstrap Components. Designed to support real-time stock movement monitoring, it features:

-User-friendly, dynamic visualizations that adapt seamlessly to any device:

-Essential KPIs (Key Performance Indicators) that are automatically and continuously updated to reflect live data.

-Intelligent dynamic target thresholds for each graph, paving the way for integration with machine learning models based on historical trends.

-A flexible backend capable of interfacing with various data sources such as Oracle, SQL, or even Excel files.

This tool is ideal for organizations looking to monitor inventory flows, optimize logistics, and gain actionable insights from their operational data.

---

##  Key Features

- **Flexible Data Sources**  
  Easily interface with various data formats and databases:  
  - Oracle  
  - SQL Server  
  - Excel files  

- **Dynamic Targets on Graphs**  
  Each visualization includes adjustable performance thresholds. These targets update automatically and can be integrated with **machine learning models** for predictive monitoring.

- **ML Integration-Ready**  
  The dashboard is designed to integrate seamlessly with machine learning models—developed using frameworks such as Scikit-learn or TensorFlow—leveraging historical stock data to automatically optimize target thresholds and detect anomalies in real time.

- **Mobile-Ready UI**  
  Thanks to Dash Bootstrap Components, the layout adapts to any screen size. Ideal for on-the-go access.

---

## Tech Stack

- Python  
- Dash & Plotly
- Flask  
- Dash Bootstrap Components  
- Pandas  
- cx_Oracle (for Oracle DB connection)

---

## Screenshot 

![shot1](https://github.com/user-attachments/assets/19af3787-7870-4b3f-8b4d-58b5caf98fd7)
![shot2](https://github.com/user-attachments/assets/648de25d-8dd9-4e9b-99a2-a8d9cd3823e3)
![shot3](https://github.com/user-attachments/assets/7b367e6d-e916-4138-bdce-661b1945f15e)
![shot4](https://github.com/user-attachments/assets/8fb0a218-f3b1-4a87-8347-caa20c06f87a)






---

```bash
git clone https://github.com/yourusername/real-time-stock-dashboard.git
cd real-time-stock-dashboard
pip install -r requirements.txt
python app.py

