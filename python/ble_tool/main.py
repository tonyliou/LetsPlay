from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import sys
import asyncio
from bleak import BleakScanner
from datetime import datetime


async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)


class Model(object):
    def __init__(self):
        pass

    def func(self, data):
        # return data * 2
        pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText('Hello World!')


class Controller(object):
    def __init__(self):
        self.view = MainWindow()

        self.model = Model()

        self.view.ui.pushButton.clicked.connect(self.buttonClicked)
        self.view.show()

    def buttonClicked(self):
        now = datetime.now()
        self.view.ui.label.setText(str(now))
        loop.run_until_complete(run())  # 按鈕事件驅動放這裡


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    app = QtWidgets.QApplication([])
    con = Controller()
    sys.exit(app.exec_())
