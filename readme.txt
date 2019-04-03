Cara penggunaan Aplikasi CLI (command line interface) fruit classification

1. Sebelum menjalankan aplikasi, pastikan package-package yang terdapat pada file requirements.txt sudah terinstall
2. Ketik python pada terminal diikuti dengan nama file python (index.py) diikuti dengan input setting(train/test) dan file yang akan diproses
3. Untuk melakukan training model, maka penggunaan aplikasinya adalah sebagai berikut : "python index.py train fruit_data_with_colors.txt", 
    dengan "train" adalah input setting untuk pembuatan model dan "fruit_data_with_colors.txt" adalah data yang akan dimodelkan
4. Proses training model akan menghasilkan dua file yaitu file model (knn_mod.joblib) dan file test (X_test.txt)
5. Jalankan test untuk menguji kemampuan model mengklasifikasi jenis buah dengan cara sebagai berikut :
    "python index.py test X_test.txt" dengan "test" adalah input setting dan X_test.txt adalah file berisi spesifikasi buah yang akan diklasifikasi
6. Proses test bisa dijalankan jika training sudah dijalankan terlebih dahulu demi menghasilkan file model dan file test
7. Jika input setting tidak dipanggil sebagai "train" atau "test" maka aplikasi akan memberi peringatan saat dijalankan
8. Happy Learning

