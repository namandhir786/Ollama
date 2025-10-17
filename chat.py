
import requests
import json

def call_ollama_chat():
    url = "http://localhost:11434/api/chat"

    user_input = "Explain the symptoms and remedies for headache."

    payload = {
        "model": "llama3.2:1b",
        "messages": [
            {"role": "system", "content": "You are a helpful nurse."},
            {"role": "user", "content": user_input}
        ]
    }

    print("\n--- Model Response ---\n")

    try:
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()

            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode("utf-8"))
                    if "message" in data:
                        print(data["message"]["content"], end="", flush=True)
                    elif "error" in data:
                        print(f"\n Error from model: {data['error']}")

    except requests.exceptions.RequestException as e:
        print(f"\n Request failed: {e}")
        print(" Make sure Ollama is running with `ollama serve`.")

if __name__ == "__main__":
    call_ollama_chat()
