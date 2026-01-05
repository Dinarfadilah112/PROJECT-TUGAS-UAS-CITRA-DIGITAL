# PROJECT-TUGAS-UAS-CITRA-DIGITAL
Sistem Pengenalan Tulisan Tangan (CNN - EMNIST)
Proyek ini adalah sistem klasifikasi tulisan tangan (huruf dan angka) menggunakan algoritma Convolutional Neural Network (CNN) yang dilatih dengan dataset EMNIST. Proyek ini dioptimalkan untuk dijalankan di Google Colab dan dilengkapi dengan antarmuka pengguna berbasis Gradio.
Panduan Menjalankan Notebook Per-Cell
1. Persiapan Direktori (Mount Drive)
Cell pertama berfungsi untuk menghubungkan Google Colab dengan penyimpanan Google Drive Anda.

Yang dilakukan: Menghubungkan akun Google Drive, berpindah ke folder /citra digital, dan menampilkan daftar file yang ada.

Cara Pakai: Klik tombol Play, lalu ikuti instruksi pop-up untuk memberikan izin akses Google Drive.

2. Pembersihan Cache Dataset (Opsional)
Cell ini sangat berguna jika proses training gagal karena data yang terunduh rusak atau tidak lengkap.

Yang dilakukan: Menghapus folder cache EMNIST di /root/.cache/emnist dan membuatnya kembali dalam keadaan bersih.

Kapan digunakan: Jalankan ini jika Anda mendapatkan error terkait file dataset saat mencoba melakukan training.

3. Instalasi Library EMNIST
Library ini diperlukan untuk memuat dataset karakter tulisan tangan secara otomatis.

Yang dilakukan: Menjalankan perintah !pip install emnist untuk mengunduh library yang dibutuhkan ke dalam environment Colab.

4. Mengunduh Dataset Manual
Terkadang pengunduhan otomatis via library lambat atau terputus. Cell ini memberikan solusi cadangan.

Yang dilakukan: Menggunakan perintah wget untuk mengunduh file dataset gzip.zip langsung dari server NIST seberat kurang lebih 536MB.

Hasil: File akan tersimpan langsung di folder cache yang sudah disiapkan sebelumnya.

5. Pelatihan Model (Training)
Ini adalah inti dari pembuatan sistem kecerdasan buatan Anda.

Yang dilakukan: Menjalankan skrip train.py.

Proses: * Model CNN akan dibangun dengan beberapa lapis (Convolutional, Pooling, dan Dense).

Sistem akan melakukan 10 kali putaran pelatihan (Epoch).

Akurasi akan terpantau meningkat di setiap epoch (terakhir mencapai sekitar 90,53%).

Hasil Akhir: File model_emnist.h5 akan tersimpan di Drive Anda.

Menjalankan Antarmuka Web (Gradio)
Cell terakhir digunakan untuk menjalankan aplikasi agar bisa dicoba secara visual.

Yang dilakukan: Memanggil gradio_app.py yang akan memuat model model_emnist.h5.

Cara Pakai: Setelah dijalankan, cari tulisan "Running on public URL: https://...gradio.live". Klik link tersebut.

Interaksi: Anda bisa langsung menggambar huruf/angka pada kanvas di browser, dan sistem akan memberikan prediksi karakter tersebut.
