import heapq
from math import inf

# ==============================
# Definisi graf (berarah + berbobot)
# ==============================
# Bentuknya dictionary: { node: [(tetangga, biaya), ...] }
# Dibuat dua arah agar bisa menelusuri balik
graph = {
    'S': [('A', 3), ('D', 2)],       # S terhubung ke A (3), D (2)
    'A': [('S', 3), ('B', 5)],       # A ke S (3), B (5)
    'B': [('A', 5), ('C', 2), ('D', 1), ('E', 1)], # dst...
    'C': [('B', 2), ('G', 4)],
    'D': [('S', 2), ('B', 1), ('E', 4)],
    'E': [('B', 1), ('D', 4), ('G', 3)],
    'G': [('C', 4), ('E', 3)]
}

# ==============================
# Nilai heuristic (h)
# ==============================
# Heuristic = estimasi jarak dari node ke tujuan G
heuristic = {
    'S': 7,
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 0   # goal selalu 0
}

def a_star_verbose(start, goal):
    # ==============================
    # Priority Queue (frontier / OPEN list)
    # ==============================
    # Tiap elemen frontier = (f, g, node, path)
    # f = g + h
    # g = biaya nyata dari start ke node
    # node = simpul yang sedang dipertimbangkan
    # path = jalur yang dilalui sampai node ini
    open_heap = []
    
    # Masukkan node awal ke frontier
    # g(start)=0, f=start.h
    heapq.heappush(open_heap, (heuristic[start], 0, start, [start]))
    
    # g_score menyimpan biaya terendah yang diketahui untuk tiap node
    g_score = {n: inf for n in graph}
    g_score[start] = 0
    
    # Closed set menyimpan node yang sudah diproses supaya tidak diulang
    closed = set()
    
    step = 0
    print("=== Proses A* Search dari {} ke {} ===\n".format(start, goal))
    
    # ==============================
    # Loop utama A*
    # ==============================
    while open_heap:
        step += 1
        # Ambil node dengan nilai f terkecil dari frontier
        f_current, g_current, current, path_current = heapq.heappop(open_heap)
        
        # Jika ada jalur lain dengan g lebih kecil, lewati (skip)
        if g_current > g_score[current]:
            continue
        
        # Cetak informasi node yang sedang diproses
        print(f"[Langkah {step}] Pop node '{current}' | g={g_current}, h={heuristic[current]}, f={f_current}")
        print(f"    Path saat ini : {path_current}")
        
        # ==============================
        # Jika goal tercapai → selesai
        # ==============================
        if current == goal:
            print("\n==> Goal ditemukan!")
            print(f"Jalur terbaik : {path_current}")
            print(f"Biaya total   : {g_current}")
            return path_current, g_current
        
        # Masukkan node ini ke closed set
        closed.add(current)
        
        # ==============================
        # Ekspansi semua tetangga node
        # ==============================
        for neighbor, cost in graph[current]:
            # Hitung g baru (biaya nyata)
            tentative_g = g_current + cost
            # Hitung f = g + h
            f_new = tentative_g + heuristic[neighbor]
            
            print(f"    Periksa tetangga '{neighbor}' (cost={cost}) → g={tentative_g}, h={heuristic[neighbor]}, f={f_new}", end="")
            
            # Jika tetangga sudah diproses → skip
            if neighbor in closed:
                print("  → SKIP (sudah di-closed)")
                continue
            
            # Jika jalur ini lebih baik daripada yang diketahui sebelumnya → update
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g  # update nilai g terbaik
                new_path = path_current + [neighbor]  # update jalur
                heapq.heappush(open_heap, (f_new, tentative_g, neighbor, new_path))  # masukkan ke frontier
                print("  → DITAMBAHKAN ke frontier")
            else:
                print("  → Abaikan (bukan jalur lebih baik)")
        
        # ==============================
        # Cetak isi frontier & closed set
        # ==============================
        frontier_snapshot = sorted([(entry[2], entry[1], entry[0]) for entry in open_heap], key=lambda x: (x[2], x[1]))
        print("    Frontier sekarang :", frontier_snapshot)  # (node, g, f)
        print("    Closed set        :", sorted(list(closed)))
        print("-" * 60)
    
    # ==============================
    # Jika tidak ada jalur ke goal
    # ==============================
    print("Goal tidak ditemukan.")
    return None, inf


# ==============================
# Jalankan algoritma A*
# ==============================
path, cost = a_star_verbose('S', 'G')
