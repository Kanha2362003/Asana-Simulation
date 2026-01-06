# Asana Workspace Simulation (Enterprise Seed Data Generator)

## 📌 Overview
This project simulates a **realistic enterprise-scale Asana workspace** for a B2B SaaS company with approximately **5,000–10,000 employees**.  
It models how cross-functional teams use Asana for **product development, marketing, and operations workflows**, and generates a high-fidelity **SQLite database** populated with realistic synthetic data.

The primary goal of this project is to demonstrate **data realism, methodological rigor, and clean system design**, closely reflecting real-world Asana usage patterns.

---

## 🎯 Objectives
- Design a production-grade relational schema for an Asana-like system
- Generate realistic synthetic data with appropriate edge cases
- Ensure strong temporal and relational consistency
- Build a fully runnable, modular data generation pipeline
- Produce a database suitable for analytics, testing, and case studies

---

## 🧱 What This Project Includes
- **Relational database schema** (`schema.sql`)
- **Documented seed data methodology** (design decisions and distributions)
- Modular **Python-based data generators**
- A fully populated **SQLite database**
- Documentation of **real-world inspirations and LLM prompt templates**

---

### 🗂️ Project Structure
asana-simulation/
├── README.md
├── requirements.txt
├── schema.sql
├── .gitignore
├── src/
│ ├── main.py
│ ├── generators/
│ │ ├── organizations.py
│ │ ├── users.py
│ │ ├── teams.py
│ │ ├── projects.py
│ │ ├── sections.py
│ │ ├── tasks.py
│ │ ├── comments.py
│ │ ├── custom_fields.py
│ │ ├── tags.py
│ │ └── attachments.py
│ └── utils/
│ ├── db.py
│ ├── dates.py
│ ├── uuid.py
│ └── text.py
├── prompts/
│ └── task_generation.txt
├── scrapers/
│ └── sources.md
└── output/
└── asana_simulation.sqlite
---

## ⚙️ Setup & Execution

### 1️⃣ Install Dependencies
``` bash
pip install -r requirements.txt
2️⃣ Run the Data Generator

python src/main.py

3️⃣ Output
After successful execution, the generated database will be available at:

output/asana_simulation.sqlite
