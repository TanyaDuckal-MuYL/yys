import sys
import os
import win32gui
import time
from pynput import mouse
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import QThread, QMutex, Qt
from ui_form import Ui_Widget
# Important
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# pyinstaller -F widget.py linklist.py yys_work.py --hidden-import PySide6.QtSvg --paths  c:\users\22953\appdata\local\programs\python\python38\lib\site-packages\shiboken6.abi3.dll -w --exclude PyQt5

#引入工作任务类
import yys_work
#引入数据结构链表
import linklist
#程序窗口
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #链表创建
        self.linklist = linklist.LinkList()
        #线程锁创建
        self.mutex = QMutex()
        self.thread = None
        # 保存初始的窗口标志
        self.original_flags = self.windowFlags()
        #程序窗口控件设置
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        # self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        # self.ui.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        #设置输出控件背景文案显示
        self.ui.textEdit.setPlaceholderText("应用程序输出")
        #修改计数器范围
        self.ui.spinBox_huntu_n.setRange(0,999)
        self.ui.spinBox_k28_n.setRange(0,999)
        self.ui.spinBox_gbyw_n.setRange(0,999)
        self.ui.spinBox_yuling_n.setRange(0,999)
        self.ui.spinBox_jieqi.setRange(0,999)
        self.ui.spinBox_jieqi_n.setRange(0,999)
        self.ui.spinBox_pata.setRange(0,999)
        self.ui.spinBox_pata_n.setRange(0,999)
        #待开发按键
        self.ui.pushButton_muban.setEnabled(False)
        self.ui.pushButton_jiejietupo.setEnabled(False)
        self.ui.pushButton_zanting.setEnabled(False)
        #按键点击事件链接到相应槽函数
        self.ui.pushButton_huntu.clicked.connect(self.on_button_huntu_click)
        self.ui.pushButton_k28.clicked.connect(self.on_button_k28_click)
        self.ui.pushButton_gbyw.clicked.connect(self.on_button_gbyw_click)
        self.ui.pushButton_ceshi.clicked.connect(self.on_button_ceshi_click)
        self.ui.pushButton_qingkong.clicked.connect(self.on_button_qingkong_click)
        self.ui.pushButton_window.clicked.connect(self.on_button_window_click)
        self.ui.pushButton_baocun.clicked.connect(self.on_button_baocun_click)
        self.ui.pushButton_liulan.clicked.connect(self.on_button_liulan_click)
        self.ui.pushButton_muban.clicked.connect(self.on_button_muban_click)
        self.ui.pushButton_jiejietupo.clicked.connect(self.on_button_jiejietupo_click)
        self.ui.pushButton_yuling.clicked.connect(self.on_button_yuling_click)
        self.ui.pushButton_chakan.clicked.connect(self.on_button_chakan_click)
        self.ui.pushButton_start.clicked.connect(self.on_button_start_click)
        self.ui.pushButton_zanting.clicked.connect(self.on_button_zanting_click)
        self.ui.pushButton_shanchu.clicked.connect(self.on_button_shanchu_click)
        self.main_window_seted = "0"
        self.ui.pushButton_main_window.clicked.connect(self.on_button_main_window_click)
        self.ui.pushButton_huntu_zudui.clicked.connect(self.on_button_huntu_zudui_click)
        self.ui.pushButton_k28_zudui.clicked.connect(self.on_button_k28_zudui_click)
        self.ui.pushButton_jieqi.clicked.connect(self.on_button_jieqi_click)
        self.ui.pushButton_pata.clicked.connect(self.on_button_pata_click)
        self.ui.checkBox_4.stateChanged.connect(self.toggle_stay_on_top)
        #创建文件用于记录目标窗口句柄
        if os.path.exists("hld.txt") == False:
            self.file = open("hld.txt","x")
            self.file.close()
            pass
        #文件io读取用户数据
        if os.path.exists("data_path.txt") == False:
            self.file = open("data_path.txt","x")
            self.file.close()
            pass
        self.file = open("data_path.txt","r+",encoding="utf-8")
        self.lines = self.file.readlines()
        self.file.close()
        #将保存数据输入到控件
        if len(self.lines) >= 0:
            self.ui.lineEdit_window_name.setText(self.lines[0][:-1])
            self.ui.lineEdit_window_hld.setText(self.lines[1][:-1])
            self.ui.lineEdit_path.setText(self.lines[2][:-1])
            self.ui.spinBox_huntu.setValue(int(self.lines[3]))
            self.ui.spinBox_huntu_n.setValue(int(self.lines[4]))
            self.ui.spinBox_k28.setValue(int(self.lines[5]))
            self.ui.spinBox_k28_n.setValue(int(self.lines[6]))
            self.ui.spinBox_gbyw.setValue(int(self.lines[7]))
            self.ui.spinBox_gbyw_n.setValue(int(self.lines[8]))
            self.ui.spinBox_yuling.setValue(int(self.lines[9]))
            self.ui.spinBox_yuling_n.setValue(int(self.lines[10]))
            self.ui.spinBox_jieqi.setValue(int(self.lines[11]))
            self.ui.spinBox_jieqi_n.setValue(int(self.lines[12]))
            self.ui.spinBox_pata.setValue(int(self.lines[13]))
            self.ui.spinBox_pata_n.setValue(int(self.lines[14]))
            pass
        pass
    #根据复选框状态切换窗口置顶
    def toggle_stay_on_top(self, state):
        stay_on_top = state
        self.set_stay_on_top(stay_on_top)
        pass
    #设置窗口是否置顶
    def set_stay_on_top(self,stay_on_top):
        if stay_on_top:
            self.setWindowFlags(self.original_flags | Qt.WindowStaysOnTopHint)
            self.show()
            pass
        else:
            self.setWindowFlags(self.original_flags)
            self.show()
            pass
        pass
    #封装参数到字典方便传参
    def set_dictionary(self):
        jieqi_zhaohuan = 0
        if self.ui.checkBox_3.isChecked():
            jieqi_zhaohuan = 1
            pass
        self.dictionary = {'run_name':"",
        'main_window_hld':self.main_window_seted,
        'window_name':self.ui.lineEdit_window_name.text(),
        'hld':self.ui.lineEdit_window_hld.text(),
        'path':self.ui.lineEdit_path.text(),
        'Duration_of_battle_h11':self.ui.spinBox_huntu.value(),
        'Duration_of_battle_h11_n':self.ui.spinBox_huntu_n.value(),
        'Duration_of_battle_k28':self.ui.spinBox_k28.value(),
        'Duration_of_battle_k28_n':self.ui.spinBox_k28_n.value(),
        'Duration_of_battle_gbyw':self.ui.spinBox_gbyw.value(),
        'Duration_of_battle_gbyw_n':self.ui.spinBox_gbyw_n.value(),
        'Duration_of_battle_yuling':self.ui.spinBox_yuling.value(),
        'Duration_of_battle_yuling_n':self.ui.spinBox_yuling_n.value(),
        'Duration_of_battle_jieqi':self.ui.spinBox_jieqi.value(),
        'Duration_of_battle_jieqi_n':self.ui.spinBox_jieqi_n.value(),
        'jieqi_zhaohuan':jieqi_zhaohuan,
        'Duration_of_battle_pata':self.ui.spinBox_pata.value(),
        'Duration_of_battle_pata_n':self.ui.spinBox_pata_n.value(),
        }
        pass
    #保存参数
    def on_button_baocun_click(self):
        self.pushbutton_setenabled(False)
        self.ui.textEdit.append("数据保存中...")
        self.file = open("data_path.txt","w+",encoding="utf-8")
        self.file.write(self.ui.lineEdit_window_name.text()+"\n")
        self.file.write(self.ui.lineEdit_window_hld.text()+"\n")
        self.file.write(self.ui.lineEdit_path.text()+"\n")
        self.file.write(str(self.ui.spinBox_huntu.value())+"\n")
        self.file.write(str(self.ui.spinBox_huntu_n.value())+"\n")
        self.file.write(str(self.ui.spinBox_k28.value())+"\n")
        self.file.write(str(self.ui.spinBox_k28_n.value())+"\n")
        self.file.write(str(self.ui.spinBox_gbyw.value())+"\n")
        self.file.write(str(self.ui.spinBox_gbyw_n.value())+"\n")
        self.file.write(str(self.ui.spinBox_yuling.value())+"\n")
        self.file.write(str(self.ui.spinBox_yuling_n.value())+"\n")
        self.file.write(str(self.ui.spinBox_jieqi.value())+"\n")
        self.file.write(str(self.ui.spinBox_jieqi_n.value())+"\n")
        self.file.write(str(self.ui.spinBox_pata.value())+"\n")
        self.file.write(str(self.ui.spinBox_pata_n.value())+"\n")
        self.file.close()
        self.ui.textEdit.append("数据保存完成")
        self.pushbutton_setenabled(True)
        pass
    # 创建一个鼠标监听器，点击时调用get_window_by_mouse函数
    def on_button_window_click(self):
        self.ui.textEdit.append("移动鼠标到目标窗口内点击左键获取窗口属性")
        self.pushbutton_setenabled(False)
        self.listener = mouse.Listener(on_click=self.get_window_by_mouse)
        self.listener.start()
        pass
    # 定义鼠标点击时调用的函数
    def get_window_by_mouse(self, x, y, button, pressed):
        # 判断是否是左键点击
        if button == mouse.Button.left and pressed :
            # 获取鼠标点击的窗口的句柄
            hld = win32gui.WindowFromPoint((x, y))
            # 获取窗口标题
            window_name = win32gui.GetWindowText(hld)
            left,top,right,bottom = win32gui.GetWindowRect(hld)
            self.ui.textEdit.append("窗口名称:{}".format(window_name))
            self.ui.textEdit.append("窗口句柄:{}".format(hld))
            self.ui.textEdit.append("窗口位置与尺寸:({},{})-({},{}) {}x{}".format(left,top,right,bottom,right-left,bottom-top))
            self.ui.lineEdit_window_name.setText(window_name)
            self.ui.lineEdit_window_hld.setText(str(hld))
            self.listener.stop()
            pass
        self.pushbutton_setenabled(True)
        pass
    #组队多开设置出战阴阳师账号所在窗口为主窗口
    def on_button_main_window_click(self):
        self.main_window_seted = self.ui.lineEdit_window_hld.text()
        self.ui.textEdit.append("主窗口设置成功，主窗口句柄:{}".format(self.main_window_seted))
        pass
    #接收工作任务传递的自定义消息并输出到输出控件
    def dataUpdate(self,data):
        self.ui.textEdit.append(data)
        pass
    #修改按键使能
    def pushbutton_setenabled(self,bool_val):
        self.ui.pushButton_window.setEnabled(bool_val)
        self.ui.pushButton_liulan.setEnabled(bool_val)
        #self.ui.pushButton_muban.setEnabled(bool_val)
        #self.ui.pushButton_jiejietupo.setEnabled(bool_val)
        self.ui.pushButton_qingkong.setEnabled(bool_val)
        self.ui.pushButton_ceshi.setEnabled(bool_val)
        self.ui.pushButton_baocun.setEnabled(bool_val)
        self.ui.pushButton_huntu.setEnabled(bool_val)
        self.ui.pushButton_k28.setEnabled(bool_val)
        self.ui.pushButton_gbyw.setEnabled(bool_val)
        self.ui.pushButton_yuling.setEnabled(bool_val)
        self.ui.pushButton_chakan.setEnabled(bool_val)
        self.ui.pushButton_start.setEnabled(bool_val)
        #self.ui.pushButton_zanting.setEnabled(bool_val)
        self.ui.pushButton_shanchu.setEnabled(bool_val)
        self.ui.pushButton_main_window.setEnabled(bool_val)
        self.ui.pushButton_huntu_zudui.setEnabled(bool_val)
        self.ui.pushButton_k28_zudui.setEnabled(bool_val)
        self.ui.pushButton_jieqi.setEnabled(bool_val)
        self.ui.pushButton_pata.setEnabled(bool_val)
        pass
    #收到工作任务消息
    def thread_finished(self,arg_0,arg_1):
        #开始执行任务，按键不使能
        if arg_0== "False":
            self.pushbutton_setenabled(False)
            pass
        #结束任务
        else:
            #删除该任务
            self.linklist.remove(arg_1)
            string = "删除" + arg_1 + "窗口已完成的任务"
            self.ui.textEdit.append(string)
            #检查是否还存在其他任务
            string = self.linklist.display()
            #存在其他任务
            if string != "":
                return
            #不存在其他工作任务
            else:
                #按键使能
                self.pushbutton_setenabled(True)
                self.ui.textEdit.append("所有任务已完成")
                self.main_window_seted = "0"
                if self.ui.checkBox_2.isChecked():
                    print("复选框被选中")
                    self.showNormal()
                    pass
                else:
                    print("复选框未选中")
                    pass
                pass
            pass
        pass
    #清空输出控件打印
    def on_button_qingkong_click(self):
        self.ui.textEdit.clear()
        pass
    #创建工作任务
    def molloc_for_thread(self,text):
        self.thread = QThread()
        self.set_dictionary()
        self.dictionary['run_name'] = text
        worker = yys_work.WorkerProcess(self.thread,self.mutex,self.dictionary)
        worker.update_data.connect(self.dataUpdate)
        worker.finished.connect(self.thread_finished)
        if self.linklist.search(self.dictionary['hld']) == None:
            self.linklist.add(self.dictionary['hld'],worker)
            string = "为" + self.dictionary['hld'] + "窗口添加任务成功"
            self.ui.textEdit.append(string)
            if self.main_window_seted != "0":
                string = "该任务为组队双开任务，其主窗口(打手)为" + self.main_window_seted
                self.ui.textEdit.append(string)
                pass
            self.file = open("hld.txt","a+",encoding="utf-8")
            self.file.write(self.ui.lineEdit_window_hld.text()+"\n")
            self.file.close()
            pass
        else:
            self.ui.textEdit.append("该窗口已存在任务，无法重复添加")
            self.ui.textEdit.append("如需重新设置任务，请删除后再试")
        pass
    #组队huntu按键点击事件槽函数
    def on_button_huntu_zudui_click(self):
        self.molloc_for_thread("huntu_zudui")
        return
    #组队k28按键点击事件槽函数
    def on_button_k28_zudui_click(self):
        self.molloc_for_thread("k28_zudui")
        return
    #测试按键
    def on_button_ceshi_click(self):
        self.molloc_for_thread("ceshi")
        return
    #huntu按键点击事件槽函数
    def on_button_huntu_click(self):
        self.molloc_for_thread("huntu")
        return
    #k28按键点击事件槽函数
    def on_button_k28_click(self):
        self.molloc_for_thread("k28")
        return
    #gbyw按键点击事件槽函数
    def on_button_gbyw_click(self):
        self.molloc_for_thread("gbyw")
        return
    #yuling按键点击事件槽函数
    def on_button_yuling_click(self):
        self.molloc_for_thread("yuling")
        return
    #契灵结契按键点击事件槽函数
    def on_button_jieqi_click(self):
        self.molloc_for_thread("jieqi")
        return
    #活动爬塔按键点击事件槽函数
    def on_button_pata_click(self):
        self.molloc_for_thread("pata")
        return
    #mubanku按键点击事件槽函数
    def on_button_muban_click(self):
        # self.thread = QThread()
        # self.set_dictionary()
        # self.dictionary['run_name'] = "mubanku"
        # self.worker = WorkerProcess(self.thread,self.dictionary)
        # self.worker.update_data.connect(self.dataUpdate)
        # self.worker.finished.connect(self.thread_finished)
        # #self.worker.start()
        return
    #jiejietupo按键点击事件槽函数
    def on_button_jiejietupo_click(self):
        # self.thread = QThread()
        # self.set_dictionary()
        # self.dictionary['run_name'] = "jiejietupo"
        # self.worker = WorkerProcess(self.thread,self.dictionary)
        # self.worker.update_data.connect(self.dataUpdate)
        # self.worker.finished.connect(self.thread_finished)
        # #self.worker.start()
        return
    #浏览按键点击事件槽函数
    def on_button_liulan_click(self):
        self.path = QFileDialog.getExistingDirectory()
        if self.path != "":
            self.ui.lineEdit_path.setText((self.path+"/\n")[:-1])
            pass
        else:
            self.ui.lineEdit_path.setText("\n")
        pass
    #查看按键点击事件槽函数
    def on_button_chakan_click(self):
        string = self.linklist.display()
        if string != "":
            self.ui.textEdit.append(string)
            pass
        else:
            self.ui.textEdit.append("None work thread")
            pass
        pass
    #开始按键点击事件槽函数
    def on_button_start_click(self):
        self.ui.textEdit.append("---所有任务开始---")
        if self.ui.checkBox.isChecked():
            print("复选框被选中")
            self.showMinimized()
            pass
        else:
            print("复选框未选中")
            pass
        self.file = open("hld.txt","r+",encoding="utf-8")
        self.lines = self.file.readlines()
        self.file.close()
        if len(self.lines) >= 1:
            i = 0
            while i < len(self.lines):
                worker = self.linklist.search(self.lines[i][:-1])
                if worker != None:
                    worker.start()
                    pass
                else:
                    string="There is no thread in "+self.lines[i][:-1]
                    self.ui.textEdit.append(string)
                    pass
                i += 1
                pass
            pass
        else:
            self.ui.textEdit.append("There is no thread")
            pass
        pass
    #暂停按键点击事件槽函数
    def on_button_zanting_click(self):
        # self.file = open("hld.txt","r+",encoding="utf-8")
        # self.lines = self.file.readlines()
        # self.file.close()
        # if len(self.lines) >= 1:
        #     i = 0
        #     while i < len(self.lines):
        #         #print(self.lines[i][:-1])
        #         worker = self.linklist.search(self.lines[i][:-1])
        #         if worker != None:
        #             #event传递信号使子线程阻塞
        #             #...
        #             pass
        #         else:
        #             print(self.lines[i][:-1],"none")
        #             pass
        #         i += 1
        #         pass
        #     pass
        # else:
        #     print("There is no thread")
        #     pass
        pass
    #删除按键点击事件槽函数
    def on_button_shanchu_click(self):
        self.linklist.remove(self.ui.lineEdit_window_hld.text())
        string = "删除" + self.ui.lineEdit_window_hld.text() + "窗口准备执行的任务"
        self.ui.textEdit.append(string)
        pass
    #关闭按键点击事件槽函数
    def closeEvent(self, event):
        if self.thread != None:
            self.thread.requestInterruption()  # 请求中断
            self.thread.quit()                # 退出事件循环
            # 等待2秒
            if not self.thread.wait(2000):
                print("线程未正常退出，强制终止")
                self.thread.terminate()     # 最后手段
                self.thread.wait()          # 确保终止完成
                pass
            pass
        #清除任务文件
        if os.path.exists("hld.txt"):
            os.remove("hld.txt")
            pass
        else:
            pass
        event.accept()                   # 接受关闭事件
        pass
    pass
pass
#主函数——程序入口
if __name__ == "__main__":
    #QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
