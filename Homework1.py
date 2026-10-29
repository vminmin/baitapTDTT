#Bai 1
print('Bai 1')
n=int(input('Nhap n: '))
print(2*n)

#Bai 2
print('Bai 2')
a=float(input('Nhap a: '))
b=float(input('Nhap b: '))
area=a*b-3.14*(a/2)**2
print(round(area, 2))

#Bai 3
print('Bai 3')
char=input('Nhap ky tu: ')
if char.isupper():
    print(char.lower())
else:
    print(char.upper())

#Bai 4
print('Bai 4')
ki_tu=input('Nhap ky tu: ')
if ki_tu.isalpha() and len(ki_tu)==1:
    print(f'{ki_tu} la chu cai')
else:
    print(f'{ki_tu} khong phai la chu cai')

#Bai 5
print('Bai 5')
chu_cai_hoa=input('Nhap chu cai hoa: ')
x=0
if chu_cai_hoa!='A':
    x=chr(ord(chu_cai_hoa)-1)
    print(x)
else:
    print('Khong co chu cai truoc A')

#Bai 6
print('Bai 6')
a1=float(input('Nhap a1: '))
b1=float(input('Nhap b1: '))
c1=float(input('Nhap c1: '))
s= (a1+b1+c1)/2
area_triangle= (s*(s-a1)*(s-b1)*(s-c1))**0.5
if a1+b1>c1 and a1+c1>b1 and b1+c1>a1:
    print(round(area_triangle, 1))
else:
    print('Khong phai la tam giac')

#Bai 7
print('Bai 7')
chuoi_ky_tu=input('Nhap chuoi ky tu: ')
if len(chuoi_ky_tu)>20:
    print(chuoi_ky_tu[4], chuoi_ky_tu[8])
else:
    print('Chuoi ky tu khong du 20 ky tu')

#Bai 8
print('Bai 8')
Ten_chu_ho=input('Nhap ten chu ho: ')
Chi_so_thang_truoc=float(input('Nhap chi so thang truoc: '))
Chi_so_thang_nay=float(input('Nhap chi so thang nay: '))
kwh=Chi_so_thang_nay-Chi_so_thang_truoc
def tinh_tien_dien(kwh):
  tong_tien = 0
  # Bac 1: 0 - 50
  if kwh > 50:
    tong_tien += 50 * 1984
    kwh -= 50
  else:
    tong_tien += kwh * 1984
    return tong_tien
  # Bac 2: 51 - 100
  if kwh > 50:
    tong_tien += 50 * 2050
    kwh -= 50
  else:
    tong_tien += kwh * 2050
    return tong_tien
  # Bac 3: 101 - 200
  if kwh > 100:
    tong_tien += 100 * 2380
    kwh -= 100
  else:
    tong_tien += kwh * 2380
    return tong_tien
  # Bac 4: 201 - 300
  if kwh > 100:
    tong_tien += 100 * 2998
    kwh -= 100
  else:
    tong_tien += kwh * 2998
    return tong_tien
  # Bac 5: 301 - 400
  if kwh > 100:
    tong_tien += 100 * 3350
    kwh -= 100
  else:
    tong_tien += kwh * 3350
    return tong_tien

  # Bac 6: >400 kWh
  tong_tien += kwh * 3460
  return tong_tien
print(tinh_tien_dien(kwh))