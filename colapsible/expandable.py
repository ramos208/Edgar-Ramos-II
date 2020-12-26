import sys
from PySide2.QtWidgets import *
import time

class Example(QWidget):

    def __init__(self, ):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        # formatting
        self.setGeometry(300, 300, 300, 300)
        scroll = QScrollArea
        self.setWindowTitle("Example")

        # widgets
        self.controlGroup = QGroupBox()
        self.controlGroup.setTitle("Group")
        self.controlGroup.setCheckable(True)
        self.controlGroup.setChecked(True)

        # groupbox layout
        self.groupLayout = QGridLayout(self.controlGroup)
        self.btn = QPushButton("FOO")
        self.groupLayout.addWidget(self.btn)
        self.controlGroup.setFixedHeight(self.controlGroup.sizeHint().height())


        # signals
        self.controlGroup.toggled.connect(lambda: self.toggleGroup(self.controlGroup))

        self.btn_2 = QPushButton("add",self)
        self.btn_2.clicked.connect(self.add)
        # layout
        self.mainLayout = QGridLayout(self)
        self.mainLayout.addWidget(self.controlGroup)
        self.show()

    def add(self):
        btn_2 = QPushButton("new")
        self.controlGroup.setChecked(False)
        self.groupLayout.addWidget(btn_2)
        self.checked()

    def checked(self):
        if self.controlGroup.isChecked() == True:
            print("True")
            pass
        else:
            self.controlGroup.setChecked(True)
        # self.controlGroup.setChecked(True)
        # self.controlGroup.setFixedHeight(self.controlGroup.sizeHint().height())
    def toggleGroup(self, ctrl):
        state = ctrl.isChecked()
        if state:
            ctrl.setFixedHeight(ctrl.sizeHint().height())
        else:
            ctrl.setFixedHeight(30)


# Main
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())