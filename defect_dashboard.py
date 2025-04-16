import streamlit as st
import pandas as pd
from datetime import datetime

# Load dataset
df = pd.read_csv("defect_dataset_1000.csv", parse_dates=['Logged Date', 'Closed Date'])
df['Closed Date'].fillna(pd.Timestamp.today(), inplace=True)
df['Aging'] = (df['Closed Date'] - df['Logged Date']).dt.days

def answer_query(query):
    query = query.lower()
    
    if "defects due today" in query:
        today = pd.Timestamp.today().normalize()
        due_today = df[df['Closed Date'].dt.normalize() == today]
        return f"{len(due_today)} defects are due today.", due_today

    elif "accounts payable" in query or "account payable" in query:
        ap_related = df[df['Summary'].str.contains("account[s]? payable", case=False, na=False)]
        return f"Found {len(ap_related)} defects related to Accounts Payable.", ap_related

    elif "high severity open defects" in query:
        results = df[(df['Severity'].str.lower() == 'high') & (df['Status'].str.lower() == 'open')]
        return f"There are {len(results)} high severity open defects.", results

    elif "open defects" in query:
        open_defects = df[df['Status'].str.lower() == 'open']
        return f"There are {len(open_defects)} open defects.", open_defects

    elif "critical defects" in query:
        critical = df[df['Severity'].str.lower() == 'critical']
        return f"There are {len(critical)} critical defects.", critical

    elif "module" in query:
        module_name = query.split("module")[-1].strip()
        module_defects = df[df['Module'].str.lower().str.contains(module_name)]
        return f"Found {len(module_defects)} defects related to {module_name} module.", module_defects

    else:
        return "Sorry, I couldn't understand the query.", pd.DataFrame()

# Streamlit UI
st.title("🛠️ Defect Analysis Dashboard")

query = st.text_input("Ask a question about defects:")
if query:
    response, results = answer_query(query)
    st.write(response)
    if not results.empty:
        st.dataframe(results)

# Optional preset buttons
if st.button("Show defect aging chart"):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Aging'], bins=20, kde=True)
    plt.title("Defect Aging Distribution")
    plt.xlabel("Days Open")
    st.pyplot(plt)

if st.button("Show severity breakdown"):
    severity_counts = df['Severity'].value_counts()
    st.bar_chart(severity_counts)

if st.button("Show status breakdown"):
    status_counts = df['Status'].value_counts()
    st.bar_chart(status_counts)

# Download link
st.download_button("📥 Download Defect Data as CSV", data=df.to_csv(index=False), file_name="defect_dataset_1000.csv", mime='text/csv')
