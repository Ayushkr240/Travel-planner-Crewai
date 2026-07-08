# AI Travel Planner using CrewAI

An AI-powered travel planning system built with **CrewAI** that generates a personalized **7-day travel itinerary** based on a user's travel budget.

Instead of using a single AI model to handle every task, this project follows a **multi-agent architecture** where specialized AI agents collaborate to recommend a destination, discover attractions, suggest hotels, and generate a complete travel plan.

---

## Overview

Planning a trip involves several decisions, including choosing a destination, finding places to visit, selecting accommodation, and organizing a daily schedule. This project automates that entire workflow using multiple AI agents working together.

Each agent is responsible for a specific task and passes its output to the next agent, creating a structured and modular planning process.

---

## Features

* Budget-based destination recommendation
* Tourist attraction discovery
* Budget-friendly hotel recommendations
* Automatic 7-day itinerary generation
* Weather information
* Restaurant suggestions
* Packing recommendations
* Budget breakdown
* Markdown itinerary export
* Modular multi-agent workflow

---

# Architecture

```text
                     User Budget
                          │
                          ▼
               City Finder Agent
                          │
                          ▼
              Place Finder Agent
                          │
                          ▼
              Hotel Finder Agent
                          │
                          ▼
                 Planner Agent
                          │
                          ▼
          Complete 7-Day Travel Itinerary
```

---

# How It Works

### Step 1 — User Input

The user provides a travel budget.

Example:

```text
₹20,000
```

---

### Step 2 — City Finder Agent

The City Finder Agent analyzes the available budget and identifies the most suitable destination.

**Responsibilities**

* Recommend a destination
* Consider affordability
* Select a travel-friendly city

---

### Step 3 — Place Finder Agent

Once the destination is selected, the Place Finder Agent searches for popular attractions and activities.

Example output:

* Historical landmarks
* Museums
* Parks
* Local markets
* Cultural attractions

---

### Step 4 — Hotel Finder Agent

This agent recommends hotels that fit within the user's budget.

It focuses on:

* Affordable accommodation
* Convenient location
* Good overall value

---

### Step 5 — Planner Agent

The Planner Agent combines the outputs from all previous agents and creates a complete travel itinerary.

The generated itinerary includes:

* Day-wise travel plan
* Places to visit
* Hotel recommendation
* Estimated budget
* Weather information
* Restaurant suggestions
* Packing tips

The final itinerary is saved as a Markdown file.

---

# Agents

## City Finder Agent

Finds the best destination according to the user's budget.

---

## Place Finder Agent

Discovers popular attractions and activities in the selected destination.

---

## Hotel Finder Agent

Recommends budget-friendly hotels based on the selected city.

---

## Planner Agent

Creates the final itinerary by combining the outputs from all previous agents.

---

# Tech Stack

* Python
* CrewAI
* Google Gemini Flash API
* SerperDevTool

---

# Project Structure

```text
crewai-travel-planner/
│
├── src/
│   └── travel_agent_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│       ├── main.py
│       └── tools/
│
├── knowledge/
├── output/
├── tests/
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/crewai-travel-planner.git
```

Move into the project directory.

```bash
cd crewai-travel-planner
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

or, if using **uv**:

```bash
uv sync
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

---

# Running the Project

```bash
crewai run
```

or

```bash
python src/travel_agent_crew/main.py
```

(depending on your CrewAI project setup)

---

# Example Workflow

```text
User Budget
      │
      ▼
Destination Selected
      │
      ▼
Tourist Attractions Found
      │
      ▼
Hotels Recommended
      │
      ▼
7-Day Travel Itinerary Generated
```

---

# Future Improvements

* Flight recommendations
* Train and bus suggestions
* Multiple destination support
* Google Maps integration
* Interactive web interface
* Real-time weather updates
* Expense optimization
* Personalized travel preferences
* PDF itinerary export
* Calendar integration

---

# What I Learned

This project helped me gain practical experience with:

* Multi-agent AI systems
* CrewAI orchestration
* Sequential task execution
* Prompt engineering
* Tool integration
* Modular AI application design
* LLM-powered automation

---

# Contributing

Contributions, ideas, and improvements are always welcome. Feel free to fork the repository, open an issue, or submit a pull request.

---

# License

This project is licensed under the MIT License.
