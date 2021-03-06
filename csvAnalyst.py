# программа анализа .csv файлов

import tkinter as tk
import tkinter.filedialog
import tkinter.scrolledtext
import pandas as pd
import os

# Создание главного окна
window = tk.Tk()
window.geometry('550x550-200-200')
window.title('csvAnalyst - программа анализа .csv файлов')

# создаём метки
file_label = tk.Label(text = 'Файл:')
rows_label = tk.Label(text = 'Строк:')
cols_label = tk.Label(text = 'Столбцов:')

# размещаем
file_label.grid(row = 0, column = 0, padx = 5, pady = 5)
rows_label.grid(row = 1, column = 0, padx = 5, pady = 5)
cols_label.grid(row = 1, column = 2, padx = 5, pady = 5)

# создаём поля ввода/вывода
file_label_out = tk.Label(text = '', relief = 'groove', width = 32)
rows_label_out = tk.Label(text = '', relief = 'groove', width =  5)
cols_label_out = tk.Label(text = '', relief = 'groove', width =  5)

# размещаем
file_label_out.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan = 4, sticky='w')
rows_label_out.grid(row = 1, column = 1, padx = 5, pady = 5)
cols_label_out.grid(row = 1, column = 3, padx = 5, pady = 5)

output_text = tk.scrolledtext.ScrolledText(height = 24, width = 32, wrap = 'none')
output_text.grid(row = 2, column = 0, padx = 5, pady = 5, columnspan = 5)

def do_read_file():
  my_dir = os.getcwd()
  file_name = tk.filedialog.askopenfilename(initialdir = my_dir, filetypes = (('CSV files', '*.csv'), ('All files', '*.*')))
  file_label_out['width'] = 0
  file_label_out['text']  = file_name
  if file_name != '':
    df = pd.read_csv(file_name, sep=';')
    rows = df.shape[0]
    cols = df.shape[1]
    rows_label_out['text'] = rows
    cols_label_out['text'] = cols
    for r in range(rows):
      for c in range(cols):
        output_text.insert(tk.END, str(df.iat[r,c]) + ';')
      output_text.insert(tk.END, os.linesep)
  else:
    file_label_out['width'] = 32
    rows_label_out['text']  = ''
    cols_label_out['text']  = ''
    output_text.delete(0.0, tk.END)

button = tk.Button(window, text = ' Читать ', command = do_read_file)
button.grid(row = 1, column = 4)

# Запуск цикла mainloop
window.mainloop()
