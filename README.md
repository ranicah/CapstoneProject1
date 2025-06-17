# Capstone Project 1
Ini adalah penyusunan capstone project CRUD pertama saya dengan topik Nilai Siswa. 

User akan melakukan aksi Create, Read, Update, Delete, dan terdapat tambahan Restore (pemulihan data yang telah terhapus).

# **Create**
Fungsi create ini digunakan user untuk membuat data yang belum ada dalam dataset. User dapat menginputkan variabel-variabel yang telah tersedia sesuai dengan format.

# **Read**
Fungsi read digunakan user untuk melihat keseluruhan dataset nilai siswa dan dapat melihat data nilai siswa secara perseorangan. User dapat menginputkan opsi yang akan dijalankan.

# **Update**
Fungsi update digunakan untuk mengubah data sesuai dengan keinginan user, terutama mengubah daftar nilai siswa yang ingin di-update

# **Delete**
Fungsi delete digunakan untuk menghapus data, dengan memasukkan primary key-nya, user dapat menghapus data sesuai dengan kebutuhan. 

# **Restore**
Fungsi pemulihan data dari data yang telah dihapus. Data yang telah dihapus dapat dilihat ke dalam history dalam fungsi restore. Apabila user ingin memulihkan data yang telah dihapus, user dapat menginputkan NRP(primary key) dari data yang telah dihapus untuk dipulihkan. 

# (Tambahan)
Dalam penginputan primary key dari masing-masing fungsi. User diharuskan untuk memasukkan NRP sesuai dengan format untuk dapat dijalankan ke aksi selanjutnya. Apabila NRP tidak dimasukkan sesuai dengan format, maka akan terjadi looping hingga NRP yang dimasukkan valid agar dapat diproses ke aksi selanjutnya.

