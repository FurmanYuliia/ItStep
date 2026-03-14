import tkinter as tk
from tkinter import scrolledtext
import requests
import threading
import time

import speech_recognition as sr
import sounddevice as sd
import tempfile
import scipy.io.wavfile as wav

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

# Відправлення питання та повертання(вивод) відповіді
def ask_ai(user_text):
    messages.append({
        "role": "user",
        "content": user_text
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
    return answer

# Виведення "..."
#  ask_ai
#   Виведення відповіді
def write_answer(user_text):
    time.sleep(0.6)  # затримка на 0.6 с
    write_chat("AI:  ...")
    answer = ask_ai(user_text) # запит може тривати декілька секунд

    # Видаляємо "AI:  ..."
    chat.config(state="normal")
    chat.delete("end-2l", "end-1l")
    chat.config(state="disabled")
    chat.see(tk.END)
    if not user_text:
        return
    write_chat(f"AI: {answer}")


# Вивід текста в чат
def write_chat(text):
    chat.config(state="normal")
    chat.insert(tk.END, text + "\n")
    chat.config(state="disabled")
    chat.see(tk.END)

# Натискання на кнопку Enter
def send_text():
    user_text = entry.get().strip()
    entry.delete(0, tk.END)
    if not user_text:
        return
    write_chat(f"— {user_text}")
    threading.Thread(
        target=write_answer,
        args=(user_text,),
        daemon=True
    ).start()

# Натискання на Enter(клавіатура)
def on_enter(event):
    send_text()

# Голос
def voice_input():
    """
    Запис голосу → WAV → розпізнавання → AI
    """

    recognizer = sr.Recognizer()

    duration = 5  # Тривалість запису (сек)
    sample_rate = 44100  # Частота дискретизації

    write_chat("🎤 Говори...")

    # Запис аудіо з мікрофона
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    sd.wait()  # Чекаємо завершення запису

    # Створюємо тимчасовий WAV-файл
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wav.write(f.name, sample_rate, recording)

        # Завантажуємо WAV у speech_recognition
        with sr.AudioFile(f.name) as source:
            audio = recognizer.record(source)

    try:
        # Розпізнавання української мови
        text = recognizer.recognize_google(audio, language="uk-UA")

        write_chat(f"— (голос): {text}")

        threading.Thread(
            target=write_answer,
            args=(text,),
            daemon=True
        ).start()

    except sr.UnknownValueError:
        write_chat("❌ Не вдалося розпізнати голос")

    except sr.RequestError:
        write_chat("❌ Помилка сервісу розпізнавання")

def voice():
    threading.Thread(
        target=voice_input,
        daemon=True
    ).start()

# UI - зовнішній вигляд / інтерфейс
root = tk.Tk()
root.title("AI Chat")
root.geometry("450x600")

chat = scrolledtext.ScrolledText(root, wrap="word", font=("Arial", 12), state="disabled")
chat.pack(padx=10, pady=10, fill="both", expand=True)


entry = tk.Entry(root, font=("Arial", 12))
entry.pack(fill="x", padx=10)

bth_frame= tk.Frame(root)
bth_frame.pack(pady=10)

tk.Button(bth_frame, text="Enter", width=15, command=send_text).pack(side="left", padx=5)
tk.Button(bth_frame, text="Голос", width=15, command=voice).pack(side="left", padx=5)
tk.Button(bth_frame, text="Вибір помічника", width=15).pack(side="left", padx=5)



entry.bind('<Return>', on_enter)

root.mainloop()