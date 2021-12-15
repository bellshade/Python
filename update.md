# install python pada linux

install dependencies yang dibutuhkan untuk python versi 3.10
```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

kemudian donwload file python 3.10
```
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz
```
note : **python 3.10 adalah versi stabil dari python 3.10**

kemudian ekstrak file python

```
tar -xf Python-3.10.0.tar.xz
```

kemudian masuk ke folder python lakukan konfigurasi Python-3
```
cd Python-3.10.0 && ./configure --enable-optimizations
```

kemudian lakukan build proses pada python

```
make -j 2
```
disini kita menggunakan 2 core dari cpu untuk test build proses

kemudian lakukan install

```
sudo make altinstall
```

setelah finish lakukan testing pada python versi 3.10

```
python3.10 --version
```

