import tkinter as tk
from tkinter import ttk, messagebox
import string

# -------------------- Caesar Cipher --------------------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# -------------------- Vigenère Cipher --------------------
def generate_vigenere_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, key):
    key = generate_vigenere_key(text, key)
    cipher = ""
    for i in range(len(text)):
        if text[i].isalpha():
            base = ord('A') if text[i].isupper() else ord('a')
            shift = ord(key[i].lower()) - ord('a')
            cipher += chr((ord(text[i]) - base + shift) % 26 + base)
        else:
            cipher += text[i]
    return cipher

def vigenere_decrypt(cipher_text, key):
    key = generate_vigenere_key(cipher_text, key)
    orig_text = ""
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            base = ord('A') if cipher_text[i].isupper() else ord('a')
            shift = ord(key[i].lower()) - ord('a')
            orig_text += chr((ord(cipher_text[i]) - base - shift + 26) % 26 + base)
        else:
            orig_text += cipher_text[i]
    return orig_text

# -------------------- Playfair Cipher --------------------
def generate_playfair_matrix(key):
    key = key.lower().replace("j", "i")
    matrix = []
    used = set()
    for char in key + string.ascii_lowercase:
        if char not in used and char != 'j':
            matrix.append(char)
            used.add(char)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == char:
                return i, j
    return None

def playfair_prepare_text(text):
    text = text.lower().replace("j", "i").replace(" ", "")
    i = 0
    result = ""
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            result += a + 'x'
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += 'x'
    return result

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = playfair_prepare_text(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

def playfair_decrypt(text, key):
    matrix = generate_playfair_matrix(key)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5]
            result += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1]
            result += matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

# -------------------- GUI Application --------------------
def create_app():
    def run_cipher():
        text = input_text.get("1.0", tk.END).strip()
        key = key_entry.get().strip()
        cipher_type = cipher_choice.get()
        operation = operation_choice.get()

        if not text:
            messagebox.showerror("Error", "Please enter text.")
            return

        result = ""
        try:
            if cipher_type == "Caesar":
                shift = int(key) if key else 3
                result = caesar_encrypt(text, shift) if operation == "Encrypt" else caesar_decrypt(text, shift)
            elif cipher_type == "Vigenère":
                if not key.isalpha():
                    messagebox.showerror("Error", "Key must be alphabetic for Vigenère.")
                    return
                result = vigenere_encrypt(text, key) if operation == "Encrypt" else vigenere_decrypt(text, key)
            elif cipher_type == "Playfair":
                result = playfair_encrypt(text, key) if operation == "Encrypt" else playfair_decrypt(text, key)
        except Exception as e:
            result = f"Error: {e}"

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    root = tk.Tk()
    root.title("Classical Cipher Tool")
    root.geometry("600x500")

    tk.Label(root, text="Input Text:").pack()
    input_text = tk.Text(root, height=5)
    input_text.pack()

    tk.Label(root, text="Key (or shift):").pack()
    key_entry = tk.Entry(root)
    key_entry.pack()

    tk.Label(root, text="Cipher Type:").pack()
    cipher_choice = ttk.Combobox(root, values=["Caesar", "Vigenère", "Playfair"])
    cipher_choice.pack()
    cipher_choice.set("Caesar")

    tk.Label(root, text="Operation:").pack()
    operation_choice = ttk.Combobox(root, values=["Encrypt", "Decrypt"])
    operation_choice.pack()
    operation_choice.set("Encrypt")

    tk.Button(root, text="Run", command=run_cipher).pack(pady=10)

    tk.Label(root, text="Output Text:").pack()
    output_text = tk.Text(root, height=5)
    output_text.pack()

    root.mainloop()

# Call to function to start the app
create_app()
