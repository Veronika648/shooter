from PyQt6.QtWidgets import *
from main import *

app = QApplication([])

window = QWidget()

start_btn = QPushButton("start")
shop_btn = QPushButton("shop")
setting_btn = QPushButton("setting")
exit_btn = QPushButton("exit")

main_line = QVBoxLayout()
main_line.addWidget(start_btn)
main_line.addWidget(shop_btn)
main_line.addWidget(setting_btn)
main_line.addWidget(exit_btn)

window.setLayout(main_line)

start_btn.clicked.connect(start_game)
shop_btn.clicked.connect(start_game)
setting_btn.clicked.connect(start_game)
exit_btn.clicked.connect(start_game)

window.show()
app.exec()