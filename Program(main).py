import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
import random

class GrammarCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Перевірка граматики")

        self.text_area = scrolledtext.ScrolledText(self.root, width=60, height=20, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10)

        self.check_button = tk.Button(self.root, text="Перевірити граматику", command=self.check_grammar)
        self.check_button.pack(pady=5)

        self.test_button = tk.Button(self.root, text="Тестування", command=self.run_test)
        self.test_button.pack(pady=5)

        self.api_url = "https://languagetool.org/api/v2/check"

    def check_grammar(self):
        text = self.text_area.get(1.0, tk.END)
        params = {
            'text': text,
            'language': 'uk-UA'
        }
        response = requests.post(self.api_url, data=params)
        if response.status_code == 200:
            data = response.json()
            if data and 'matches' in data:
                error_messages = [error['message'] for error in data['matches']]
                if error_messages:
                    messagebox.showerror("Помилки граматики", "\n".join(error_messages))
                else:
                    messagebox.showinfo("Перевірка граматики", "Помилок граматики не знайдено!")
            else:
                messagebox.showinfo("Перевірка граматики", "Помилок граматики не знайдено!")
        else:
            messagebox.showerror("Помилка", "Не вдалося підключитися до служби перевірки граматики.")

    def generate_random_text(self):
        num_words = random.randint(5, 10)
        words = []
        for _ in range(num_words):
            word_length = random.randint(3, 10)
            word = ''.join(random.choice('абвгдеєжзиіїйклмнопрстуфхцчшщьюя') for _ in range(word_length))
            words.append(word)
        return ' '.join(words)

    def run_test(self):
        for _ in range(10):
            text = self.generate_random_text()
            # Додамо помилку в половині випадків
            if random.random() < 0.5:
                text += " деякі текст"
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)
            self.check_grammar()

def main():
    root = tk.Tk()
    app = GrammarCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()