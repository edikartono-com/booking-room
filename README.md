# Booking Room
Booking Room projet manajemen pesanan room yang digunakan seseorang memesan sebuah gedung atau ruangan untuk pertemuan rapat dan lainnya.

Pengelola menentukan ruangan dan hari yang bisa disewa. (diasumsikan ruangan disewa harian bukan perjam)
Pemesan ruangan dapat memilih tanggal besok hari dan ruangan yang tersedia. Tidak bisa memesan untuk hari ini apalagi kemarin.

Ruangan yang sedang dalam proses pemesanan tidak tampak oleh calon pemesan lain selama 1 jam. Apabila pemesan tidak menyelesaikan pesanannya dalam waktu 1 jam, maka ruangan tersebut dapat dipesan oleh penyewa lain.


# installasi
1. Membuat virtual environment dan aktivkan.
2. Clone git clone https://github.com/edikartono-com/booking-room.git
3. Install pip install -r requirements.txt
4. Buat directory <code>tmp/cart</code>
5. Jalankan <code>makemigrations</code> dan <code>migrate</code>
6. Buat superuser <code>python manage.py createsuperuser</code>
7. Jalankan runserver <code>python manage.py runserver</code>
8. Buka halaman http://127.0.0.1:8000 di browser kesayangan kalian

# Next
1. checkout menuju halaman pembayaran
2. sedang dipikirkan Hahahahaaaaa


# credits

home page template -> https://freehtml5.co/luxe-free-html5-bootstrap-template-for-hotel-website/

login template -> https://bootsnipp.com/snippets/vl4R7

admin : jazzmin