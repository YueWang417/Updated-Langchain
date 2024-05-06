from dotenv import load_dotenv
import os

load_dotenv()  # Ensure this is the first thing you do related to env variables

print("OPENAI_API_KEY from environment:", os.getenv("OPENAI_API_KEY"))
print("LANGCHAIN_API_KEY from environment:", os.getenv("LANGCHAIN_API_KEY"))
