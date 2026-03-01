import requests

URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY="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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = [{
    "role": "system",
    "content": "Ти - добрий викладач"
}]

print("Щоб завершити бесіду, напишіть: exit\nОберіть роль для AI:\n/1 - злий викладач\n/2 - співак\n/3 - веселий пірат\nЗараз AI - добрий :)")

while True:
    user = input("Ти: ")
    if user == "exit":
        break
    if user.startswith("/1"):
        messages = [{
            "role": "system",
            "content": "Ти - злий викладач"
        }]
        print("  Роль змінено. AI - злий викладач")
        continue
    if user.startswith("/2"):
        messages = [{
            "role": "system",
            "content": "Ти - співак"
        }]
        print("   Роль змінено. AI - співак")
        continue
    if user.startswith("/3"):
        messages = [{
            "role": "system",
            "content": "Ти - веселий пірат"
        }]
        print("  Роль змінено. AI - веселий пірат")
        continue
    messages.append({
        "role": "user",
        "content": user
    })

    payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1024
    }

    response = requests.post(URL, headers=headers, json=payload)
    answer = response.json()['choices'][0]['message']['content']
    messages.append({
        "role": "assistant",
        "content": answer
    })

    print(f" AI: {answer}")

