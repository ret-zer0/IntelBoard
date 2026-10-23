# IntelBoard

**IntelBoard** is a lightweight web dashboard designed to bring the day's important information into one convenient place. It combines news updates, interesting GitHub repositories, and weather information through three dedicated navigation sections: **News, GitHub, and Weather**.

Instead of switching between multiple websites to stay informed, IntelBoard provides a unified interface where users can quickly explore current events, discover developer projects, and check local weather conditions.

## Features

### News
- Fetch recent headlines from selected RSS news feeds.
- Display article titles, summaries, publication dates, and source names.
- Provide direct links to original articles for further reading.
- Bring updates from multiple sources into one section.

### GitHub
- Explore interesting and trending repositories.
- View repository descriptions, programming languages, and star counts.
- Discover projects and tools from across the developer community.

### Weather
- View current weather conditions for a selected location.
- Access forecast information to get a quick overview of upcoming weather.
- Keep useful weather details available alongside daily news and technology updates.

### User Interface
- Three dedicated navigation sections for straightforward browsing.
- A clean, modern dashboard designed for everyday use.
- Data refresh functionality to retrieve updated information.
- A unified layout that keeps the experience simple and focused.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Flask | Web server and application routing |
| HTML | Dashboard structure |
| CSS | Layout, styling, and visual design |
| JavaScript | Frontend interactions and dynamic updates |
| Feedparser | Reading and parsing RSS feeds |
| Requests | Fetching data from public APIs |

## Getting Started

### Prerequisites
- Python 3 installed on your system
- Internet connection to retrieve external data

### Installation

1. Clone the repository:

   ```bash
   git clone "https://github.com/ret-zer0/IntelBoard"
   cd IntelBoard
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open the local URL displayed in your terminal in your web browser.

## Project Structure

```text
IntelBoard/
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── .gitignore
├── app.py
├── news.py
├── git.py
├── requirements.txt
├── weather.py
└── README.md
```

## Project Purpose

IntelBoard was built to make daily information easier to access through a single, organized dashboard. The project brings together world news, developer activity, and weather updates while keeping the implementation lightweight and practical.

It also serves as a hands-on project in Python web development, API integration, RSS feed processing, and frontend design.

## Future Improvements

Potential improvements include adding more configurable news sources, expanding repository discovery options, and providing additional weather details.
