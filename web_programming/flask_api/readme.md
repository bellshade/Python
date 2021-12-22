# Rest API Using Flask
Repositori ini dibuat untuk contoh dasar pembuatan Rest API menggunakan Python dengan library flask.

## Contents
- [Pendahuluan](#Pendahuluan)
    - [Apa Itu Rest API](#apa-itu-rest-api-)
    - [Apa itu Flask](#apa-itu-rest-api-)
    - [TOOls yang digunakan](#tools-yang-digunakan)
    - [Apa yang akan dipelajari](#apa-yang-akan-dipelajari)
- [Pembahasan](#Pembahasan)
    - [Instalasi Requirement](#-instalasi-requirement)
    - [Instalasi Database](#-instalasi-database)
    - [Hello World](#-hello-world)
    - [Membuat URL](#-membuat-url)
    - [Costume URL menggunakan variable](#-costume-url-menggunakan-variabel)
    - [Costume Method](#%EF%B8%8F-costume-method)
    - Menampilkan Data
        - [Menampilkan data dari database](#-menampilkan-data-dari-database)
        - [Menanmpilkan data dari database berdasarkan userid](#-menampilkan-data-dari-database-berdasarkan-userid)
    - Menambah Data
        - [Menambah Data](#-menambahkan-data-ke-database)
    - Mengupdate Data
        - [Mengupdate Data](#-mengupdate-data)
    - Menghapus Data
        - [Menghapus Data](#%EF%B8%8F-menghapus-data)
- [Penutupan](#-penutupan)

## Pendahuluan
### Apa itu Rest API ?
Pertama - tama ketahuilah apa itu API, API atau Application Programming Interface adalah sebuah software yang memungkinkan para developer untuk mengintegrasikan dan mengizinkan dua atau lebih aplikasi yang berbeda secara bersamaan untuk saling terhubung satu sama lain.

Sedangkan Rest API merupakan arsitektur atau desain API tersebut dimana client dapat mengakses data dengan cara mencantumkan id suatu data pada sebuah request, contohnya saya ingin mendapatkan profil suatu user dengan ```id = 1``` maka request yang dikirim adalah ```get profile by user id = 1```.
Nantinya data akan dikirim oleh API ke client dalam bentuk JSON yang secara umum dipakai dalam Rest API.

Adapun metode penggunaan API yaitu :
- GET, berfungsi untuk membaca data/resource dari REST server.
- POST, berfungsi untuk membuat sebuah data/resource baru di REST server.
- PUT, berfungsi untuk memperbaharui data/resource di REST server.
- DELETE, berfungsi untuk menghapus data/resource dari REST serve.
- OPTIONS, berfungsi untuk mendapatkan operasi yang disupport pada resource dari REST server.

### Apa itu Flask ?
Flask adalah kerangka kerja web mikro yang banyak digunakan untuk membuat API dengan Python. Ini adalah kerangka kerja web yang sederhana namun kuat yang dirancang untuk memulai dengan cepat dan mudah, dengan kemampuan untuk meningkatkan aplikasi yang kompleks.

### TOOls yang digunakan
- IDE.
- Browser.
- [Postman][postman].
- Local virtual server (dapat menggunakan [xampp][xampp] maupun [laragon][laragon]).

### Apa yang akan dipelajari
- Membuat return sederhana menggunakan flask.
- Menampilkan data dari database menggunakan postman dan browser.
- Membuat data baru dalam database.
- Mengedit data baru dalam database.
- Menghapus data baru dalam database.

## Pembahasan
### 💡 Instalasi requirement
Untuk menginstall library flask kalian bisa mengetikan.
```
$ pip install flask
```
Sedangkan untuk database saya menggunakan [flask mysql][flaskmysql].
kalian bisa mengintall dengan
```
$ pip install flask-mysqldb
```
Package yang kita gunakan untuk merancang arsitektur rest api adalah flask restful.
```
$ pip install flask_restful
```
### 💾 Instalasi database
Untuk database kalian bisa mengimport contoh database di file [user.sql][contohdatabase], database tersebut akan kita gunakan sebagai penyimpanan.

### 👋 Hello World
Baik sekarang kita mulai membuat return pertama kita ada di contoh file [Hello World][helloworld]
dalam file tersebut kalian perlu mengimport flask kemudian jalankan dan buka ip dan port di halaman browser kalian. [Test][test1]
kalian akan melihat return text 'Hello World', mudah dipahami bukan saat kita membuka ip tersebut flask akan mencari function dan menampilkan return langsung ke halaman browser kalian.

### 🔗 Membuat URL
Selanjutnya kalian dapat membuat costume url sendiri, kalian dapat melihat contoh di file [Costume Url][costumeurl], dalam file tersebut, kita dapat membuka dengan /costumeurl [Test][test2].

### 🔗 Costume URL menggunakan variabel
Bagaimana jika URL yang kalian buat bersifat dinamis atau selalu berubah ?, tenang kalian juga dapat membuat costume url menggunakan variabel, kalian dapat melihat contoh pada file [Costume Url Variable][castumeurlvariable].

### ⌨️ Costume method
Ada beberapa method dalam berinterkasi dengan API, seperti yang dijelaskan di atas, dalam bagian ini kita dapat mengecek method yang dikirimkan [Method][costumemethod].

### 💿 Menampilkan data dari database
Baik setelah kita membahas dasar pembuatan API, kita dapat langsung mencoba untuk menampilkan data yang kita simpan dalam database dengan menggunakan format output json. Pertama buka file contoh [APP][app], disana kita dapat mengubah user dan database yang akan kita akses (dalam kasus ini kita menggunakan database [contoh database][contohdatabase]).
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'remote'
app.config['MYSQL_PASSWORD'] = 'ilham211'
app.config['MYSQL_DB'] = 'contohdatabase'
```
Baik setelah semua disesuaikan, kalian dapat menjalankan file python tersebut, untuk megakses API dapat melakukan seperti pada contoh.

![Get users](/flask_api/image/getuser.gif)

### 📀 Menampilkan data dari database berdasarkan userid.
Untuk menampilkan data kita dapat menggunakan metode costume url yang telah kita buat sebelumnya, kalian dapat melihat pada [APP][app], dimana userid akan kita kirimkan sebagai parameter dalam url.

![Get user by userid](/image/getuserbyuserid.gif)

### 📕 Menambahkan data ke database
Kemudian kita akan menambahkan data ke database sesuai tabel, kalian dapat mengecek pada [APP][app] bagian menambahkan data, untuk menambahkan data kita perlu mendapatkan data yang kita kirim, kita dapat menggunakan fungsi ```request.form``` atau ```request.form.get```, setelah itu data tersebut akan kita masukan ke dalam query menyimpan. Untuk method yang kita gunakan adalah POST.

![Add Data](/image/adddata.gif)

### 📖 Mengupdate data
Setelah menampilkan dan menambahkan data, kita dapat mengupdate data menggunakan API, langkahnya sama dengan menambahkan data, namun query dan data yang kita kirimkan berbeda karena tentunya kita membutuhkan primary key untuk menentukan data mana yang kita update. Kalian bisa melihat contoh pada [APP][app].

![Update Data](/image/updatedata.gif)

### 🗑️ Menghapus data
Selain menambahkan dan mengupdate data kita juga dapat menghapus data, menghapus data prinsipnya sama dengan menampilkan data, method yang kita gunakan adalah delete.

![Update Data](/image/deletedata.gif)

## 😃 Penutupan
Setelah melihat dan mengikuti contoh project rest api menggunakan flask di atas dapat diambil kesimpulan bahwa nantinya kita dapat membuat banyak sekali fungsi yang lebih komplek menggunakan rest api, selain itu karena kita menggunakan bahasa pemrograman python, project yang akan kita kembangkan dapat menggunakan semua package python yang tetunya powerful untuk suatu bahasa pemrograman yang mudah dipahami sebagai backend.

[helloworld]: /contoh/helloworld.py
[costumeurl]: /contoh/costumeurl.py
[postman]: https://www.postman.com/downloads/?utm_source=postman-home
[contohdatabase]: /user.sql
[castumeurlvariable]: /contoh/costumeurlvariable.py
[costumemethod]: /contoh/costmemethod.py
[app]: /contoh/main.py
[flaskmysql]: https://flask-mysqldb.readthedocs.io/en/latest/
[test1]: http://127.0.0.1:2020/
[test2]: http://127.0.0.1:2020/costumeurl
[xampp]: https://www.apachefriends.org/index.html
[laragon]: https://laragon.org/