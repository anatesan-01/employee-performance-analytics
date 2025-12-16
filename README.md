# 📊 Employee Performance & Salary Insights  
### Portfolio Project – Data Visualization using Python

---

## 📌 Project Summary

This portfolio project demonstrates how **data visualization techniques** can be used to analyze **employee performance, salary trends, promotions, productivity, experience, and sales metrics** in a simulated corporate environment.

The project focuses on **exploratory data analysis (EDA)** and **visual storytelling** to convert raw employee data into meaningful business insights.

---

## 🎯 What This Project Demonstrates

Through this project, the following skills are demonstrated:

- Translating **business requirements** into analytical questions  
- Selecting appropriate **visualizations** for different data scenarios  
- Interpreting charts to extract **clear and unbiased insights**  
- Communicating results in a **professional and structured format**  
- Building **review-ready metrics** using Python

---

## 🧩 Business Context

An organization requires a **data visualization–based review** to understand workforce patterns related to:

- Salary distribution and compensation trends  
- Promotion and increment consistency  
- Experience and productivity behavior  
- Sales performance across employees  

This analysis supports **decision-making** before implementing final dashboards in BI tools.

---

## 🗂 Dataset Overview

The dataset contains employee-level information, including:

- Salary  
- Final incremented salary  
- Increment percentage  
- Promotion status  
- Years of experience  
- Productivity time (hours)  
- Sales performance  

> **Note:**  
> Some null values are present in the dataset. Data cleaning was intentionally limited to focus on **visual analysis and insight generation**, aligning with a review-stage analytics approach.

---

## ❓ Key Analytical Questions

This project answers the following questions using **data visualization**:

1. **How are salaries distributed across employees?**  
2. **How does promotion status influence salary levels?**  
3. **How consistent are increment percentages across the workforce?**  
4. **How does experience relate to salary growth?**  
5. **What does the experience distribution of the workforce look like?**  
6. **How does productivity time relate to sales performance?**  
7. **Are there standout performers at similar experience levels?**  
8. **How do experience, sales, and productivity interact simultaneously?**  
9. **What are the key workforce KPIs for management review?**

---

## 📈 Visualizations Used

The following visualizations were created to answer the business questions:

- **Histogram** – Salary and experience distribution  
- **Bar Chart** – Salary comparison by promotion status  
- **Box Plot** – Increment percentage variability  
- **Line Chart** – Experience vs productivity trends  
- **Scatter Plot** – Productivity vs sales relationship  
- **Bubble Chart (Plotly)** – Experience vs sales with productivity context  
- **KPI Cards (Streamlit)** – Summary performance metrics  

Each visualization is purpose-driven and directly mapped to a business question.

---

## 🛠 Tools & Technologies

- **Python**  
- **Pandas** – Data manipulation  
- **Matplotlib & Seaborn** – Static visualizations  
- **Plotly** – Interactive visualizations  
- **Streamlit** – KPI dashboard  
- **Jupyter Notebook / Python Scripts**

---

## 🔄 Project Workflow

1. Understanding the business problem  
2. Exploring the dataset structure  
3. Performing exploratory data analysis (EDA)  
4. Creating meaningful visualizations  
5. Extracting insights from charts  
6. Summarizing key performance indicators  

---

## 📌 Key Learnings

- Data visualization is effective for identifying workforce patterns quickly  
- Promotion status and experience strongly influence salary trends  
- Productivity plays a key role in differentiating sales performance  
- Experience alone does not guarantee higher productivity or sales  
- Careful wording is essential when interpreting visual insights  

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
streamlit run Dashboard.py
