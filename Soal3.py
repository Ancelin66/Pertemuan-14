#fungsi untuk membaca file dan mengambil kata dalam bentuk set
def ambil_kata(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            teks = f.read().lower()  # ubah semua ke lowercase
            for tanda in [".", ",", "!", "?", "\n", ";", ":"]:
                teks = teks.replace(tanda, " ")  # hilangkan tanda baca
            kata = teks.split()
            return set(kata)
    except:
        print(f"Terjadi kesalahan saat membuka file: {nama_file}")
        return None

#minta nama file dari pengguna
f1 = input("Masukkan nama file pertama: ")
f2 = input("Masukkan nama file kedua: ")

#ambil kata dari kedua file
kata1 = ambil_kata(f1)
kata2 = ambil_kata(f2)

#cek jika tidak ada error saat baca file
if kata1 is not None and kata2 is not None:
    hasil = kata1 & kata2  # ambil kata yang muncul di kedua file
    print("\n=== Kata yang muncul di kedua file ===")
    if hasil:
        for k in sorted(hasil):
            print("-", k)
    else:
        print("Tidak ada kata yang sama.")
