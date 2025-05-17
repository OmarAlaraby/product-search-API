# Product Search API

## Project Overview

[![Project Demo Video](https://img.shields.io/badge/Watch-Demo_Video-blue?style=for-the-badge&logo=googledrive)](https://drive.google.com/file/d/1y4wiK_4s53GdPQ2w3l5J86905Pl61TSP/view?usp=sharing)

This API provides advanced product search capabilities with the following features:
- Multi-language search support through DeepL translation
- Automatic spelling correction for search terms
- Filtering by various product attributes (vegan, gluten-free, calories, etc.)
- Product categorization and brand filtering

## Installation Guide

### Prerequisites
- Python 3.8+
- Poetry (Python package manager)
- Redis server (for caching)

### Step 1: Install Prerequisites

#### Install Python 3.8+
Make sure you have Python 3.8 or higher installed:
```bash
python --version
```

#### Install Poetry
If you don't have Poetry installed, run:
```bash
# For Linux/macOS/WSL
curl -sSL https://install.python-poetry.org | python3 -

# For Windows PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Verify your installation:
```bash
poetry --version
```

#### Install Redis Server
Redis is required for caching in this application:

```bash
# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install redis-server
sudo systemctl enable redis-server
sudo systemctl start redis-server

# For macOS using Homebrew
brew install redis
brew services start redis

# For Windows
# Download and install from https://github.com/tporadowski/redis/releases
```

Verify Redis is running:
```bash
redis-cli ping
# Should return "PONG"
```

### Step 2: Clone the Repository
```bash
git clone https://github.com/OmarAlaraby/product-search-API.git
cd product-search-API
```

### Step 3: Install Dependencies
```bash
poetry install
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory, see the `.env.example` file

### Step 5: Start the Development Server
```bash
poetry run python manage.py runserver
```

## API Documentation

Once the server is running, you can access the Swagger API documentation:
- Visit [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

## API Features

- **Product Search**: Search across product names, descriptions, ingredients, and more
- **Translation**: Automatically translates search queries for multi-language support
- **Spelling Correction**: Corrects typos in search queries to improve results
- **Filtering**: Filter products by various attributes:
  - Dietary preferences (vegan, gluten-free)
  - Brands
  - Categories
  - Nutritional information (calories, etc.)

## Technology Stack

- Django
- Django REST Framework
- DeepL API for translations
- Redis
- PostgreSQL