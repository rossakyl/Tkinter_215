#Graphical User Interface (GUI) tampilan visual

import tkinter as tk
import tkinter.messagebox as msg

#fungsi untuk menampilkan hasil prediksi (event)
def hasil_prediksi():
    msg.showinfo("Hasil Prediksi", "Prodi yang cocok: Teknologi Informasi")  # tampilkan pesan hasil prediksi

# membuat jendela utama
root = tk.Tk()                     # buat window utama (state)
root.title("Aplikasi Prediksi Prodi Pilihan")   # set judul window
root.geometry("400x500")           # atur ukuran window
root.configure(bg="lightblue")      # atur warna latar belakang

# label judul aplikasi
judul = tk.Label(root, text="Prediksi Prodi Pilihan", font=("Times New Roman", 14, "bold"))  # buat label judul
judul.pack(pady=10)                # tampilkan label dengan jarak vertikal

# membuat 10 input nilai mata pelajaran
entries = []                       # list untuk menampung input (state = menyimpan data)
for i in range(1, 11):             # ulang 10 kali
    frame = tk.Frame(root)        # buat frame untuk tiap baris input
    frame.pack(pady=3)             # atur jarak antar baris
    label = tk.Label(frame, text=f"Nilai {i}:")  # label nama pelajaran
    label.pack(side="left")        # tampilkan label di kiri
    entry = tk.Entry(frame, width=10)  # buat kotak input nilai
    entry.pack(side="left", padx=5)     # tampilkan entry di kanan label
    entries.append(entry)          # simpan entry ke list

# tombol untuk menampilkan hasil prediksi
tombol = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  #buat tombol (event)
tombol.pack(pady=15)               # tampilkan tombol dengan jarak

# label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="Luaran hasil prediksi akan muncul di sini.", font=("Arial", 10, "italic"))  # label hasil
hasil_label.pack(pady=10)          # tampilkan label hasil

# menjalankan GUI agar tetap tampil
root.mainloop()                    # jalankan event loop GUI