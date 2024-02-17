import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def load_data():
    try:
        with open("data.txt", "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'data.txt' não encontrado.")

def save_data():
    try:
        with open("data.txt", "w") as file:
            for item in tree.get_children():
                values = tree.item(item, "values")
                data = f"{values[0]}|{values[1]}|{values[2]}|{values[3]}|{values[4]};\n"
                file.write(data)
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")

def add_data():
    data = f"{image_entry.get()}| {name_entry.get()}| {description_entry.get()}| {genres_entry.get()}| {links_entry.get()};"
    tree.insert("", "end", values=(image_entry.get(), name_entry.get(), description_entry.get(), genres_entry.get(), links_entry.get()))
    clear_fields()
    messagebox.showinfo("Sucesso", "Novos dados adicionados com sucesso!")

def update_data():
    selected_item = tree.focus()
    if selected_item:
        values = (image_entry.get(), name_entry.get(), description_entry.get(), genres_entry.get(), links_entry.get())
        tree.item(selected_item, values=values)
        clear_fields()
        messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
    else:
        messagebox.showerror("Erro", "Selecione um item para modificar.")

def delete_data():
    selected_item = tree.focus()
    if selected_item:
        tree.delete(selected_item)
        clear_fields()
        messagebox.showinfo("Sucesso", "Item excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Selecione um item para excluir.")

def clear_fields():
    image_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    genres_entry.delete(0, tk.END)
    links_entry.delete(0, tk.END)

def on_item_selected(event):
    selected_item = tree.focus()
    values = tree.item(selected_item, "values")
    if values:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, values[0])
        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[1])
        description_entry.delete(0, tk.END)
        description_entry.insert(0, values[2])
        genres_entry.delete(0, tk.END)
        genres_entry.insert(0, values[3])
        links_entry.delete(0, tk.END)
        links_entry.insert(0, values[4])

root = tk.Tk()
root.title("Editor de Dados")

# Treeview
tree = ttk.Treeview(root, columns=("Image URL", "Name", "Description", "Genres", "Links"), show="headings")
tree.heading("Image URL", text="Image URL")
tree.heading("Name", text="Name")
tree.heading("Description", text="Description")
tree.heading("Genres", text="Genres")
tree.heading("Links", text="Links")
tree.bind("<<TreeviewSelect>>", on_item_selected)
tree.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Load existing data
existing_data = load_data()
if existing_data:
    for idx, item in enumerate(existing_data):
        item_data = item.strip().split("|")
        item_data[len(item_data)-1]=item_data[len(item_data)-1].replace(";","")
        tree.insert("", "end", values=item_data)

# Entry Fields
image_label = ttk.Label(root, text="URL da Imagem:")
image_label.grid(row=1, column=0, sticky=tk.W)
image_entry = ttk.Entry(root, width=50)
image_entry.grid(row=1, column=1, padx=5, pady=5)

name_label = ttk.Label(root, text="Nome:")
name_label.grid(row=2, column=0, sticky=tk.W)
name_entry = ttk.Entry(root, width=50)
name_entry.grid(row=2, column=1, padx=5, pady=5)

description_label = ttk.Label(root, text="Descrição:")
description_label.grid(row=3, column=0, sticky=tk.W)
description_entry = ttk.Entry(root, width=50)
description_entry.grid(row=3, column=1, padx=5, pady=5)

genres_label = ttk.Label(root, text="Gêneros:")
genres_label.grid(row=4, column=0, sticky=tk.W)
genres_entry = ttk.Entry(root, width=50)
genres_entry.grid(row=4, column=1, padx=5, pady=5)

links_label = ttk.Label(root, text="Links:")
links_label.grid(row=5, column=0, sticky=tk.W)
links_entry = ttk.Entry(root, width=50)
links_entry.grid(row=5, column=1, padx=5, pady=5)

# Buttons
save_button = ttk.Button(root, text="Salvar", command=save_data)
save_button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

add_button = ttk.Button(root, text="Adicionar", command=add_data)
add_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.E)

update_button = ttk.Button(root, text="Modificar", command=update_data)
update_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

delete_button = ttk.Button(root, text="Excluir", command=delete_data)
delete_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.E)

root.mainloop()

