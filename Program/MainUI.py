# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
# 
# Coded by TranTruong
#
# WARNING! All changes made in this file will be lost!


import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
import cv2 as cv
# import face_recognition
import ntpath
# import face_detection
from datetime import datetime
import numpy as np
from time import sleep


cascPath = os.path.abspath("D:/College/Artificial Intelligence/New folder/Project Face Recognition/lib/haarcascade_frontalface_default.xml")
savingPath = os.path.abspath("D:\\College\\Artificial Intelligence\\New folder\\Project Face Recognition\\Images")
count = 1

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 827)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(1)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 751, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 130, 1141, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 210, 1141, 521))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imgIn = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.imgIn.setFont(font)
        self.imgIn.setScaledContents(True)
        self.imgIn.setAlignment(QtCore.Qt.AlignCenter)
        self.imgIn.setObjectName("imgIn")
        self.horizontalLayout_2.addWidget(self.imgIn)
        self.imgOut = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.imgOut.setFont(font)
        self.imgOut.setScaledContents(True)
        self.imgOut.setAlignment(QtCore.Qt.AlignCenter)
        self.imgOut.setObjectName("imgOut")
        self.horizontalLayout_2.addWidget(self.imgOut)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 740, 1141, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnTaiHinhAnh = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnTaiHinhAnh.setFont(font)
        self.btnTaiHinhAnh.setObjectName("btnTaiHinhAnh")
        self.horizontalLayout_3.addWidget(self.btnTaiHinhAnh)
        self.btnXuLy = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnXuLy.setFont(font)
        self.btnXuLy.setObjectName("btnXuLy")
        self.horizontalLayout_3.addWidget(self.btnXuLy)
        self.btnChupAnh = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnChupAnh.setFont(font)
        self.btnChupAnh.setObjectName("btnChupAnh")
        self.horizontalLayout_3.addWidget(self.btnChupAnh)
        self.btnNhanDienAnhRealtime = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnNhanDienAnhRealtime.setFont(font)
        self.btnNhanDienAnhRealtime.setObjectName("btnNhanDienAnhRealtime")
        self.horizontalLayout_3.addWidget(self.btnNhanDienAnhRealtime)
        self.btnLuuHinhAnh = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLuuHinhAnh.setFont(font)
        self.btnLuuHinhAnh.setObjectName("btnLuuHinhAnh")
        self.horizontalLayout_3.addWidget(self.btnLuuHinhAnh)
        self.btnThoat = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnThoat.setFont(font)
        self.btnThoat.setObjectName("btnThoat")
        self.horizontalLayout_3.addWidget(self.btnThoat)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # bắt sự kiện click cho push button
        self.btnTaiHinhAnh.clicked.connect(self.load_image)
        self.btnXuLy.clicked.connect(self.handle_image)
        self.btnLuuHinhAnh.clicked.connect(self.save_image)
        self.btnThoat.clicked.connect(self.quit_program)
        # self.btnThoat.clicked.connect(lambda:self.closeEvent())
        self.btnChupAnh.clicked.connect(self.capture_video)
        self.btnNhanDienAnhRealtime.clicked.connect(self.record_video)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Phần mềm nhận diện khuôn mặt sử dụng thư viện OpenCV"))
        self.label_3.setText(_translate("MainWindow", "Hình ảnh trước xử lý"))
        self.label_5.setText(_translate("MainWindow", "Hình ảnh sau xử lý"))
        self.imgIn.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/imageIn.qrc\"/></p></body></html>"))
        self.imgOut.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/imageIn.qrc\"/></p></body></html>"))
        self.btnTaiHinhAnh.setText(_translate("MainWindow", "Tải hình ảnh"))
        self.btnXuLy.setText(_translate("MainWindow", "Nhận diện khuôn mặt"))
        self.btnChupAnh.setText(_translate("MainWindow", "Chụp ảnh"))
        self.btnNhanDienAnhRealtime.setText(_translate("MainWindow", "Nhận diện khuôn mặt real-time"))
        self.btnLuuHinhAnh.setText(_translate("MainWindow", "Lưu hình ảnh"))
        self.btnThoat.setText(_translate("MainWindow", "Thoát"))
        

    def load_image(self):
        root = tk.Tk()
        root.withdraw()
        # mở hộp thoại để chọn ảnh
        global file_path
        file_path = filedialog.askopenfilename()
        # load ảnh lên và gán vào biến img
        global img 
        img = cv.imread(file_path)
        # set ảnh vào khung hình
        self.imgIn.setPixmap(QPixmap(file_path))
        
    def handle_image(self):
        global faceCascade
        faceCascade = cv.CascadeClassifier(cascPath)
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 5, minSize = (40, 40))
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        saving_path = savingPath + "\\detect_%s"%path_leaf(file_path)
        cv.imwrite(saving_path, img)
        self.imgOut.setPixmap(QPixmap(saving_path))
        os.remove(saving_path)
        
    def save_image(self):
        saving_path = savingPath + "\\detect_%s"%path_leaf(file_path)
        cv.imwrite(saving_path, img)
    
    def quit_program(self):
        cv.VideoCapture(0).release()
        os._exit(0)

    def capture_video(self):
        # real time capture
        global cap
        cap = cv.VideoCapture(0)
        # To use a video file as input 
        # cap = cv.VideoCapture('filename.mp4')
        # while True:
        # Read the frame
        _, img = cap.read()
    
        # Convert to grayscale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
        # Detect the faces
        faces = cv.CascadeClassifier(cascPath).detectMultiScale(gray, 1.3, 4)
        
        if len(faces) == 0:
            self.label.setText("Không tìm thấy khuôn mặt!")
            self.label.setStyleSheet("background-color: blue")
            # sleep(5)
            cap.release()
            # self.label.setText("Phần mềm nhận diện khuôn mặt sử dụng thư viện OpenCV")
            # self.label.setStyleSheet("background-color: lightgreen")
            return
        else:
            self.label.setText("Phần mềm nhận diện khuôn mặt sử dụng thư viện OpenCV")
    
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
        # Display
        cv.imshow("face_detection", img)
        
        # save
        now = datetime.now()
        # cv.imwrite("/Project Face Recognition/Images/detect_face_%s.jpg" %now.strftime("%dd-%mm-%yyyy--%HH-%MM-%SS"), img)
        saving_path = savingPath + "\\face_detect_" + now.strftime("%d-%m-%y--%H-%M-%S") + ".jpg"
        cv.imwrite(saving_path, img)
        self.imgIn.setPixmap(QPixmap(saving_path))
            # Release the VideoCapture object
        cap.release()
    
    def record_video(self):
        # MainWindow.hide()
        self.main_window = QtWidgets.QMainWindow()
        self.main_widget = RealtimeDetection(cascPath)
        self.main_window.setCentralWidget(self.main_widget)
        self.main_window.show()
        # sys.exit(app.exec_())
        
        
