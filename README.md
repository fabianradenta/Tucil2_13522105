# Constructing Bézier Curve Using Divide and Conquer Midpoint Algorithm and Brute-Force Algorithm
> *Source Code* ini dibuat untuk memenuhi Tugas Kecil 2 Mata kuliah Strategi Algoritma IF2211 yaitu "Membangun Kurva Bézier dengan Algoritma Titik Tengah berbasis *Divide and Conquer*".

## Deskripsi Singkat Program
Program untuk memvisualisasikan Kurva Bézier dengan titik tengah berbasis Algoritma *Divide and Conquer*. Program dibatasi hanya dapat menggambar kurva dengan 3 titik kontrol. Program akan menerima masukan berupa jumlah iterasi, tiga titik kontrol dan metode algoritma yang akan digunakan. Dengan program ini, pemecahan masalah membangun Kurva Bézier dengan metode *Divide and Conquer* dapat dibandingkan terhadap metode *Brute Force*. Program dibangun dengan menggunakan bahasa Python.

## Requirements
- Python3 
- *Library* Matplotlib
- *Library* time

## Cara Menjalankan Program
1. Pastikan Python3 sudah terpasang di perangkat anda. Status pemasangan dapat diperiksa dengan menjalankan *command* `python3 --version` pada *command prompt*.
2. *Clone repository* dengan *command* berikut
```
git clone https://github.com/fabianradenta/Tucil2_13522105.git
``` 
3. Masuk ke *directory* src. Pastikan mengganti `/path/to/src` dengan *path* yang benar.
```
cd /path/to/src
```
4. Jalankan program dengan *command* `python3 main.py` 
5. Program akan meminta masukan jumlah iterasi, titik kontrol (titik yang paling awal dimasukkan akan menjadi titik awal kurva, begitu juga dengan titik yang paling akhir.), dan metode algoritma yang akan digunakan. Pastikan masukan yang diterima program benar. Jika masukan salah maka program akan berhenti dan memberikan pesan *error*. 
6. Jika masukan yang diterima sudah benar, program akan melakukan perhitungan untuk memperoleh titik-titik yang dilewati *Kurva Bézier* dengan metode yang dipilih (*Divide and Conquer* atau *Brute Force*) kemudian memvisualisasikan Kurva dengan menarik garis antara titik-titik tersebut. Program juga akan memberikan informasi waktu eksekusi program yang ditampilkan di CLI (waktu yang ditampilkan hanyalah waktu perhitungan program dalam mendapatkan titik-titik yang melewati kurva, tidak termasuk waktu program divisualisasikan). 

## Author
Nama : Fabian Radenta Bangun<br>
NIM : 13522105<br>
Program Studi : Teknik Informatika<br>
Profile Github : [fabianradenta](github.com/fabianradenta)