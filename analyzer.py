from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from models import FeedbackItem

def analyze_feedback(df):
    llm = ChatOpenAI(model="gpt-4o-mini")
    # Iterate through rows, call LLM, parse JSON
    return parsed_items
