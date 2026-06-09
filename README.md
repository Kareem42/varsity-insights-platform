# Varsity Insights Platform

A data platform for analyzing high school varsity sports participation across Texas school districts.

## Overview

This project generates and models sports participation data for Texas school districts, segmented by district type (charter, rural, urban/suburban). It uses Python for data generation and dbt for data transformation and modeling.

## Project Structure

```
varsity-insights-platform/
├── data/
│   └── raw/
│       ├── districts.csv             # Texas school district reference data
│       └── sports_participation.csv  # Generated participation data
├── scripts/
│   └── generate_participation.py     # Generates synthetic sports participation data
├── varsity_insights/                 # dbt project
│   ├── models/
│   ├── analyses/
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   └── tests/
└── dbt_project.yml
```

## Data

**Districts** (`data/raw/districts.csv`) — Texas school districts with TEA/NCES classification (charter, rural, urban, suburban).

**Sports Participation** (`data/raw/sports_participation.csv`) — Synthetic participation records for the 2023–2024 academic year across 15 sports and activities:

- Football, Basketball, Baseball, Softball, Soccer, Volleyball
- Track and Field, Swimming, Tennis, Golf, Cross Country, Wrestling
- Cheerleading, Band, Dance Team

Participation volume scales by district type:

| District Type | Sports Offered | Participants per Sport |
|---------------|----------------|------------------------|
| Charter       | 2–6            | 10–150                 |
| Rural         | 3–8            | 50–300                 |
| Other         | 6–12           | 100–800                |

## Setup

### Prerequisites

- Python 3.14+
- dbt

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install pandas
```

### Generate participation data

```bash
python scripts/generate_participation.py
```

Reads `data/raw/districts.csv` and writes `data/raw/sports_participation.csv`.

### Run dbt

```bash
dbt run
```

## dbt Project

The dbt project (`varsity_insights`) uses the `varsity_insights` profile. Models live under `varsity_insights/models/`.
