import requests

url = "http://localhost:8000/v1/chat/completions"
payload = {
    "model": "llama",
    "messages": [{"role": "user", "content": "Hello there!"}],
    "max_tokens": 30,
    "top_p": 0.9,
    "temperature": 0.9,
    "stop": ["\n"]
}
response = requests.post(url, json=payload)
print(response.json())

# Output:
# {'id': 'chatcmpl-da87a0b1-0f20-4e10-b731-ba483e13b450', 'object': 'chat.completion', 'created': 1689868843, 'model': 'D:/llama-api/models/gptq/orca_mini_7b', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': " Hi there! Sure, I'd be happy to help you with that. What can I assist you with?"}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 11, 'completion_tokens': 23, 'total_tokens': 34}}