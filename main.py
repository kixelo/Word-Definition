from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QLineEdit
from PyQt6.QtCore import Qt
import json

data = json.load(open("data.json"))

def convert_word(w):
    w = text.text()
    w = w.lower()
    if w in data:
        output=data[w]
        output_label.setText('\n'.join(output))

    elif w.title() in data:
        w = w.title()
        output=data[w]
        output_label.setText('\n'.join(output))

    elif w.upper() in data:
        w = w.upper()
        output=data[w]
        output_label.setText('\n'.join(output))

    else:
        output_label.setText("The word does not exist. Please double check it.")

#def convert_word():
#    input_text=text.text()
#   word=en_thesaurus(input_text)
#   output='\n'.join(word)
#   output_label.setText(str(output))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Word definition')

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

output_label = QLabel('')
layout.addWidget(output_label)

text = QLineEdit()
layout2.addWidget(text, alignment=Qt.AlignmentFlag.AlignLeft)

convert_btn = QPushButton('Convert')
layout3.addWidget(convert_btn)
convert_btn.clicked.connect(convert_word)

window.setLayout(layout)
window.show()
app.exec()
