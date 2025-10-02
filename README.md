# Tugas-Seacrhing-AI
🚀 A* Search Algorithm in Python
📌 Deskripsi

Program ini mengimplementasikan algoritma A* dalam Python untuk mencari jalur terpendek dari titik awal (S) ke titik tujuan (G).

Selain menemukan jalur terbaik, program ini juga menampilkan setiap tahapan pencarian secara detail, termasuk:

Node yang dipilih

Perhitungan nilai g, h, dan f

Update frontier (open list)

Isi closed set

Jalur sementara yang terbentuk

Dengan begitu, program ini tidak hanya menghasilkan solusi, tetapi juga mempermudah pemahaman cara kerja algoritma A*.

📊 Struktur Graph

Graph diambil dari contoh soal (gambar).
Setiap node terhubung ke tetangga dengan bobot (cost) tertentu.

graph = {
    'S': [('A', 3), ('D', 2)],
    'A': [('S', 3), ('B', 5)],
    'B': [('A', 5), ('C', 2), ('D', 1), ('E', 1)],
    'C': [('B', 2), ('G', 4)],
    'D': [('S', 2), ('B', 1), ('E', 4)],
    'E': [('B', 1), ('D', 4), ('G', 3)],
    'G': [('C', 4), ('E', 3)]
}

Heuristik (h)

Heuristik adalah perkiraan jarak dari node ke goal:

heuristic = {
    'S': 7,
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 0
}

⚙️ Cara Kerja Algoritma

Inisialisasi

Masukkan node start S ke frontier (open list).

Hitung f = g + h untuk node awal.

Loop pencarian

Ambil node dengan nilai f terkecil dari frontier.

Jika node = G, maka pencarian selesai.

Jika bukan:

Tambahkan ke closed set.

Periksa semua tetangganya:

Hitung tentative_g = g_current + cost.

Hitung f_new = tentative_g + h(neighbor).

Jika lebih baik, update dan tambahkan ke frontier.

Output

Setiap langkah menampilkan:

Node yang sedang diekspansi

Perhitungan nilai g, h, f

Update frontier

Isi closed set

Hasil akhir

Jalur optimal + total biaya perjalanan.

🖥️ Contoh Output
=== Proses A* Search dari S ke G ===

[Langkah 1] Pop node 'S' | g=0, h=7, f=7
    Path sekarang : ['S']
    Periksa tetangga 'A' (cost=3) → g=3, h=9, f=12  → DITAMBAHKAN ke frontier
    Periksa tetangga 'D' (cost=2) → g=2, h=5, f=7   → DITAMBAHKAN ke frontier
    Frontier sekarang : [('D', 2, 7), ('A', 3, 12)]
    Closed set        : ['S']
------------------------------------------------------------
[Langkah 2] Pop node 'D' | g=2, h=5, f=7
   ...
==> Goal ditemukan!
Jalur akhir : ['S', 'D', 'B', 'E', 'G']
Biaya total: 7

▶️ Cara Menjalankan

Pastikan Python 3 sudah terinstall.

Simpan kode dalam file astar.py.

Jalankan di terminal:

python astar.py

📌 Kesimpulan

Algoritma A* menggabungkan biaya aktual (g) dan perkiraan ke goal (h) untuk mencari jalur terpendek.

Program ini memperlihatkan langkah demi langkah proses pencarian, sehingga sangat cocok untuk belajar dan memahami bagaimana A* bekerja.
