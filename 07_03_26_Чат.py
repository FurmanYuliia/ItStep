import tkinter as tk
from tkinter import scrolledtext

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
    write_chat(user_text)

# Натискання на Enter(клавіатура)
def on_enter(event):
    send_text()

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
tk.Button(bth_frame, text="Голос", width=15).pack(side="left", padx=5)
tk.Button(bth_frame, text="Вибір помічника", width=15).pack(side="left", padx=5)



entry.bind('<Return>', on_enter)

root.mainloop()