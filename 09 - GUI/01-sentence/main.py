from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

def  make_sentence():
    input_text = text.text()
    output_label.setText(input_text.upper() + '.')

app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentece Maker')

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)


btn = QPushButton('Make')
layout.addWidget(btn)

output_label = QLabel('')
layout.addWidget(output_label)

btn.clicked.connect(make_sentence)

window.setLayout(layout)
window.show()
app.exec()
