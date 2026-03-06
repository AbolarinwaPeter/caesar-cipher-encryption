import tkinter as tk
from tkinter import messagebox
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def cipher(coefficient):
    message_entry = cipher_entry.get().lower()
    shift_val = shift_entry.get()
    if len(message_entry) == 0 or len(shift_val) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            shift_val= int(shift_val) * coefficient
        except ValueError:
            messagebox.showerror("Error", "Please enter a number in the shift value")
        else:
            message_out = []
            out_string = ""
    
            for l in message_entry:
                if l not in letter_list:
                    message_out.append(l)
                else:
                    l_index = letter_list.index(l)
                    message_out.append(letter_list[(l_index + shift_val)%len(letter_list)])
            out_string = "".join(message_out)
            cipher_entry.delete(0, len(message_entry))
            cipher_entry.insert(0, out_string)
def decode():
    cipher(-1)
def encode():
    cipher(1)


window = tk.Tk()
window.title("Caesar's Cypher")
window.config(padx=20, pady=20)
cipher_label = tk.Label(text="Enter Cypher text")
cipher_label.grid(column=0, row=0)
cipher_entry = tk.Entry()
cipher_entry.grid(column=1, row=0)
cipher_entry.focus()
shift_label = tk.Label(text="Shift value")
shift_label.grid(column=0, row=1)
shift_entry = tk.Entry(width = 25)
shift_entry.grid(column=1, row=1)
encrypt_button = tk.Button(text="Encrypt", command=encode)
encrypt_button.grid(column=0, row=3)
decrypt_button = tk.Button(text="Decrypt", command=decode)
decrypt_button.grid(column=1, row=3)
window.mainloop()
