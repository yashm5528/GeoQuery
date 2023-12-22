from langchain_community.utilities import SQLDatabase, SQLDatabaseToolkit
from langchain_community.llm import OpenAI
import requests

# Connect to the SQLite database
db = SQLDatabase.from_uri("sqlite:///home/student/capstone_implementation/GeoQuery/GeoQuery.db")
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

# Prepare the OpenAI API call
openai_url = "http://localhost:8000/v1/chat/completions"
openai_payload = {
    "model": "llama",
    "messages": [{"role": "user", "content": "Name all cities in the state alaska"}],
    "max_tokens": 30,
    "top_p": 0.9,
    "temperature": 0.9,
    "stop": ["\n"]
}

# Make the OpenAI API call
openai_response = requests.post(openai_url, json=openai_payload)
openai_result = openai_response.json()

# Use the result as input for the SQLDatabaseToolkit
sql_toolkit_response = toolkit.process(openai_result)

# Print the final response
print(sql_toolkit_response)