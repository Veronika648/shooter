from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from file_helper import read_file, save_file


def buy_item(price, img):
    data = read_file()
    if data["money"] >= price:
        data["skin"] = img
        data["money"] -= price
        save_file(data)
    else:
        print("Немає грошей")
def shop_window():
    window = QDialog()
    elements = [
        {
            "name": "test1",
            "img": "hero.png",
            "price": 100
        }
    ]

    main_line = QHBoxLayout()
    for element in elements:
        ver = QVBoxLayout()
        name_lbl = QLabel(element["name"])
        img_lbl = QLabel()
        img_pm = QPixmap(element["img"])
        img_pm = img_pm.scaledToWidth(100)
        img_lbl.setPixmap(img_pm)
        price_lbl = QLabel(str(element["price"]))
        buy_btn = QPushButton("Купити")
        buy_btn.clicked.connect(lambda _,
                                       price=element["price"],
                                       img=element["img"]: buy_item(price,
                                                                    img) )
        ver.addWidget(name_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(price_lbl)
        ver.addWidget(buy_btn)
        main_line.addLayout(ver)
    window.setLayout(main_line)
    window.show()
    window.exec()