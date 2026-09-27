from pydantic import BaseModel

class FeedbackItem(BaseModel):
    text: str
    sentiment: str
    category: str
    priority: str
    summary: str
