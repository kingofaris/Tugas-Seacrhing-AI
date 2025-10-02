# 🔎 A* Search Algorithm in Python

Algoritma **A\*** digunakan untuk menemukan jalur terpendek dari titik awal (**Start**) ke titik tujuan (**Goal**) dengan menggabungkan:
- **g(n)** = biaya perjalanan dari start ke node n  
- **h(n)** = estimasi jarak dari node n ke goal  
- **f(n) = g(n) + h(n)**

---

## 📑 Daftar Isi
- [Deskripsi](#-deskripsi)
- [Struktur Graph](#-struktur-graph)
- [Heuristik](#-heuristik)
- [Cara Kerja Algoritma](#-cara-kerja-algoritma)
- [Cara Menjalankan](#-cara-menjalankan)
- [Kesimpulan](#-kesimpulan)

---

## 📝 Deskripsi
Program ini mengimplementasikan **A\*** dengan bahasa Python.  
Selain mencari jalur terpendek, program juga menampilkan **setiap langkah pencarian**:  
- Node yang dipilih  
- Perhitungan `g`, `h`, `f`  
- Isi frontier (*open list*) dan *closed set*  
- Jalur sementara  

---

## 📊 Struktur Graph
```python
graph = {
    'S': [('A', 3), ('D', 2)],
    'A': [('S', 3), ('B', 5)],
    'B': [('A', 5), ('C', 2), ('D', 1), ('E', 1)],
    'C': [('B', 2), ('G', 4)],
    'D': [('S', 2), ('B', 1), ('E', 4)],
    'E': [('B', 1), ('D', 4), ('G', 3)],
    'G': [('C', 4), ('E', 3)]
}

heuristic = {
    'S': 7, 'A': 9, 'B': 4,
    'C': 2, 'D': 5, 'E': 3, 'G': 0
}
```
## ⚙️ Cara Kerja Algoritma
- Masukkan node awal S ke frontier dengan g=0.

- Hitung f = g + h.

- Pilih node dengan f terkecil dari frontier.

- Jika node tersebut adalah G, pencarian selesai.

- Jika bukan, pindahkan node ke closed set dan periksa semua tetangga.

- Update frontier dengan nilai g, h, f baru jika lebih baik.

- Ulangi proses sampai goal ditemukan atau frontier kosong.

## ▶️ Cara Menjalankan
1. Pastikan Python 3 sudah terinstall.
2. jalankan dengan command :
```
python serching.py
```

## ✅ Kesimpulan
- Algoritma A* mencari jalur terpendek dengan menggabungkan biaya aktual (g) dan estimasi heuristik (h).

- Dibandingkan BFS atau DFS, A* lebih efisien karena mempertimbangkan perkiraan jarak ke tujuan.

- Program ini memperlihatkan langkah demi langkah pencarian, sehingga sangat membantu dalam pembelajaran Artificial Intelligence.
