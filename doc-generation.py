from fpdf import FPDF
from datetime import datetime

# Create PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Defect Analysis Dashboard Documentation', 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create PDF document
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=11)

# Add title and metadata
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Defect Analysis Dashboard Documentation', 0, 1, 'C')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f'Version: 1.0 | Last Updated: {datetime.now().strftime("%Y-%m-%d")}', 0, 1, 'C')
pdf.ln(10)

# Add sections
sections = [
    ("1. Overview", "The Defect Analysis Dashboard is a Streamlit-based interactive tool designed to analyze and visualize defect tracking data through natural language queries."),
    ("2. System Requirements", "Python 3.8+\nLibraries:\nstreamlit==1.13.0\npandas==1.5.3\nmatplotlib==3.7.0\nseaborn==0.12.2"),
    ("3. Data Structure", "Input File: defect_dataset_1000.csv\nColumns:\n- Logged Date: DateTime\n- Closed Date: DateTime\n- Summary: String\n- Severity: String\n- Status: String\n- Module: String"),
    ("4. Features", "A. Natural Language Query\nB. Visualizations\nC. Data Export"),
    ("5. How to Use", "1. Installation: pip install -r requirements.txt\n2. Run: streamlit run defect_dashboard.py\n3. Input queries like 'Show high severity open defects'"),
    ("6. Example Workflow", "Sample query processing for accounts payable defects"),
    ("7. Enhancement Guide", "How to add new query support and advanced features"),
    ("8. Troubleshooting", "Common issues and solutions"),
    ("9. Appendix", "References and download links")
]

for title, content in sections:
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, title, 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 7, content)
    pdf.ln(5)

# Add table for query examples
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Supported Queries:', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.cell(60, 7, 'Query Type', 1)
pdf.cell(60, 7, 'Example', 1)
pdf.cell(60, 7, 'Response', 1)
pdf.ln(7)

queries = [
    ("Defects due today", "\"defects due today\"", "Count + table of defects due today"),
    ("Module-specific", "\"module Inventory\"", "Defects in Inventory module"),
    ("Severity-based", "\"critical defects\"", "All critical defects")
]

for qtype, example, response in queries:
    pdf.cell(60, 7, qtype, 1)
    pdf.cell(60, 7, example, 1)
    pdf.cell(60, 7, response, 1)
    pdf.ln(7)

# Save the PDF
pdf.output("Defect_Analysis_Dashboard_Documentation.pdf")
print("PDF documentation generated successfully!")