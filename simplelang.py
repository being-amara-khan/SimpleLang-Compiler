import tkinter as tk
from tkinter import filedialog
import subprocess

def lexical_analysis():
    code = code_text.get(1.0, tk.END)
    # Placeholder for Lexical Analysis (replace with actual logic)
    tokens = code.split()  # Simple tokenization for demonstration
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Lexical Analysis Phase:\n")
    output_text.insert(tk.END, f"Tokenized Output: {', '.join(tokens)}\n")
    output_text.config(state=tk.DISABLED)

def syntax_analysis():
    # Placeholder for Syntax Analysis (replace with actual logic)
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Syntax Analysis Phase:\n")
    output_text.insert(tk.END, "Syntax Tree Output: Placeholder\n")
    output_text.config(state=tk.DISABLED)

def semantic_analysis():
    # Placeholder for Semantic Analysis (replace with actual logic)
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Semantic Analysis Phase:\n")
    output_text.insert(tk.END, "Semantic Analysis Output: Placeholder\n")
    output_text.config(state=tk.DISABLED)

def generate_code():
    # Placeholder for Code Generation (replace with actual logic)
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Code Generation Phase:\n")
    output_text.insert(tk.END, "Generated Code Output: Placeholder\n")
    output_text.config(state=tk.DISABLED)

def run_code():
    code = code_text.get(1.0, tk.END)
    process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Final Output:\n")
    output_text.insert(tk.END, output.decode('utf-8'))
    output_text.insert(tk.END, error.decode('utf-8'))
    output_text.config(state=tk.DISABLED)

def open_file():
    file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if file_path:
        with open(file_path, 'r') as file:
            code_text.delete(1.0, tk.END)
            code_text.insert(tk.END, file.read())

root = tk.Tk()
root.title("Simplelang Compiler")
root.configure(bg='black')  # Set background color to black

# Title box on the top
title_label = tk.Label(root, text="SIMPLELANG COMPILER", fg='green', bg='black', font=("Arial", 16, "bold"))
title_label.pack(side=tk.TOP, pady=5)

# Increase the size of the input and output text boxes
code_text = tk.Text(root, wrap="word", width=100, height=20, fg='green', bg='black', insertbackground='green')
code_text.pack(pady=5)

# Place buttons on the top
button_frame = tk.Frame(root, bg='black')
button_frame.pack(side=tk.TOP)

lexical_button = tk.Button(button_frame, text="Lexical Analysis", command=lexical_analysis, fg='green', bg='black')
lexical_button.pack(side=tk.LEFT, padx=5)

syntax_button = tk.Button(button_frame, text="Syntax Analysis", command=syntax_analysis, fg='green', bg='black')
syntax_button.pack(side=tk.LEFT, padx=5)

semantic_button = tk.Button(button_frame, text="Semantic Analysis", command=semantic_analysis, fg='green', bg='black')
semantic_button.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(button_frame, text="Generate Code", command=generate_code, fg='green', bg='black')
generate_button.pack(side=tk.LEFT, padx=5)

run_button = tk.Button(button_frame, text="Run Code", command=run_code, fg='green', bg='black')
run_button.pack(side=tk.LEFT, padx=5)

open_button = tk.Button(button_frame, text="Open File", command=open_file, fg='green', bg='black')
open_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.destroy, fg='green', bg='black')
exit_button.pack(side=tk.RIGHT, padx=5)

output_text = tk.Text(root, wrap="word", width=100, height=10, state=tk.DISABLED, fg='green', bg='black')
output_text.pack(pady=5)

root.mainloop()
