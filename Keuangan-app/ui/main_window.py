from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QTableWidget, QLabel,
    QTableWidgetItem, QMessageBox
)
from PySide6.QtWidgets import QMenuBar, QMenu, QHeaderView
from PySide6.QtGui import QAction
from database.db import get_all_transaksi, delete_transaksi
from ui.transaksi_dialog import TransaksiDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Keuangan Sederhana")
        self.setGeometry(100, 100, 800, 500)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # label nama & nim
        self.label_info = QLabel("Nama: [Arya Rayan Utama] | NIM: [F1D02310106]")
        layout.addWidget(self.label_info)

        # tabel
        self.table = QTableWidget()
        from PySide6.QtWidgets import QHeaderView
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Tanggal", "Jenis", "Kategori", "Jumlah", "Deskripsi"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        # tombol
        self.btn_tambah = QPushButton("Tambah")
        self.btn_edit = QPushButton("Edit")
        self.btn_hapus = QPushButton("Hapus")
        
        # set nama objek untuk styling
        self.btn_tambah.setObjectName("btnTambah")
        self.btn_edit.setObjectName("btnEdit")
        self.btn_hapus.setObjectName("btnHapus")

        # koneksi tombol
        self.btn_tambah.clicked.connect(self.buka_dialog_tambah)
        self.btn_edit.clicked.connect(self.edit_data)
        self.btn_hapus.clicked.connect(self.hapus_data)

        # tambahkan ke layout
        layout.addWidget(self.btn_tambah)
        layout.addWidget(self.btn_edit)
        layout.addWidget(self.btn_hapus)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # menu bar
        menubar = self.menuBar()

        menu_help = menubar.addMenu("Help")

        action_tentang = QAction("Tentang Aplikasi", self)
        action_tentang.triggered.connect(self.tampilkan_tentang)

        menu_help.addAction(action_tentang)

        # load data awal
        self.load_data()

    # =========================
    # TAMBAH DATA
    # =========================
    def buka_dialog_tambah(self):
        dialog = TransaksiDialog()
        dialog.exec()

        # refresh tabel setelah tambah
        self.load_data()

    # =========================
    # LOAD DATA KE TABEL
    # =========================
    def load_data(self):
        data = get_all_transaksi()
        self.table.setRowCount(len(data))

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):

                # format kolom jumlah
                if col_index == 4:
                    formatted = "Rp {:,}".format(int(col_data)).replace(",", ".")
                    item = QTableWidgetItem(formatted)
                else:
                    item = QTableWidgetItem(str(col_data))

                self.table.setItem(row_index, col_index, item)

    # =========================
    # HAPUS DATA
    # =========================
    def hapus_data(self):
        selected_items = self.table.selectedItems()

        if not selected_items:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu!")
            return

        selected_row = self.table.row(selected_items[0])
        id = self.table.item(selected_row, 0).text()

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin menghapus data?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            delete_transaksi(id)
            self.load_data()
    
    def edit_data(self):
        selected_items = self.table.selectedItems()

        if not selected_items:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu!")
            return

        selected_row = self.table.row(selected_items[0])

        data = []
        for col in range(6):
            item = self.table.item(selected_row, col)
            data.append(item.text())

        dialog = TransaksiDialog(data)
        dialog.exec()

        self.load_data()       
        
    def tampilkan_tentang(self):
        QMessageBox.information(
            self,
            "Tentang Aplikasi",
            "Aplikasi Manajemen Keuangan\n\n"
            "Digunakan untuk mencatat pemasukan dan pengeluaran.\n\n"
            "Nama: [Arya Rayan Utama]\n"
            "NIM: [F1D02310106]"
        ) 