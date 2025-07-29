# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(794, 466)
        Widget.setMinimumSize(QSize(700, 300))
        self.verticalLayoutWidget_3 = QWidget(Widget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 791, 279))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_window_name = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_window_name.setObjectName(u"lineEdit_window_name")

        self.horizontalLayout_2.addWidget(self.lineEdit_window_name)

        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_window_hld = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_window_hld.setObjectName(u"lineEdit_window_hld")

        self.horizontalLayout_2.addWidget(self.lineEdit_window_hld)

        self.pushButton_window = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_window.setObjectName(u"pushButton_window")

        self.horizontalLayout_2.addWidget(self.pushButton_window)

        self.pushButton_main_window = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_main_window.setObjectName(u"pushButton_main_window")

        self.horizontalLayout_2.addWidget(self.pushButton_main_window)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_path = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_path.setObjectName(u"lineEdit_path")

        self.horizontalLayout.addWidget(self.lineEdit_path)

        self.pushButton_liulan = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_liulan.setObjectName(u"pushButton_liulan")

        self.horizontalLayout.addWidget(self.pushButton_liulan)

        self.pushButton_muban = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_muban.setObjectName(u"pushButton_muban")

        self.horizontalLayout.addWidget(self.pushButton_muban)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_qingkong = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_qingkong.setObjectName(u"pushButton_qingkong")

        self.horizontalLayout_3.addWidget(self.pushButton_qingkong)

        self.pushButton_ceshi = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_ceshi.setObjectName(u"pushButton_ceshi")

        self.horizontalLayout_3.addWidget(self.pushButton_ceshi)

        self.pushButton_baocun = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_baocun.setObjectName(u"pushButton_baocun")

        self.horizontalLayout_3.addWidget(self.pushButton_baocun)

        self.pushButton_jiejietupo = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_jiejietupo.setObjectName(u"pushButton_jiejietupo")

        self.horizontalLayout_3.addWidget(self.pushButton_jiejietupo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.textEdit = QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spinBox_huntu = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_huntu.setObjectName(u"spinBox_huntu")

        self.horizontalLayout_4.addWidget(self.spinBox_huntu)

        self.pushButton_huntu = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_huntu.setObjectName(u"pushButton_huntu")

        self.horizontalLayout_4.addWidget(self.pushButton_huntu)

        self.pushButton_huntu_zudui = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_huntu_zudui.setObjectName(u"pushButton_huntu_zudui")

        self.horizontalLayout_4.addWidget(self.pushButton_huntu_zudui)

        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.spinBox_huntu_n = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_huntu_n.setObjectName(u"spinBox_huntu_n")

        self.horizontalLayout_4.addWidget(self.spinBox_huntu_n)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.spinBox_k28 = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_k28.setObjectName(u"spinBox_k28")

        self.horizontalLayout_5.addWidget(self.spinBox_k28)

        self.pushButton_k28 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_k28.setObjectName(u"pushButton_k28")

        self.horizontalLayout_5.addWidget(self.pushButton_k28)

        self.pushButton_k28_zudui = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_k28_zudui.setObjectName(u"pushButton_k28_zudui")

        self.horizontalLayout_5.addWidget(self.pushButton_k28_zudui)

        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.spinBox_k28_n = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_k28_n.setObjectName(u"spinBox_k28_n")

        self.horizontalLayout_5.addWidget(self.spinBox_k28_n)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.spinBox_gbyw = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_gbyw.setObjectName(u"spinBox_gbyw")

        self.horizontalLayout_6.addWidget(self.spinBox_gbyw)

        self.pushButton_gbyw = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_gbyw.setObjectName(u"pushButton_gbyw")

        self.horizontalLayout_6.addWidget(self.pushButton_gbyw)

        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.spinBox_gbyw_n = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_gbyw_n.setObjectName(u"spinBox_gbyw_n")

        self.horizontalLayout_6.addWidget(self.spinBox_gbyw_n)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.spinBox_yuling = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_yuling.setObjectName(u"spinBox_yuling")

        self.horizontalLayout_8.addWidget(self.spinBox_yuling)

        self.pushButton_yuling = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_yuling.setObjectName(u"pushButton_yuling")

        self.horizontalLayout_8.addWidget(self.pushButton_yuling)

        self.label_12 = QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.spinBox_yuling_n = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_yuling_n.setObjectName(u"spinBox_yuling_n")

        self.horizontalLayout_8.addWidget(self.spinBox_yuling_n)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.spinBox_jieqi = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_jieqi.setObjectName(u"spinBox_jieqi")

        self.horizontalLayout_10.addWidget(self.spinBox_jieqi)

        self.pushButton_jieqi = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_jieqi.setObjectName(u"pushButton_jieqi")

        self.horizontalLayout_10.addWidget(self.pushButton_jieqi)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_10.addWidget(self.checkBox_3)

        self.label_13 = QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.spinBox_jieqi_n = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_jieqi_n.setObjectName(u"spinBox_jieqi_n")

        self.horizontalLayout_10.addWidget(self.spinBox_jieqi_n)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 320, 447, 80))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_chakan = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_chakan.setObjectName(u"pushButton_chakan")

        self.horizontalLayout_9.addWidget(self.pushButton_chakan)

        self.pushButton_start = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout_9.addWidget(self.pushButton_start)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_4.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_4.addWidget(self.checkBox_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.pushButton_zanting = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_zanting.setObjectName(u"pushButton_zanting")

        self.horizontalLayout_9.addWidget(self.pushButton_zanting)

        self.pushButton_shanchu = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_shanchu.setObjectName(u"pushButton_shanchu")

        self.horizontalLayout_9.addWidget(self.pushButton_shanchu)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u76ee\u6807\u7a97\u53e3\u540d\u79f0", None))
        self.lineEdit_window_name.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u76ee\u6807\u7a97\u53e3\u53e5\u67c4", None))
        self.pushButton_window.setText(QCoreApplication.translate("Widget", u"\u81ea\u52a8\u83b7\u53d6\u7a97\u53e3\u4fe1\u606f", None))
        self.pushButton_main_window.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e\u4e3b\u7a97\u53e3(\u6253\u624b)", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u6a21\u677f\u5e93\u8def\u5f84", None))
        self.lineEdit_path.setText("")
        self.pushButton_liulan.setText(QCoreApplication.translate("Widget", u"\u6d4f\u89c8", None))
        self.pushButton_muban.setText(QCoreApplication.translate("Widget", u"\u6a21\u677f\u5e93\u81ea\u52a8\u751f\u6210", None))
        self.pushButton_qingkong.setText(QCoreApplication.translate("Widget", u"\u6e05\u7a7a\u8f93\u51fa\u680f", None))
        self.pushButton_ceshi.setText(QCoreApplication.translate("Widget", u"\u6d4b\u8bd5\u6309\u952e", None))
        self.pushButton_baocun.setText(QCoreApplication.translate("Widget", u"\u4fdd\u5b58\u53c2\u6570", None))
        self.pushButton_jiejietupo.setText(QCoreApplication.translate("Widget", u"\u7ed3\u754c\u7a81\u7834", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5355\u5c40\u6218\u6597\u65f6\u957f", None))
        self.pushButton_huntu.setText(QCoreApplication.translate("Widget", u"\u9b42\u571f", None))
        self.pushButton_huntu_zudui.setText(QCoreApplication.translate("Widget", u"\u9b42\u571f-\u7ec4\u961f", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u6267\u884c\u6b21\u6570", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u5355\u5c40\u6218\u6597\u65f6\u957f", None))
        self.pushButton_k28.setText(QCoreApplication.translate("Widget", u"\u56f028", None))
        self.pushButton_k28_zudui.setText(QCoreApplication.translate("Widget", u"\u56f028-\u7ec4\u961f", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u6267\u884c\u6b21\u6570", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u5355\u5c40\u6218\u6597\u65f6\u957f", None))
        self.pushButton_gbyw.setText(QCoreApplication.translate("Widget", u"\u9b3c\u5175\u6f14\u6b66", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u6267\u884c\u6b21\u6570", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u5355\u5c40\u6218\u6597\u65f6\u957f", None))
        self.pushButton_yuling.setText(QCoreApplication.translate("Widget", u"\u5fa1\u7075", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"\u6267\u884c\u6b21\u6570", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u5355\u5c40\u6218\u6597\u65f6\u957f", None))
        self.pushButton_jieqi.setText(QCoreApplication.translate("Widget", u"\u5951\u7075\u7ed3\u5951", None))
        self.checkBox_3.setText(QCoreApplication.translate("Widget", u"\u53ec\u5524", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"\u6267\u884c\u6b21\u6570", None))
        self.pushButton_chakan.setText(QCoreApplication.translate("Widget", u"\u67e5\u770b\u4efb\u52a1", None))
        self.pushButton_start.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u4efb\u52a1", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u4efb\u52a1\u9690\u85cf\u754c\u9762", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"\u7ed3\u675f\u4efb\u52a1\u663e\u793a\u754c\u9762", None))
        self.pushButton_zanting.setText(QCoreApplication.translate("Widget", u"\u6682\u505c\u4efb\u52a1", None))
        self.pushButton_shanchu.setText(QCoreApplication.translate("Widget", u"\u5220\u9664\u4efb\u52a1", None))
    # retranslateUi

