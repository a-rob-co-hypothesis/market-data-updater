# Stock Scraper Demo (Python)

## 📌 Project Overview
This repository demonstrates how to automatically fetch daily stock market data from different online sources (websites or APIs), clean the data, and update a local table (CSV or SQLite).  
The goal is to showcase **domain switching**: changing the data source simply by modifying a configuration file, without touching the business logic.

---

## ✅ Features (MVP)
- Fetch daily market data (price, volume, % change, etc.)  
- Supports multiple data sources:
    - APIs (preferred when available, e.g., Yahoo Finance API / `yfinance`)
    - Scraping public websites (HTML parsing) ⚠️ [See Notes](#notes)
- Clean and normalize retrieved data
- Update local tables (CSV or SQLite)
- Automatic deduplication (only insert new rows)
- Simple **source switching** via config file (`config.yml`)
- Logging + error handling (fallback to another source if the primary fails)

---

## 📂 Project Structure

    project-root/
    │
    ├─ config/              # Data sources list and scraping/API settings
    │   └─ config.yml
    │
    ├─ data/                # Generated dataset (CSV/SQLite)
    │   ├─ prices.csv
    │   └─ prices.sqlite
    │
    ├─ scraper/
    │   ├─ fetcher.py       # Source-agnostic data downloader (API or HTML)
    │   ├─ parser.py        # Cleans / normalizes data
    │   ├─ updater.py       # Updates CSV/SQLite tables
    │   └─ utils.py         # Logging, retries, helpers
    │
    ├─ demo.py              # Main demo script
    └─ README.md            # This file

---

## 🛠️ Tech Stack
| Component | Choice | Reason |
|----------|--------|--------|
| Language | Python 3.10+ | Lightweight, perfect for demos and data workflows |
| Parsing  | `beautifulsoup4` / `lxml` | HTML scraping |
| API      | `yfinance` / custom REST calls | Reliable and legal data access |
| Storage  | CSV or SQLite | Fast setup & easy demo usage |
| Data     | `pandas` | Table manipulation |
| Config   | `yaml` or `.env` | Domain switching without changing code |

---

## 🚀 How to Run

### 1. Install dependencies
    pip install -r requirements.txt

### 2. Edit data source / tickers
Edit `config/config.yml`:

    source: "yfinance"        # or "scraper"
    tickers: ["AAPL", "TSLA", "NVDA"]
    frequency: "daily"

### 3. Run the demo
    python demo.py

---

## ✨ Demo Workflow
1. Reads the configuration file `config.yml`
2. Fetches stock market data from the selected source
3. Normalizes the dataset
4. Updates the local table
5. Logs:

        Ticker NVDA updated: +1 row (2025-11-07)
        Source A failed → fallback to source B

---

## 🧩 Extend the project
- Add asynchronous fetching (`aiohttp`)
- Visual dashboard with Streamlit
- Automate execution via cron/Task Scheduler
- Export to PostgreSQL or time-series DB

---

## ⚠️ Notes
- ⚠️ HTML scraping is **not yet implemented**.  

---

## 📄 License
MIT — free to use, modify, and distribute.
