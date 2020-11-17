import tkinter as tk

master = tk.Tk()
tk.Label(master, text="Database").grid(row=0)
tk.Label(master, text="Table").grid(row=1)
tk.Label(master, text="Table Engine").grid(row=1, column=3)
tk.Label(master, text="Columns").grid(row=2)
tk.Label(master, text="Data Type").grid(row=2, column=3)
tk.Label(master, text="Query: ").grid(row=3)

e_db = tk.Entry(master)
e_tab = tk.Entry(master)
e_col = tk.Entry(master)
e_data_type = tk.Entry(master)
e_tab_engine = tk.Entry(master)

e_db.grid(row=0, column=1)
e_tab.grid(row=1, column=1)
e_tab_engine.grid(row=1, column=4)
e_col.grid(row=2, column=1)
e_data_type.grid(row=2, column=4)


def create_table():
    query = f"CREATE TABLE IF EXISTS {e_db.get()}.{e_tab.get()} ({e_col.get()} {e_data_type.get()}) ENGINE {e_tab_engine.get()}"
    # print(query
    result.delete(0, tk.END)
    result.insert(0, query)
    print(result.get())
    # e_db.delete(0, tk.END)
    # e_tab.delete(0, tk.END)


tk.Button(master, text='QUIT', command=master.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='CREATE', command=create_table).grid(row=4, column=1, sticky=tk.W, pady=4)

result = tk.Entry(master, width=100)
result.grid(row=3, column=1, columnspan=10)

master.mainloop()
