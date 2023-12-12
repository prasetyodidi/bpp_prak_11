import sqlite3
# Membuat koneksi ke database atau membuat database jika belum ada

conn = sqlite3.connect('my_database.db')

# Menginisialisasi kursor untuk eksekusi perintah SQL
cursor = conn.cursor()

# Membuat tabel dalam database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Commit perubahan dan menutup koneksi
conn.commit()
conn.close()