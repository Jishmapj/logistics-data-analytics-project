# Logistics Data Science Internship: Supply Chain Analytics & Optimization

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green.svg)
![Status](https://img.shields.io/badge/Phase%201-Completed-success.svg)

This repository contains the end-to-end deliverables, code, and analytical documentation for the **Logistics & Supply Chain Data Science Internship**. 

---

## Repository Structure

```text
├── Cleaned_Data/
│   ├── Cleaning_Report.csv                    # Summary audit of data cleaning and record retention
│   ├── inventory_cleaned.csv                  # Multi-warehouse inventory stock, ROP, and reserved units
│   ├── order items_cleaned.csv                # Itemized order line items, quantities, and line totals
│   ├── Orders (2)_cleaned.csv                 # Customer order header details, destination cities, status
│   ├── products (1)_cleaned.csv               # Product catalog, categories, manufacturing costs, SKU info
│   └── shipping table_cleaned.csv             # Carrier shipments, transit dates, freight costs, status
├── Week_1_Strategic_Planning_Report.docx      # Comprehensive Strategic Planning Report (DOCX deliverable)
├── Week_1_Strategic_Planning_Report.md        # Full Strategic Planning Report in GitHub Markdown
├── week_1_data_exploration.py                 # Automated data ingestion, KPI computation, EDA & baseline ML
├── generate_phase1_report.py                  # DOCX generation script
├── docx_builder.py                            # Custom OpenXML DOCX builder module
├── carrier_transit_cost_analysis.png          # Carrier latency vs. shipping cost comparison plot
├── warehouse_inventory_status.png             # Multi-hub inventory holding and safety stock distribution
├── order_value_distribution.png               # Order line total revenue distribution histogram
└── README.md                                  # Repository overview and documentation
```

---

## Phase 1 Overview: Strategic Planning and Data Exploration

### Objective
Simulate the strategic planning and data exploration phase of a multi-echelon enterprise logistics network. The project defines a realistic operational scenario (**OmniFlow Logistics**), formulates key supply chain performance indicators (KPIs), synthesizes literature on supply chain theories and machine learning in freight operations, and outlines a six-stage data science roadmap.

### Key Metrics & Findings from Cleaned Data
* **Total Sales Revenue:** $88,770.46 (across 899 orders)
* **Total Freight Spend:** $48,698.19 (across 3,481 shipments)
* **Freight-to-Revenue Ratio:** **54.86%** (Urgent strategic optimization needed; healthy target is 8–15%)
* **Carrier Speed vs. Cost Dynamics:**
  * **Purolator (Express):** 2.0-day transit at $19.99/order
  * **UPS (Expedited):** 3.0-day transit at $14.99/order
  * **Canada Post (Standard):** 7.0-day transit at $9.99/order
  * **FedEx (Standard):** 8.0-day transit at $11.99/order
  * **DHL (Standard):** 9.0-day transit at $12.99/order
* **Multi-Warehouse Holdings:** 56,229 units on hand across 5 distribution hubs (Toronto, Calgary, Chicago, Edmonton, Vancouver) with zero active stockouts.

---

## How to Run the Phase 1 Code

### 1. Run Data Exploration & KPI Engine
```bash
python week_1_data_exploration.py
```
This executes:
1. Multi-table schema ingestion and data audit.
2. Automated KPI calculation (carrier transit days, inventory buffers, freight-to-revenue ratio).
3. Generation of three high-resolution charts (`.png`).
4. Baseline Ordinary Least Squares (OLS) regression predicting transit latency ($R^2 = 0.9995$).

### 2. Re-generate the Word Document Report
```bash
python generate_phase1_report.py
```
This script rebuilds the formatted Word document: `Week_1_Strategic_Planning_Report.docx`.

---

## Git & GitHub Setup Instructions

To push this project to your GitHub repository:

```bash
# 1. Initialize git in the root folder
git init

# 2. Add all cleaned files and deliverables
git add .

# 3. Commit Phase 1 deliverables
git commit -m "Complete Phase 1: Strategic Planning and Data Exploration in Logistics"

# 4. Link to your GitHub remote repository (replace with your repo URL)
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git

# 5. Push to GitHub
git push -u origin main
```

---

## Next Steps: Phase 2 Preview
* **Relational Schema Reconciliation:** Harmonizing Master Product SKU catalog with warehouse inventory line items.
* **Feature Engineering:** Geospatial route distances, carrier reliability indices, and delivery delay classification flags.
* **Prescriptive Modeling:** Mixed-Integer Linear Programming for cost-optimal carrier dispatching.
