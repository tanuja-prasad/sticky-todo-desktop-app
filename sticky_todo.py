import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QColor

# PERSISTANCE STORAGE

APP_DIR = os.path.join(os.environ["APPDATA"], "StickyTodo")
os.makedirs(APP_DIR, exist_ok=True)

DATA_FILE = os.path.join(APP_DIR, "tasks.json")



class StickyTodo(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(370, 480)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(18, 18, 18, 18)
        main_layout.setSpacing(12)

        # -HEADER
        header_layout = QHBoxLayout()

        title = QLabel("To-Do")
        title.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: bold;
        """)

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(30, 30)
        close_btn.clicked.connect(self.close)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff4d4d;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e60000;
            }
        """)

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(close_btn)

        # FOR INPUT
        self.input = QLineEdit()
        self.input.setPlaceholderText("Type a task and press Enter…")
        self.input.returnPressed.connect(self.add_task)
        self.input.setStyleSheet("""
            QLineEdit {
                color: #222;
                background-color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 14px;
            }
            QLineEdit::placeholder {
                color: #666;
                border-radius:10px;
            }
        """)

        # ADD BUTTON
        add_btn = QPushButton("Add Task")
        add_btn.clicked.connect(self.add_task)
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff7a18;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff5c00;
            }
        """)

        #TASKS LIST
        self.list = QListWidget()
        self.list.itemClicked.connect(self.handle_task_click)
        self.list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
            }
            QListWidget::item {
                background-color: white;
                color: #222;
                border-radius: 12px;
                padding: 12px;
                margin-bottom: 8px;
                font-size: 14px;
            }
            QListWidget::item:hover {
                background-color: #f2f2f2;
            }
        """)

       # LAYOUT
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.input)
        main_layout.addWidget(add_btn)
        main_layout.addWidget(self.list)
        self.setLayout(main_layout)

     
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #00c6ff,
                    stop:1 #7f00ff
                );
                border-radius: 24px;
            }
        """)

        # Drag support
        self.oldPos = self.pos()

        # Load tasks
        self.load_tasks()
        self.move_to_right()


    #TASKS LOGIC
    
    


    def add_task(self):
        text = self.input.text().strip()
        if not text:
            return

        item = QListWidgetItem("☐  " + text)
        item.setFont(QFont("Segoe UI", 11))
        self.list.addItem(item)
        self.input.clear()
        self.save_tasks()

    def handle_task_click(self, item):
        text = item.text()
        row = self.list.row(item)

        # MARK DONE
        if text.startswith("☐"):
            item.setText(text.replace("☐", "☑", 1))
            item.setForeground(QColor("#777"))
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)

        # DELETE
        else:
            self.list.takeItem(row)

        self.save_tasks()

    def save_tasks(self):
        tasks = [self.list.item(i).text() for i in range(self.list.count())]
        with open(DATA_FILE, "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    item = QListWidgetItem(task)
                    font = item.font()
                    if task.startswith("☑"):
                        font.setStrikeOut(True)
                        item.setForeground(QColor("#777"))
                    item.setFont(font)
                    self.list.addItem(item)
                    
    def move_to_right(self):
        screen = QApplication.primaryScreen().availableGeometry()
        x = screen.width() - self.width() - 20   # 20px margin from right
        y = (screen.height() - self.height()) // 2  # vertically centered
        self.move(x, y)

    # DRAG

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


# RUN

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StickyTodo()
    window.show()
    sys.exit(app.exec_())
