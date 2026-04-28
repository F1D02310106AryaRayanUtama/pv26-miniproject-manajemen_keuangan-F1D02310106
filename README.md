# Nama : Arya Rayan Utama  
# NIM  : F1D02310106  
# Kelas : Pemvis C
---

# Aplikasi Manajemen Keuangan Sederhana

## Deskripsi
Aplikasi Keuangan Sederhana adalah aplikasi desktop berbasis GUI yang dibuat menggunakan PySide6.  
Aplikasi ini digunakan untuk mencatat pemasukan dan pengeluaran secara terstruktur dengan penyimpanan data menggunakan database SQLite.

Aplikasi ini dibuat sebagai Mini Project Pemrograman Visual dengan menerapkan konsep Separation of Concerns (SoC), penggunaan database, serta styling menggunakan QSS.

---

## Fitur Utama
- Tambah data transaksi (Create)
- Menampilkan data transaksi (Read)
- Edit data transaksi (Update)
- Hapus data transaksi (Delete)
- Validasi input jumlah (hanya angka)
- Format otomatis mata uang Rupiah (Rp)
- Dialog form terpisah untuk tambah/edit data
- Konfirmasi saat menghapus data
- Menu "Tentang Aplikasi"
- Tampilan GUI menggunakan styling QSS eksternal

---

## Teknologi yang Digunakan
- Python
- PySide6 (GUI Framework)
- SQLite (Database)
- QSS (Qt Style Sheet)

---

## Struktur Folder Project

Keuangan-app/
│
├── main.py
├── database/
│ └── db.py
├── ui/
│ ├── main_window.py
│ └── transaksi_dialog.py
├── styles/
│ └── style.qss
└── keuangan.db



---

## Cara Menjalankan Aplikasi

1. Pastikan Python sudah terinstall
2. Install dependency: pip install PySide6
3. 3. Jalankan aplikasi: python main.py
  

---

## Desain Database

Tabel: `transaksi`

| Kolom      | Tipe Data |
|-----------|----------|
| id        | INTEGER (Primary Key) |
| tanggal   | TEXT |
| jenis     | TEXT |
| kategori  | TEXT |
| jumlah    | REAL |
| deskripsi | TEXT |

---

## Penerapan Separation of Concerns (SoC)

- `main.py` → Entry point aplikasi
- `ui/main_window.py` → Tampilan utama & interaksi user
- `ui/transaksi_dialog.py` → Form input (tambah & edit)
- `database/db.py` → Pengelolaan database (CRUD)
- `styles/style.qss` → Styling tampilan aplikasi

---

## Screenshot Aplikasi
Tambahkan screenshot tampilan aplikasi di sini (opsional namun disarankan)
### Tampilan awal saat aplikasi dijalankan 
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/609b5d56-1ff0-4891-a407-eb0d4a81a692" />

---

### Tampilan fitur Tambah Transaksi
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/ccf62c10-a1a7-4c8d-a719-ccbbbf67abed" />

---

### Tampilan fitur Edit Transaksi
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/323a3c0b-4886-4c2e-ac3e-4b6d5a17db45" />

---

### Tampilan fitur Hapus Transaksi serta Peringatan Konfirmasi
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/d2690ba8-975e-4b20-beef-bf2140dab9b4" />

---

### Tampilan Fitur Help Tentang Aplikasi
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/a8432ce5-1476-4368-9241-92451f80a9f5" />

---

### Tampilan Warning saat ingin Edit atau Hapus data tanpa memilih data terlebih dahulu
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/69f713f4-de16-495e-91ea-f74356ba61d0" />


---

## Link
GitHub Repository :  
Video YouTube     : [ISI LINK VIDEO]
