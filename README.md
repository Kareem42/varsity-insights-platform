# Varsity Insights Platform

## Overview

A business intelligence web application modeling sports distribution analytics across 1,216 Texas school districts. This project generates and models sports participation data for Texas school districts, segmented by district type (charter, rural, urban/suburban). It uses Python for data generation and dbt for data transformation and modeling.

## Data Sources
- Texas Education Agency (TEA) district classification data
- Synthetic sports participation data modeled after 
  NFHS participation patterns

## Tech Stack
- Snowflake — cloud data warehouse
- dbt — data transformation layer
- Java Spring Boot — REST API
- React/TypeScript — frontend dashboard
- PostgreSQL — local development

## Architecture
Raw TEA district data → Snowflake RAW schema → 
dbt transformations → TRANSFORMED schema → 
Spring Boot API → React dashboard


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
