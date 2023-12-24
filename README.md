# OEE Analysis
Overview

This repository serves as a resource for training and analysis of Overall Equipment Efficiency (OEE) and machine metrics in manufacturing environments. OEE is a key performance indicator used to measure the effectiveness of production processes, providing insights into the efficiency and utilization of equipment.
Contents

    assets_sensing.py: Module for monitoring the location and operations of key logistical assets. Generates reports on asset status and supply route efficiency.

    ambient_sensing.py: Module for real-time monitoring of environmental conditions in industrial settings. Captures data on temperature, pressure, CO2 levels, and particulate matter, offering historical records and alerts.

    data_sensing.py: Module automating the collection of local data from equipment on the factory floor. Connects equipment to the cloud, eliminates manual reporting, and identifies equipment failures.

    first_mes.py: Module for monitoring the overall efficiency of manufacturing processes. Conducts a personalized analysis to enhance factory performance, identify bottlenecks, and control material quality.

    equipment_sensing.py: Module for monitoring key equipment, providing data for predictive maintenance of motors, compressors, and pumps. Analyzes vibration, temperature, and operational trends.

    process_sensing.py: Module for monitoring essential manufacturing processes online. Validates takt time, identifies bottlenecks in real-time, and provides insights into the overall effectiveness of equipment (OEE).

Getting Started

    Clone the repository:

    bash

git clone https://github.com/natalia-dias01/oee-analysis.git
cd oee-analysis

Install the required dependencies:

bash

    pip install -r requirements.txt

    Run individual modules or integrate them as needed for your specific use case.

Usage

Each module can be executed independently to simulate the sensing and analysis of specific aspects related to OEE and machine metrics. Additionally, the scripts are set up to run 24/7, generating daily reports in PDF format.
Running a Module

To run a specific module, use the following command:

bash

python <module_name>.py

Replace <module_name> with the name of the module you want to execute (e.g., python ambient_sensing.py).
Consolidating Reports

To consolidate daily reports into a single PDF file, use the following command:

bash

python consolidate_reports.py

The consolidated report will be saved as consolidated_reports.pdf.
Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or provide suggestions for improvement. Please follow the contribution guidelines.

License
This project is licensed under the MIT License.
