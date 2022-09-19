# Assignment-Zenius
Essay about Data Science Use Cases in Banking with title "Prediksi Perilaku Konsumen Retail" pada (Studi Kasus : Mini Market di Kampus XY)

**Prediksi Perilaku Konsumen Retail (Studi Kasus : Mini Market di Kampus XY)**

**1. Pendahuluan**

   Pertumbuhan bisnis ritel berkembang cukup pesat di Indonesia. Menurut data dari Bank Indonesia (BI), kinerja penjualan ritel atau eceran menguat pada Maret 2022 dibanding bulan sebelumnya. Hal ini tercermin dari Indeks Penjualan Riil (IPR) yang mencapai level 205,3 per Maret 2022, tumbuh 2,6% dari level 200 pada Februari 2022 (month-to-month/m-to-m). Bisnis ritel cukup mempunyai peran penting dalam perekonomian tiap negara. Industri ritel di Indonesia memberikan kontribusi yang besar terhadap Produk Domestik Bruto (PDB) dan juga menyerap tenaga kerja dalam jumlah yang besar.
    
   Ritel merupakan penjualan produk atau jasa kepada konsumen dalam skala kecil atau eceran untuk memenuhi kebutuhan konsumen. Proses transaksinya dapat dilakukan di mana saja, baik melalui toko fisik maupun toko online. Bisnis ritel ini sebagai penghubung antara pihak pabrik dan konsumen. Berdasarkan sifatnya, ritel di indonesia terbagi atas 2, yaitu ritel yang bersifat tradisional atau konvensional dan ritel yang bersifat modern.
    
   Kehadiran industri ritel modern pada dasarnya memanfaatkan pola belanja masyarakat terutama kelas menengah ke atas yang tidak mau berdesak-desakan di dalam pasar tradisional yang biasanya becek atau tidak tertata rapi. Walaupun kehadiran ritel modern ini disoroti dapat mematikan pasar tradisional karena mempunyai keunggulan pada banyak faktor, perkembangannya sendiri dapat dikatakan tidak terbendung.

**2. Pembahasan dan Metodologi**

Berikut adalah contoh penerapan Framework CRISP-DM terhadap perilaku pelanggan mini market di kampus XY, seperti yang dijelaskan pada jurnal e-Proceeding of Engineering:

1. *Business Understanding Phase*

    Terdapat sebuah mini market di kampus XY yang dibangun untuk dapat memenuhi kebutuhan sehari-hari mahasiswa. Data transaksi memberikan informasi barang-barang yang terjual. Selain itu, data transaksi digunakan untuk pembuatan rekap bulanan yang berkaitan dengan hasil penjualan perusahaan. Manfaat data transaksi ini dapat memberikan pertimbangan terhadap strategi penjualan pada bulan berikutnya. Dalam data mining, terdapat analisis asosiasi yang berguna untuk menganalisis data transaksi. Asosiasi berarti mencari kombinasi antar barang dalam transaksi yang telah terjadi.

2. *Data Understanding Phase*

    Terdapat total 4692 data, sesuai dengan transaksi yang terjadi pada Januari 2014. Data transaksi yang diambil merupakan Data Penjualan mini market di kampus XY. Rincian besar data transaksi penjualan per bulan yang terjadi dari mini market tersebut bisa dilihat di tabel dibawah ini.
    
   |Bulan|Jumlah|NoTransaksi Awal|NoTransaksi Akhir|
   | Januari |4692|1|4692|
   |Februari|12886|4693|17578|
   |TOTAL|17578|~|~|

3. *Data Preparation Phase*

Fase persiapan data terdiri dari langkah-langkah berikut ini : 

   1)	*Data Cleaning*
    
   Atribut yang dapat dipangkas yang tidak digunakan dalam analisis antara lain
   |NO|Atribut|Value|
   |1|Kode|Numerik|
   |2|Harga|Numerik|
   |3|Jumlah|Numerik|
   |4|Subtotal|Numerik|
   
   2)	*Construct Data*

   Atribut baru yang bisa dibuat antara lain NoTransaksi dari NoJual dan Tanggal dari tanggal yang tercantum di tiap transaksi.
   
   3)	*Data Transformation*
   
   Pada Data Transformation format data yang digunakan dari .xls. format datanya diubah menjadi .csv dengan tujuan mempermudah input ke dalam database.
   
 4.	*Modelling Phase*

    Pada Modelling Phase ini menggunakan Pseudocode algoritma Apriori. Sistem dimulai dari input support dan confidence. Input digunakan untuk pemangkasan dalam proses mendapatkan frequent itemset. Setelah input dilakukan, proses selanjutnya adalah pembuatan frequent 1-itemset. Frequent 1-itemset menentukan pembangkitan frequent k-itemset. Pembangkitan frequent k-itemset berakhir bila sudah tidak ada lagi itemset yang dihasilkan. Bila Frequent Itemset sudah didapat proses selanjutnya adalah pembangkitan aturan asosiasi atau Association Rules. Pembangkitan kandidat Association Rules akan berakhir bila tidak ada lagi kandidat yang dihasilkan.
    
5. *Evaluation*

    Dari pemodelan yang telah dilakukan pada fase sebelumnya, dilakukan implementasi sistem pada Bahasa Pemrograman Java. Hasil berdasarkan rules yang terbentuk pada tiap bulan relative berbeda. Berikut hasil yang rulesyang ada pada Bulan Januari dan Bulan Februari. Tabel dan grafik di bawah ini dihasilkan dari minsup 0.004 dan minconf 0.1 :
    
   |Rules|Support|Confidence|
   |[Ades 1.5 Lt]=>[Amidis Galon 19 Ltr]|0.00683|0.19135802|
   |[Risoles Ayam/ Risol]=>[Soes / Martabak/ Gehu Pedas /Cente /Puding Manis/ Pisang ]|0.00529|0.35820896|
   |[Soes / Martabak/ Gehu Pedas/ Cente/ Puding Manis/ Pisang ]=>[Risoles Ayam/ Risol]|	0.00529|0.18045113|
   |[Sari Roti Sandwich Coklat]=>[Sari Roti Sandwich Keju]|0.00506|0.14465409| 
   |[Sari Roti Sandwich Keju]=>[Sari Roti Sandwich Coklat]|0.00506|0.29487179|
   
6.	*Deployment*

   Dalam tahapan penyebaran data mining dapat dilakukan pada semua jualan yang ada di Kampus XY. Pada penelitian ini tahapan deployment atau tahap penyebaran tidak dilakukan.

**Kesimpulan**

   Dalam tahapan penyebaran data mining dapat dilakukan pada semua jualan yang ada di Kampus XY. Pada penelitian ini tahapan deployment atau tahap penyebaran tidak dilakukan.  
    
Berdasarkan hasil penelitian yang dilakukan, dapat diambil simpulan sebagai berikut: 
1.	Metodologi CRISP-DM dapat diterapkan untuk melakukan prediksi Perilaku Pelanggan Mini Market di Kampus XY
2.	Pengaruh jumlah database transaksi dengan waktu komputasi menunjukkan bahwa semakin banyak data yang dianalisis, semakin lama waktu yang dibutuhkan.
3.	Hasil rules yang dihasilkan menunjukkan kombinasi item yang berbeda setiap bulannya walaupun menggunakan nilai parameter yang sama
