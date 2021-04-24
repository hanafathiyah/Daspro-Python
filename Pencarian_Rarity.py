def open_gadget_csv():

  f = open("Gadget.csv","r")
  raw_lines = f.readlines()
  f.close()
  lines = [raw_line.replace("\n","") for raw_line in raw_lines]

  def convert_array_data_to_real_values(array_data):
    arr_cpy = array_data[:]
    for i in range(6):
      if ( i == 3 or i == 5 ):
        arr_cpy[i] = int(arr_cpy[i])   
    return arr_cpy

  def convert_line_to_data(line):
    raw_array_of_data = line.split(";")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

  raw_header = lines.pop(0)
  header = convert_line_to_data(raw_header)

  datas = []

  for line in lines:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data)
    datas.append(real_values)

  return datas

datas = open_gadget_csv()

###################################################
print(">>> carirarity")
rarity = input("Masukkan rarity: ")
print("\nHasil pencarian:\n")

def mencari_rarity(rarity,datas) :
  rarity_benar = False
  i = 0
  while rarity_benar == False and i < len(datas):
    if (rarity == datas[i][4]):
      print("Nama :", datas[i][1])
      print("Deskripsi :", datas[i][2])
      print("Jumlah :", datas[i][3], "buah")
      print("Rarity :", datas[i][4])
      print("Tahun Ditemukan :", datas[i][5] ,"\n")
      i += 1
    else:
      i += 1

mencari_rarity(rarity,datas)