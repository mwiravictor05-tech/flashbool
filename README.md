FeedbackLoop AI

Automated Customer Sentiment & Action Item Engine

FeedbackLoop AI solves the "data noise" problem for product teams. Instead of manually reviewing thousands of unstructured support tickets, reviews, and transcripts, our tool uses LLMs to instantly categorize, summarize, and prioritize feedback.

🚀 The Problem
Product teams are overwhelmed by unstructured data spread across multiple platforms. Insights are often buried, leading to missed bugs and misaligned feature roadmaps.

💡 The Solution
FeedbackLoop AI automates the analysis pipeline:
Ingestion: Processes raw text data (CSV/Manual Input).
Analysis: Uses LLMs to extract sentiment, category, summary, and priority.
Visualization: A streamlined Streamlit dashboard that visualizes the feedback in a Kanban-style board for instant action.

🛠️ Tech Stack
Language: Python
Orchestration: LangChain
Data Validation: Pydantic
Dashboard: Streamlit
AI Engine: OpenAI GPT-4o-mini

📥 Getting Started

Prerequisites
Python 3.9+
pip install -r requirements.txt
An OpenAI API Key

Running the App
1.Clone the repository.
2.Set your API Key: export OPENAI_API_KEY='your-key-here'
3.Launch the dashboard:
bashCopy

📈 Roadmap
API Connectors: Direct integrations with Zendesk and Jira.
Action Engine: Automated Jira ticket creation from high-priority insights.
Comparative Analytics: Cross-segment feedback analysis.

