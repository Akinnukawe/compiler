from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

class IDEInterface:
    def __init__(self, code_output):
        self.code_output = code_output

    def get_input(self):
        # Code to retrieve the source code from the IDE or user input
        source_code = self.code_output.get('1.0', 'end-1c')
        return source_code

    def display_output(self, output):
        # Code to display the output in the IDE
        self.code_output.insert('1.0', output)

    def display_error(self, error_message):
        # Code to display the error message in the IDE
        self.code_output.insert('1.0', error_message)

def set_file_path(path):
    global file_path
    file_path = path

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

compiler = Tk()
compiler.title('Free IDE')
file_path = ''

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_menu = Menu(menu_bar, tearoff=0)
run_menu.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_menu)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()