class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        self.camera = cv.VideoCapture(camera_port, cv.CAP_DSHOW)

        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        global count
        count = 2
        self.timer.start(0, self)
       

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            self.camera.release()
            return

        read, data = self.camera.read()
        if read:
            self.image_data.emit(data)


class FaceDetectionWidget(QtWidgets.QWidget):
    def __init__(self, haar_cascade_filepath, parent=None):
        super().__init__(parent)
        self.classifier = cv.CascadeClassifier(haar_cascade_filepath)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)

    def detect_faces(self, image: np.ndarray):
        # haarclassifiers work better in black and white
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray_image = cv.equalizeHist(gray_image)

        faces = self.classifier.detectMultiScale(gray_image,
                                                 scaleFactor=2,
                                                 minNeighbors=4,
                                                 flags=cv.CASCADE_SCALE_IMAGE,
                                                 minSize=self._min_size)

        return faces

    def image_data_slot(self, image_data):
        faces = self.detect_faces(image_data)
        for (x, y, w, h) in faces:
            cv.rectangle(image_data,
                          (x, y),
                          (x+w, y+h),
                          self._red,
                          self._width)

        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())

        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()


class RealtimeDetection(QtWidgets.QWidget):
    def __init__(self, haarcascade_filepath, parent=None):
        super().__init__(parent)
        fp = haarcascade_filepath
        self.face_detection_widget = FaceDetectionWidget(fp)

        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.face_detection_widget)
        self.run_button = QtWidgets.QPushButton('Start')
        layout.addWidget(self.run_button)

        self.run_button.clicked.connect(self.record_video.start_recording)
        self.setLayout(layout)
    
        
if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())