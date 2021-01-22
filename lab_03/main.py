from mygui import *
import sys


def main():
    app = QApplication([])
    application = myWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
