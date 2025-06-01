from collections import defaultdict

#input jumlah kategori
n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}

#input nama kategori dan aplikasi
for i in range(n):
    nama_kategori = input(f'\nMasukkan nama kategori ke-{i+1}: ')
    print(f'Masukkan 5 nama aplikasi di kategori {nama_kategori}:')
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input(f'  Nama aplikasi {j+1}: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi

#tampilkan isi dictionary
print("\n=== Daftar Aplikasi di Setiap Kategori ===")
for kategori, apps in data_aplikasi.items():
    print(f"- {kategori}: {', '.join(apps)}")

#mengambil semua daftar aplikasi dan ubah ke set
daftar_aplikasi_list = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

#aplikasi yang muncul di semua kategori
hasil_intersection = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil_intersection = hasil_intersection.intersection(daftar_aplikasi_list[i])

print("\n=== Aplikasi yang muncul di semua kategori ===")
if hasil_intersection:
    for app in hasil_intersection:
        print(f"- {app}")
else:
    print("Tidak ada aplikasi yang muncul di semua kategori.")

#hitung jumlah kemunculan aplikasi di semua kategori
jumlah_kemunculan = defaultdict(int)
for daftar in data_aplikasi.values():
    for app in daftar:
        jumlah_kemunculan[app] += 1

#aplikasi yang hanya muncul di satu kategori
print("\n=== Aplikasi yang hanya muncul di satu kategori ===")
ada = False
for app, count in jumlah_kemunculan.items():
    if count == 1:
        print(f"- {app}")
        ada = True
if not ada:
    print("Tidak ada.")

#jika n > 2: tampilkan aplikasi yang muncul tepat di dua kategori
if n > 2:
    print("\n=== Aplikasi yang muncul tepat di dua kategori ===")
    ada_dua = False
    for app, count in jumlah_kemunculan.items():
        if count == 2:
            print(f"- {app}")
            ada_dua = True
    if not ada_dua:
        print("Tidak ada.")
