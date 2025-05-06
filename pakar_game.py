from pyswip import Prolog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("pakar_game.pl")
genre_list = list()
preferensi = dict()
index_genre = 0
index_preferensi = 0
current_genre = ""
current_preferensi = ""

def mulai_rekomendasi():
    global genre_list, preferensi, index_genre, index_preferensi
    prolog.retractall("preferensi_pos(_)")
    prolog.retractall("preferensi_neg(_)")
    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)
    genre_list = [g["X"].decode() for g in list(prolog.query("genre(X)"))]
    for g in genre_list:
        preferensi[g] = [p["X"] for p in list(prolog.query(f"preferensi(X,\"{g}\")"))]
    index_genre = 0
    index_preferensi = -1
    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_genre=False):
    global current_genre, current_preferensi, index_genre, index_preferensi

    if ganti_genre:
        index_genre += 1
        index_preferensi = -1
    if index_genre >= len(genre_list):
        hasil_rekomendasi()
        return
    current_genre = genre_list[index_genre]
    index_preferensi += 1
    if index_preferensi >= len(preferensi[current_genre]):
        hasil_rekomendasi(current_genre)
        return
    current_preferensi = preferensi[current_genre][index_preferensi]
    if list(prolog.query(f"preferensi_pos({current_preferensi})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"preferensi_neg({current_preferensi})")):
        pertanyaan_selanjutnya(ganti_genre=True)
        return
    pertanyaan = list(prolog.query(f"pertanyaan({current_preferensi}, Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"preferensi_pos({current_preferensi})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"preferensi_neg({current_preferensi})")
        pertanyaan_selanjutnya(ganti_genre=True)

def hasil_rekomendasi(genre=""):
    if genre:
        messagebox.showinfo("Rekomendasi Game", f"Genre yang cocok untuk Anda adalah: {genre}.")
    else:
        messagebox.showinfo("Rekomendasi Game", "Tidak ditemukan genre yang cocok.")
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# GUI
root = tk.Tk()
root.title("Sistem Rekomendasi Genre Game")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Aplikasi Rekomendasi Genre Game", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)
kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)
no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))
yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))
start_btn = ttk.Button(mainframe, text="Mulai Rekomendasi", command=mulai_rekomendasi)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
