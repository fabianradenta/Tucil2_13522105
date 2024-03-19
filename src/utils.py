from point import Point

def welcome() :
    print("""
Selamat datang di Program Visualisasi Kurva Bézier

Untuk menggunakan program ini, silakan persiapkan masukan berikut :
- Jumlah iterasi yang digunakan dalam perhitungan
- Tiga buah titik kontrol (x,y) yang membentuk kurva

Ayo kita mulai!
    """)

def process_input_point(input_str_1, input_str_2, input_str_3) :
    # pisahkan absis dan oordinat
    x_str_1, y_str_1 = input_str_1.split(',')
    x_str_2, y_str_2 = input_str_2.split(',')
    x_str_3, y_str_3 = input_str_3.split(',')

    # casting tipe data
    x1 = float(x_str_1)
    x2 = float(x_str_2)
    x3 = float(x_str_3)
    y1 = float(y_str_1)
    y2 = float(y_str_2)
    y3 = float(y_str_3)

    # declare point
    point1 = Point(x1,y1)
    point2 = Point(x2,y2)
    point3 = Point(x3,y3)
    return point1, point2, point3

def method_option() :
    print("""

Pilihan metode :
1. Divide and Conquer
2. Brute-Force
    """)

def thanks() :
    print('\n'+23*'=')
    print(5*' '+"Terima kasih"+6*' ')
    print(23*'=')
    print(7*' '+"₊˚.⊹♡⊹.˚₊"+7*' ')

