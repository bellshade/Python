# A. Regular Expression

Regular Expression adalah sekumpulan karakter yang membentuk suatu pola pencarian

# B. Regular Expression Special Sequences
<table border=1>
  <tr align="center">
    <td>Special Sequences</td>
    <td>Arti</td>
  </tr>
  <tr align="center">
    <td>\d</td>
    <td>Bilangan Bulat / Digit (0-9)</td>
  </tr>
  <tr align="center">
    <td>\s</td>
    <td>Spasi / Withspace</td>
  </tr>
  <tr align="center">
    <td>\w</td>
    <td>Alphabet (A-Za-z), Digit (0-9), dan '_' (garis bawah)</td>
  </tr>
</table>

# C. Regular Expression Metacharacters
<table border=1>
  <tr align="center">
    <td>Metacharacters</td>
    <td>Arti</td>
  </tr>
  <tr align="center">
    <td>+</td>
    <td>Apabila special sequences yang diinginkan muncul sekali ataupun lebih dari satu</td>
  </tr>
  <tr align="center">
    <td>*</td>
    <td>Apabila special sequences yang diinginkan tidak muncul ataupun lebih dari satu</td>
  </tr>
  <tr align="center">
    <td>[]</td>
    <td>Menspesifikasikan pola / special sequences yang diinginkan</td>
  </tr>
  <tr align="center">
    <td>{}</td>
    <td>Menspesifikasikan kemunculan dari special sequences tersebut</td>
  </tr>
  <tr align="center">
    <td>|</td>
    <td>Pernyataan logika OR pada Regex</td>
  </tr>
</table>

# D. Regular Expression Set Example
<table border=1>
  <tr align="center">
    <td>Sets</td>
    <td>Arti</td>
  </tr>
  <tr align="center">
    <td>[A-Z]</td>
    <td>Hanya menerima alphabet berupa huruf besar semua</td>
  </tr>
  <tr align="center">
    <td>[a-z]</td>
    <td>Menerima alphabet huruf kecil</td>
  </tr>
  <tr align="center">
    <td>[abc]</td>
    <td>Hanya huruf abc</td>
  </tr>
  <tr align="center">
    <td>[0-9]</td>
    <td>Bilangan digit dari 0 sampai 9</td>
  </tr>
</table>

# E. Reguler Expression Function
## 1. Findall
Findall adalah sebuah fungsi dimana fungsi tersebut mengembalikan kecocokan antara sequences atau pola yang kita inginkan dengan text yang akan dicari
## 2. Sub
Sub adalah sebuah fungsi dimana fungsi tersebut mengganti sequences yang kita cari dengan sequences / kata baru
## 3. Search
Search adalah sebuah fungsi dimana fungsi tersebut mencari object yang kita inginkan pada kata yang akan kita eksekusi
## 4. Split
Split adalah sebuah fungsi dimana fungsi itu memecah / membagi kalimat yang akan dieksekusi berdasarkan sebuah pola
