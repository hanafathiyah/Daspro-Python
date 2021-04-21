f = open("user.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(6):
    if(i == 0):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

def convert_line_to_data(line):
  raw_array_of_data = line.split(",")
  array_of_data = [data.strip() for data in raw_array_of_data]
  return array_of_data

raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)

datas = []

for line in lines :
  array_of_data = convert_line_to_data(line)
  real_values = convert_array_data_to_real_values(array_of_data)
  datas.append(real_values)

def modify_datas(idx, col, value):
  datas[idx][col] = value

def convert_datas_to_string():
  string_data = ",".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data

datas_as_string = convert_datas_to_string()

print(">> register")
new_user_idx = datas[-1][0] + 1
new_user_name = input("Masukkan nama: ")
upper_new_user_name = new_user_name.title()

# Ngecek apakah username sudah unik sebelum melanjutkan regis
unique = False
while unique == False :
  new_user_username = input("Masukkan username: ") 
  ketemu = False
  i = 0
  while ketemu == False and i < len(datas):
    if datas[i][1] == new_user_username:
      ketemu = True
      print("Username telah digunakan") 
    else:
      ketemu = False
      i += 1
  if ketemu == True and i >= len(datas):
    unique = False
  elif ketemu == False and i >= len(datas):
    unique = True

new_user_addres = input("Masukkan alamat: ")
new_user_password = input("Masukkan password: ")
new_user_role = "User"
new_user = [new_user_idx, new_user_username, upper_new_user_name, new_user_addres, new_user_password, new_user_role]

datas.append(new_user)
datas_as_string = convert_datas_to_string()

f = open("user.csv", "w")
f.write(datas_as_string)
f.close()
