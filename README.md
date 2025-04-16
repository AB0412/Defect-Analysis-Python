Defect Dashboard Setup & Usage Guide
This guide helps you set up and run a defect analysis dashboard using Streamlit on macOS.
1. Prerequisites
Ensure Python 3 is installed. Check by running:
python3 --version
2. Install pip (if missing)
Run the following in Terminal:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
3. Create a Virtual Environment (Recommended)
Run:
python3 -m venv defect-env
source defect-env/bin/activate
4. Install Required Python Packages
Run this inside your environment:
pip install streamlit pandas matplotlib seaborn
5. Run the Streamlit Dashboard
Make sure defect_dashboard.py and defect_dataset_1000.csv are in the same directory. Then run:
streamlit run defect_dashboard.py
6. Using the Dashboard
Ask natural language questions like:
•	- How many defects are due today?
- Show high severity open defects
- What defects are related to Accounts Payable
Click buttons to view aging charts, severity breakdowns, and status summaries.
You can also download the dataset as a CSV.
![image](https://github.com/user-attachments/assets/9efd5246-ab4e-4f2d-92f4-d5d7a3742565)
