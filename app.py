import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# Page Title
# ---------------------------------
st.title("IAM Security Metrics Dashboard (Simulation)")

# ---------------------------------
# Load Data
# ---------------------------------
users = pd.read_csv("data/users.csv")
violations = pd.read_csv("data/violations.csv")
roles = pd.read_csv("data/roles.csv")

# =================================
# 1. Company People Overview
# =================================
st.header("Company People Overview")

st.metric("Total Users in Organization", len(users))

dept_counts = users["department"].value_counts()

fig1, ax1 = plt.subplots()
dept_counts.plot(kind="bar", ax=ax1)
ax1.set_title("Users by Department")
ax1.set_xlabel("Department")
ax1.set_ylabel("Number of Users")

st.pyplot(fig1)
st.dataframe(users)

# =================================
# 2. High Privilege Accounts
# =================================
st.header("High Privilege Accounts")

high_priv_users = users[users["privilege_level"] == "High"]

st.metric("Total High Privilege Users", len(high_priv_users))

priv_dept_counts = high_priv_users["department"].value_counts()

fig2, ax2 = plt.subplots()
priv_dept_counts.plot(kind="bar", ax=ax2)
ax2.set_title("High Privilege Users by Department")
ax2.set_xlabel("Department")
ax2.set_ylabel("Number of Users")

st.pyplot(fig2)
st.dataframe(high_priv_users)

# =================================
# 3. Access Violations
# =================================
st.header("Access Violations")

st.metric("Total Violations", len(violations))
st.metric(
    "High Severity Violations",
    len(violations[violations["severity"] == "High"])
)

violation_counts = violations["severity"].value_counts()

fig3, ax3 = plt.subplots()
violation_counts.plot(kind="bar", ax=ax3)
ax3.set_title("Violations by Severity")
ax3.set_xlabel("Severity")
ax3.set_ylabel("Count")

st.pyplot(fig3)
st.dataframe(violations)

# =================================
# 4. Role Distribution
# =================================
st.header("Role Distribution")

role_counts = users["role"].value_counts()

fig4, ax4 = plt.subplots()
role_counts.plot(kind="bar", ax=ax4)
ax4.set_title("Role Distribution Across Users")
ax4.set_xlabel("Role")
ax4.set_ylabel("Number of Users")

st.pyplot(fig4)
