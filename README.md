# SpotMe Recommendation API

A FastAPI service for sports player recommendations, player/club data, and CV generation.

## Overview

This service exposes REST endpoints for managing players and clubs, generating recommendations, and building player CVs. It uses a SQLite database (`players.db`), repository/service layers, and seed scripts. An `AI_Plan.md` outlines planned AI services (search, filtering, ranking, recommendation, embedding, CV generation).

## Features

- Player and club CRUD APIs
- Recommendation endpoint
- SQLite database with seed data (`seed_players.py`)
- Layered architecture: API → repositories → database

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic

## Project Structure

```text
SpotMe.recomendtion/
├── app/
│   ├── main.py                 # FastAPI app + routers
│   ├── api/                    # player, club, recommendation routers
│   ├── database/               # connection, models, session, init_db
│   ├── repositories/           # data access layer
│   ├── schemas/                # Pydantic schemas
│   ├── models/                 # domain models
│   └── services/
├── seed_players.py
├── setup_project.py
├── clean_project.py
├── players.db
├── requirements.txt
└── AI_Plan.md
```

## Installation

```bash
git clone https://github.com/ahmedyasser1588/SpotMe.recomendtion.git
cd SpotMe.recomendtion
pip install -r requirements.txt
python seed_players.py
```

## Usage

```bash
uvicorn app.main:app --reload
```

## Project Status

In development — recommendation/CV API scaffold.

## Future Improvements

- Implement the ranking/embedding/recommendation services from `AI_Plan.md`
- Add tests
- Add environment-based configuration
