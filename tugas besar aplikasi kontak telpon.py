import time

# --- 1. Data Kontak Telepon ---
RAW_KONTAK_DATA = [
    {'nama': 'AHMAD IHZAT', 'no_hp': '081234000001'},
    {'nama': 'ALFAT ARYA ADI CANDRA', 'no_hp': '081234000002'},
    {'nama': 'AUGUSTIO SYABRI MAULANA', 'no_hp': '081234000003'},
    {'nama': 'AZMI SYAPUTRA', 'no_hp': '081234000004'},
    {'nama': 'BAIQ AIGESTIA CAHYA ILAMI', 'no_hp': '081234000005'},
    {'nama': 'FAHRURROZY', 'no_hp': '081234000006'},
    {'nama': 'HENDRI JASWANDI', 'no_hp': '081234000007'},
    {'nama': 'ISMAIL TOYYIB', 'no_hp': '081234000008'},
    {'nama': 'KEMAS ABDUL AZIS SANJAYA', 'no_hp': '081234000009'},
    {'nama': 'LINDA AYU SAFITRI', 'no_hp': '081234000010'},
    {'nama': 'M. ZELQY ADRIAN', 'no_hp': '081234000011'},
    {'nama': 'M. RIPAI', 'no_hp': '081234000013'},
    {'nama': 'ABDUL GANDI', 'no_hp': '081234000025'},
    {'nama': 'ABDUL HARIS', 'no_hp': '081234000026'},
    {'nama': 'FADLI', 'no_hp': '081234000027'},
    {'nama': 'ALFIAN JULIANDA LUKMANSYA', 'no_hp': '081234000031'},
    {'nama': 'LALU MUH. RIZKY ADITIA PAMU', 'no_hp': '081234000032'},
    {'nama': 'M. KAISAR FAJRI AZMUS SYARQI', 'no_hp': '081234000012'},
    {'nama': 'MARDIANA SARI', 'no_hp': '081234000014'},
    {'nama': 'MIZWAN BUDIANSYAH', 'no_hp': '081234000015'},
    {'nama': 'MUHAMMAD RESAR FAHLEFI ASHAR', 'no_hp': '081234000016'},
    {'nama': 'NURUL HASAH FEBRIANI', 'no_hp': '081234000017'},
    {'nama': 'PUTRI WIHDA ANANDA', 'no_hp': '081234000018'},
    {'nama': 'SRI RAHMAYANI', 'no_hp': '081234000019'},
    {'nama': 'SUSI RAHADIAN', 'no_hp': '081234000020'},
    {'nama': 'VAREL HADINATA RIZKY', 'no_hp': '081234000021'},
    {'nama': 'WINA HAYATI', 'no_hp': '081234000022'},
    {'nama': 'WIRAHADI', 'no_hp': '081234000023'},
    {'nama': 'YULIA SUHERNI', 'no_hp': '081234000024'},
    {'nama': 'ZULFA ISMI ZURAIDA', 'no_hp': '081234000028'},
    {'nama': 'MUHAMMAD AMRIL', 'no_hp': '081234000029'},
    {'nama': 'MUHAMMAD SAPRUDIN JAELANI', 'no_hp': '081234000033'},
    {'nama': 'ZAKIRA', 'no_hp': '081234000034'}
]

# Menghapus duplikat (jika ada)
unique_kontak_data = []
seen_entries = set()
for kontak in RAW_KONTAK_DATA:
    kontak_tuple = tuple(sorted(kontak.items()))
    if kontak_tuple not in seen_entries:
        unique_kontak_data.append(kontak)
        seen_entries.add(kontak_tuple)

JUMLAH_KONTAK = len(unique_kontak_data)

# --- Fungsi Linear Search ---
def linear_search_kontak(kontak_list, search_name):
    start_time = time.perf_counter()
    found_kontak = None
    comparisons = 0

    for kontak in kontak_list:
        comparisons += 1
        if kontak["nama"].lower() == search_name.lower():
            found_kontak = kontak
            break

    end_time = time.perf_counter()
    time_taken_ms = (end_time - start_time) * 1000
    return found_kontak, time_taken_ms, comparisons

# --- Fungsi Binary Search ---
def binary_search_kontak(kontak_list_sorted, search_name):
    start_time = time.perf_counter()
    left = 0
    right = len(kontak_list_sorted) - 1
    search_name_lower = search_name.lower()
    found_kontak = None
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        current_name = kontak_list_sorted[mid]["nama"].lower()
        comparisons += 1

        if current_name == search_name_lower:
            found_kontak = kontak_list_sorted[mid]
            break
        elif current_name < search_name_lower:
            left = mid + 1
        else:
            right = mid - 1

    end_time = time.perf_counter()
    time_taken_ms = (end_time - start_time) * 1000
    return found_kontak, time_taken_ms, comparisons

# --- Fungsi Pencarian Parsial ---
def search_kontak_partial(kontak_list, query_partial):
    matches = []
    query_lower = query_partial.lower()
    comparisons = 0

    for kontak in kontak_list:
        comparisons += 1
        if query_lower in kontak["nama"].lower():
            matches.append(kontak)

    return matches, comparisons

# --- Siapkan Data Terurut ---
sorted_kontak_data = sorted(unique_kontak_data, key=lambda k: k['nama'].lower())

# --- Aplikasi Pencarian Kontak ---
def run_kontak_search_demo():
    print("\n==================== APLIKASI KONTAK TELEPON ====================")
    print(f"Jumlah Kontak: {JUMLAH_KONTAK}")

    while True:
        print("\n--- Menu ---")
        print("1. Cari Kontak (Linear Search)")
        print("2. Cari Kontak (Binary Search)")
        print("3. Pencarian Parsial (Autocomplete)")
        print("4. Tampilkan Daftar Kontak (Terurut)")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ").strip()

        if pilihan == '1':
            nama = input("Masukkan nama lengkap: ").strip()
            hasil, waktu, banding = linear_search_kontak(unique_kontak_data, nama)
            if hasil:
                print(f"\nDitemukan:\nNama: {hasil['nama']}\nNo HP: {hasil['no_hp']}")
            else:
                print("\nKontak tidak ditemukan.")
            print(f"Waktu: {waktu:.6f} ms, Perbandingan: {banding}")

        elif pilihan == '2':
            nama = input("Masukkan nama lengkap: ").strip()
            hasil, waktu, banding = binary_search_kontak(sorted_kontak_data, nama)
            if hasil:
                print(f"\nDitemukan:\nNama: {hasil['nama']}\nNo HP: {hasil['no_hp']}")
            else:
                print("\nKontak tidak ditemukan.")
            print(f"Waktu: {waktu:.6f} ms, Perbandingan: {banding}")

        elif pilihan == '3':
            nama = input("Masukkan sebagian nama: ").strip()
            hasil, banding = search_kontak_partial(sorted_kontak_data, nama)
            if not hasil:
                print("Tidak ada hasil ditemukan.")
            else:
                print("\nHasil Pencarian Parsial:")
                for i, kontak in enumerate(hasil):
                    print(f"{i+1}. {kontak['nama']} - {kontak['no_hp']}")
                print(f"Total hasil: {len(hasil)}, Perbandingan: {banding}")

        elif pilihan == '4':
            print("\nDaftar Kontak (Terurut):")
            for i, kontak in enumerate(sorted_kontak_data):
                print(f"{i+1}. {kontak['nama']} - {kontak['no_hp']}")

        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi kontak.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan aplikasi
if __name__ == "__main__":
    run_kontak_search_demo()
