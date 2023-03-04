from PyQt5.QtWidgets import QApplication
import sys
import ui
from connection import Connection
from threading import Thread

def main():
    conec = Connection()

    app = QApplication(sys.argv)
    window = ui.Window(conec)

    print("debug")

    Thread(target=conec.receber, args = [window]).start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()