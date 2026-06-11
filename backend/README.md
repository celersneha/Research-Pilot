# Research-Pilot

A simple multi-agent research app built with Streamlit and LangChain. It takes a research topic, searches for recent information, scrapes a relevant source, drafts a report, and provides critic feedback.

## Features

- Enter a research topic in the UI
- Run a multi-step research pipeline
- View search results and scraped content
- Generate a final report and critic feedback
- Download the report as Markdown

## Setup

1. Go to the backend folder:
   cd backend
2. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate # macOS/Linux
   .\.venv\Scripts\activate # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Create a .env file and add your API keys:
   TAVILY_API_KEY=your_key
   GROQ_API_KEY=your_key
   MISTRAL_API_KEY=your_key
5. Start the app:
   streamlit run app.py

## Tech Stack

- Python
- Streamlit
- LangChain
- Tavily API
- Groq / Mistral models
- BeautifulSoup
- python-dotenv

## Notes

- The app uses the backend environment for running the research pipeline.
- Make sure your API keys are set before launching the app.
