# Airport Route Analyzer

## Overview

The **Airport Route Analyzer** is a web-based application built using Streamlit that allows users to analyze and visualize the connections between Indian airports. It enables users to explore strongly connected components (SCCs) within the airport network and find the shortest flight paths between different airports.

## Features

- **SCC Analysis**: Identify whether two airports belong to the same strongly connected component.
- **Graph Visualization**: Visualize the flight routes between airports using NetworkX and Matplotlib.
- **Shortest Path Finder**: Compute the shortest flight path between selected airports using Dijkstra's algorithm.

## Technologies Used

- Python
- Streamlit
- NetworkX
- Matplotlib
- Collections

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install required packages: Make sure you have pip installed, then run:

bash
Copy code
pip install -r requirements.txt
Run the application: Start the Streamlit server:

bash
Copy code
streamlit run app.py
Open your web browser: Navigate to http://localhost:8501 to access the application.

Usage
Home Page: Overview and navigation options.
SCC Analysis:
Select a source and destination airport.
Click "Check" to see if both airports belong to the same SCC.
Graph Visualization:
Displays a visual representation of the airport network.
Strongly connected components are highlighted in different colors.
Shortest Path:
Choose source and destination airports.
Click "Find Shortest Path" to display the route, if available.
Sample Data
The application includes sample data representing Indian airports and their flight routes. You can modify the airports and flight_routes dictionaries in the code to add or remove airports and routes.
