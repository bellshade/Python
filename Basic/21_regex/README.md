# A. Regular Expression

Regular Expression adalah sekumpulan karakter yang membentuk suatu pola pencarian

# B. Regular Expression Special Sequences
| Special Sequences   | Arti                                                  |
|---------------------|-------------------------------------------------------|
| \d                  | Bilangan Bulat / Digit (0-9)                          |
| \s                  | Spasi / Whitespace                                    |
| \w                  | Alphabet (A-Za-z), Digit (0-9), dan '-' (garis bawah) |

# C. Regular Expression Metacharacters
| Metacharacters   | Arti                                                                            |
|------------------|---------------------------------------------------------------------------------|
| +                | Apabila special sequences yang diinginkan muncul sekali ataupun lebih dari satu |
| *                | Apabila special sequences yang diinginkan tidak muncul ataupun lebih dari satu  |
| []               | Menspesifikasikan pola / special sequences yang diinginkan                      |
| {}               | Menspesifikasikan kemunculan dari special sequences tersebut                    |
| |                | Pernyataan logika OR pada Regex                                                 |

# D. Regular Expression Set Example
| Set   | Arti                                             |
|-------|--------------------------------------------------|
| [A-Z] | Hanya menerima alphabet berupa huruf besar semua |
| [a-z] | Menerima alphabet huruf kecil                    |
| [abc] | Hanya huruf abc                                  |
| [0-9] | Bilangan digit dari 0 sampai 9                   |
| [1-5] | Hanya menerima bilangan digit dari 1 sampai 5    |

# E. Reguler Expression Function
## 1. Findall
Findall adalah sebuah fungsi dimana fungsi tersebut mengembalikan kecocokan antara sequences atau pola yang kita inginkan dengan text yang akan dicari.
## 2. Sub
Sub adalah sebuah fungsi dimana fungsi tersebut mengganti sequences yang kita cari dengan sequences / kata baru.
## 3. Search
Search adalah sebuah fungsi dimana fungsi tersebut mencari object yang kita inginkan pada kata yang akan kita eksekusi.
## 4. Split
Split adalah sebuah fungsi dimana fungsi itu memecah / membagi kalimat yang akan dieksekusi berdasarkan sebuah pola.

[Materi Selanjutnya](../22_scope)