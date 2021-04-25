import data
from LoadData import load_data

load_data("folder_isi")

def hasil_kategori(kategori,array,tahun):
  if kategori == '=':
    return (array[5] == tahun)
  elif kategori == '>':
    return (array[5] > tahun)
  elif kategori == '<':
    return (array[5] < tahun)
  elif kategori == '>=':
    return (array[5] >= tahun)
  elif kategori == '<=':
    return (array[5] <= tahun)

def mencari_tahun() :
  datas = data.gadget

  print(">>> caritahun")
  tahun = int(input("Masukkan tahun: "))
  kategori = input("Masukkan kategori: ")
  print("\nHasil pencarian:\n")

  for array in (datas):
    if (hasil_kategori(kategori,array,tahun)) :
      print("Nama :", array[1])
      print("Deskripsi :", array[2])
      print("Jumlah :", array[3], "buah")
      print("Rarity :", array[4])
      print("Tahun Ditemukan :", array[5] ,"\n")