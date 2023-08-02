from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate

def  show_currency():
    input_text = float(text.text())
    in_cur = in_combo.currentText()
    out_cur = out_combo.currentText()
    rate = input_text * get_currency(in_cur, out_cur)
    message = f'{input_text} {in_cur} is {rate} {out_cur}'
    output_label.setText(message)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency converter')

currencies = ['USD', 'EUR', 'INR']


layout = QVBoxLayout()

in_combo = QComboBox()
in_combo.addItems(currencies)
layout.addWidget(in_combo)

out_combo = QComboBox()
out_combo.addItems(currencies)
layout.addWidget(out_combo)

text = QLineEdit()
layout.addWidget(text)


btn = QPushButton('Convert')
layout.addWidget(btn)

output_label = QLabel('')
layout.addWidget(output_label)

btn.clicked.connect(show_currency)

window.setLayout(layout)
window.show()
app.exec()
