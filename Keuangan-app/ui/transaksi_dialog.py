from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout,
    QLineEdit, QComboBox, QTextEdit,
    QPushButton, QDateEdit
)
from PySide6.QtCore import QDate
from PySide6.QtGui import QIntValidator

from database.db import insert_transaksi, update_transaksi


class TransaksiDialog(QDialog):
    def __init__(self, data=None):
        super().__init__()
        self.data = data
        if self.data:
            self.setWindowTitle("Edit Transaksi")
        else:
            self.setWindowTitle("Tambah Transaksi")

        self.init_ui()

        if self.data:
            self.load_data()

    def init_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # tanggal
        self.input_tanggal = QDateEdit()
        self.input_tanggal.setDate(QDate.currentDate())

        # jenis
        self.input_jenis = QComboBox()
        self.input_jenis.addItems(["Pemasukan", "Pengeluaran"])

        # kategori
        self.input_kategori = QLineEdit()

        # jumlah (VALIDASI + FORMAT)
        self.input_jumlah = QLineEdit()
        self.input_jumlah.setValidator(QIntValidator(0, 1000000000))
        self.input_jumlah.textChanged.connect(self.format_rupiah)

        # deskripsi
        self.input_deskripsi = QTextEdit()

        form_layout.addRow("Tanggal:", self.input_tanggal)
        form_layout.addRow("Jenis:", self.input_jenis)
        form_layout.addRow("Kategori:", self.input_kategori)
        form_layout.addRow("Jumlah:", self.input_jumlah)
        form_layout.addRow("Deskripsi:", self.input_deskripsi)

        layout.addLayout(form_layout)

        # tombol
        if self.data:
            self.btn_simpan = QPushButton("Update")
        else:
            self.btn_simpan = QPushButton("Simpan")
        layout.addWidget(self.btn_simpan)

        self.btn_simpan.clicked.connect(self.simpan_data)

        self.setLayout(layout)

    # =========================
    # FORMAT RUPIAH
    # =========================
    def format_rupiah(self, text):
        if text == "":
            return

        angka = ''.join(filter(str.isdigit, text))

        if angka == "":
            self.input_jumlah.setText("")
            return

        formatted = "Rp " + "{:,}".format(int(angka)).replace(",", ".")

        self.input_jumlah.blockSignals(True)
        self.input_jumlah.setText(formatted)
        self.input_jumlah.blockSignals(False)

    # =========================
    # LOAD DATA (EDIT MODE)
    # =========================
    def load_data(self):
        self.input_tanggal.setDate(QDate.fromString(self.data[1], "yyyy-MM-dd"))
        self.input_jenis.setCurrentText(self.data[2])
        self.input_kategori.setText(self.data[3])

        jumlah_str = str(self.data[4])
        jumlah = int(''.join(filter(str.isdigit, jumlah_str)))

        formatted = "Rp {:,}".format(jumlah).replace(",", ".")
        self.input_jumlah.setText(formatted)

        self.input_deskripsi.setPlainText(self.data[5])

    # =========================
    # SIMPAN DATA
    # =========================
    def simpan_data(self):
        tanggal = self.input_tanggal.text()
        jenis = self.input_jenis.currentText()
        kategori = self.input_kategori.text()
        jumlah_text = self.input_jumlah.text()
        deskripsi = self.input_deskripsi.toPlainText()

        if not kategori or not jumlah_text:
            return

        jumlah = int(''.join(filter(str.isdigit, jumlah_text)))

        if self.data:
            id = self.data[0]
            update_transaksi(id, tanggal, jenis, kategori, jumlah, deskripsi)
        else:
            insert_transaksi(tanggal, jenis, kategori, jumlah, deskripsi)

        self.accept()