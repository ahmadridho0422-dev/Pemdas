# Input
nama_barang = "Nasi goreng"
harga_satuan = 12000
jumlah_beli = 5
diskon_persen = 3

# Proses
total = harga_satuan * jumlah_beli
diskon = total * diskon_persen / 100
bayar = total - diskon

# Output
print(f"{nama_barang} x{jumlah_beli}")
print(f"Total  : Rp{total:,.0f}")
print(f"Diskon : Rp{diskon:,.0f}")
print(f"Bayar  : Rp{bayar:,.0f}")