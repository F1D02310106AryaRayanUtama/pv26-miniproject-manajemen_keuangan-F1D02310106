import sqlite3

DB_NAME = "keuangan.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            jenis TEXT,
            kategori TEXT,
            jumlah REAL,
            deskripsi TEXT
        )
    """)

    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    create_table()
    print("Database dan tabel berhasil dibuat!")
    
def get_all_transaksi():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transaksi")
    data = cursor.fetchall()

    conn.close()
    return data

def insert_transaksi(tanggal, jenis, kategori, jumlah, deskripsi):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transaksi (tanggal, jenis, kategori, jumlah, deskripsi)
        VALUES (?, ?, ?, ?, ?)
    """, (tanggal, jenis, kategori, jumlah, deskripsi))

    conn.commit()
    conn.close()

def delete_transaksi(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transaksi WHERE id = ?", (id,))

    conn.commit()
    conn.close()
    
def update_transaksi(id, tanggal, jenis, kategori, jumlah, deskripsi):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transaksi
        SET tanggal=?, jenis=?, kategori=?, jumlah=?, deskripsi=?
        WHERE id=?
    """, (tanggal, jenis, kategori, jumlah, deskripsi, id))

    conn.commit()
    conn.close()