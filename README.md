# Data Engineering Experiments

This repository contains a diverse set of data engineering experiments demonstrating ETL, analytics, CI/CD, Dockerization, cloud integrations, language comparisons, and more, using Python, Rust, and modern tools.

---

## 📂 Subproject Summaries

---

### 1. **arko-sqlite-lab**
- **Purpose:** CLI tool for interacting with SQLite databases.
- **Highlights:** ETL from CSV → SQLite, CRUD operations, custom queries (like 5-day close % change), unit tests, Docker/devcontainer support, CI/CD.
- **Get Started:** `main.py` is the CLI entrypoint. ETL is modularized in `mylib/`.

---

### 2. **arko_bhattacharya_pandas_descriptives**
- **Purpose:** Descriptive statistics and data visualization with Pandas.
- **Highlights:** MapBan dataset analysis, visualization generation, profile report as CI/CD artifact, Docker-worker pipeline for automation.
- **Get Started:** Notebooks and scripts under `scripts/`, CI/CD deploys on push.

---

### 3. **arko_bhattacharya_week1**
- **Purpose:** Python project template with data tasks.
- **Highlights:** Array operations with numpy, pandas DataFrame, CSV export, dockerization, GitHub Actions for CI/CD.
- **Get Started:** Follow scaffold; main logic under `src/`.

---

### 4. **arko_complex_query**
- **Purpose:** CLI for performing complex SQL on Databricks tables.
- **Highlights:** CRUD and advanced window queries on AAPL table (uses SQL API), modular ETL, default query computes price statistics.
- **Get Started:** Run `main.py` for menu-driven CLI; functions detailed in README.

---

### 5. **arko_databricks_pipeline**
- **Purpose:** End-to-end ELT pipeline demonstration on Databricks.
- **Highlights:** Extracts CSVs to DBFS, loads as inbound table, transforms and stages into final processed reporting table, with CI/CD automation.
- **Get Started:** Workflows described in README; source code in `modules/`.

---

### 6. **arko_dockerized_app**
- **Purpose:** Simple calculator REST API web app.
- **Highlights:** Built with Flask and Docker, supports basic arithmetic via endpoints, auto-builds/test/push with GitHub Actions.
- **Get Started:** `app.py`, run locally or as Docker container. API details in README.

---

### 7. **arko_github_actions_matrix_build**
- **Purpose:** Compare performance/statistics in Pandas vs. Polars.
- **Highlights:** Jupyter notebooks for both libraries, notebook runtime comparison via script, test matrix across Python versions using GitHub Actions.
- **Get Started:** Notebooks in root, scripts for benchmarking in `lib/`, results visualized in `plots/`.

---

### 8. **arko_individual_project_1**
- **Purpose:** Statistical analysis with Polars and Pandas.
- **Highlights:** Two separate notebooks, helper function library, runtime comparison, similar to GitHub Actions Matrix Build but single-user focus.
- **Get Started:** See notebooks and main script for comparison/plots.

---

### 9. **arko_individual_project_2**
- **Purpose:** ETL CLI for AAPL stock data using Rust.
- **Highlights:** Extract, transform, load / query Apple stock data (CSV → SQLite) via a Rust CLI; default and custom queries; automated Rust binary artifact in CI/CD.
- **Get Started:** Rust CLI docs, entrypoint in `src/main.rs`, test suite included.

---

### 10. **arko_python_to_rust**
- **Purpose:** Benchmark Rust vs. Python for AAPL CSV analysis.
- **Highlights:** Compares speed and memory (Polars in Rust/Pandas in Python), reports with metrics and plots, Docker/Rust/CICD setup for reproducibility.
- **Get Started:** See README for make commands that run both and compare outputs.

---

> _Note: Some additional subfolders could not be summarized here due to access limitations, but most follow the same principles—isolated, reproducible, modular experiments illustrating advanced data engineering and automation practices._

---

**Feel free to edit or extend as needed!**
