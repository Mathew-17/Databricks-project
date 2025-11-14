# End-to-End Data Engineering Pipeline on Databricks

This project showcases a complete data engineering pipeline built on Databricks using PySpark and the Medallion Architecture. It ingests raw data into the Bronze layer, applies cleaning and transformation logic in the Silver layer, and produces analytics-ready fact and dimension tables in the Gold layer for reporting and dashboarding.

The pipeline demonstrates industry-standard data engineering practices, including schema enforcement, incremental processing, deduplication, data quality checks, and modular transformation logic.

---

## 🚀 Features

- Raw data ingestion into Delta Lake (Bronze)
- Data cleaning, standardization, and deduplication (Silver)
- Aggregated business views and dimensional modeling (Gold)
- PySpark transformation pipelines
- Delta Lake ACID transactions and time travel
- Notebook-based workflow with clear modular steps
- Scalable Medallion Architecture for real-world data platforms

---

## 🧱 Architecture (Medallion Model)

### **Bronze Layer**
- Stores raw ingested data as-is
- Handles schema definition and ingestion logic

### **Silver Layer**
- Cleans and transforms data
- Handles:
  - Null value treatment  
  - Deduplication  
  - Type casting  
  - Standardization  

### **Gold Layer**
- Final curated business tables
- Fact & dimension tables optimized for analytics
- Used by BI tools or ML pipelines

---

## 🛠️ Tech Stack

- Databricks (Spark + Delta Lake)
- PySpark
- Delta Tables
- Databricks Notebooks
- SQL for analytics/modeling
- GitHub for version control

---

## 📂 Project Structure

