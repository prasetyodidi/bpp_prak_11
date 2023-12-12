import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Menyimpan data ke dalam tabel
cursor.execute("INSERT INTO users (username, email) VALUES (?,?)", ('john_doe', 'john@example.com'))

# Commit perubahan
conn.commit()

# Mengambil data dari tabel
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Menampilkan data
for row in rows:
    print(row)

# Menutup koneksi
conn.close()