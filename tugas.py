# Tugas Pemrograman Dasar dan Git
# Nama dalam Huruf ASCII

A = [" *** ", "*   *", "*****", "*   *", "*   *"]
H = ["*   *", "*   *", "*****", "*   *", "*   *"]
M = ["*   *", "** **", "* * *", "*   *", "*   *"]
D = ["**** ", "*   *", "*   *", "*   *", "**** "]
R = ["**** ", "*   *", "**** ", "*  * ", "*   *"]
I = ["*****", "  *  ", "  *  ", "  *  ", "*****"]
O = [" *** ", "*   *", "*   *", "*   *", " *** "]

# Nama AHMAD
ahmad = [A, H, M, A, D]
for baris in range(5):
    print("  ".join(huruf[baris] for huruf in ahmad))

print()

# Nama RIDHO
ridho = [R, I, D, H, O]
for baris in range(5):
    print("  ".join(huruf[baris] for huruf in ridho))

print()

# Biodata mahasiswa
print("==========================================")
print("Nama  : Ahmad Ridho")
print("NIM   : 26012048")
print("Kelas : 26M13")
print("Prodi : D3 Manajemen Informatika")
print("==========================================")