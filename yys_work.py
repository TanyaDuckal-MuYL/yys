from PySide6.QtCore import QThread, Signal, QDateTime
import cv2
import random
import pyautogui
import time
import datetime
import os
import shutil
from glob import glob
import win32gui
#工作任务
class WorkerProcess(QThread):
    update_data = Signal(str)
    finished = Signal(str,str)
    def __init__(self,thread,mutex,arg):
        QThread.__init__(self)
        self.thread = thread
        self.mutex = mutex
        self.arg = arg
        #目标窗口属性
        self.hld = 0
        self.left = 0
        self.top = 0
        self.right = 0
        self.bottom = 0
        self.window_name = ""
        #默认模板库路径
        self.path = ""
        #模板匹配阈值
        self.THRESHOLD = 0.5  # 匹配阈值
        #默认目标窗口高度(单位/像素)
        self.Vertical_dimensions = self.bottom-self.top#垂直尺寸
        #默认单局游戏战斗时长
        self.Duration_of_battle_h11 = 13 + 7#魂土战斗耗时
        self.Duration_of_battle_k28 = 7 + 5#困28战斗耗时
        self.Duration_of_battle_gbyw = 14#光总经验战斗耗时
        self.Duration_of_battle_yuling = 10 + 7#御灵战斗耗时
        #默认游戏次数
        self.n = 2#循环次数
        pass
    #模板库字典更新
    def update_mubanku(self):
        #组队
        self.zudui_zhuye = self.path +"zudui_zhuye.png"
        self.yuhun_zudui = self.path + "yuhun_zudui.png"
        self.zudui_chuangjian = self.path + "zudui_chuangjian.png"
        self.chuangjian = self.path + "chuangjian.png"
        self.yaoqing_ = self.path + "yaoqing_.png"
        self.zudui_haoyou = self.path + "zudui_haoyou.png"
        self.yaoqing = self.path + "yaoqing.png"
        self.shouyao = self.path + "shouyao.png"
        self.tiaozhan_x8 = self.path + "tiaozhan_x8.png"
        self.dashou_haoshi_zhuye = self.path + "dashou_haoshi_zhuye.png"
        self.dashou_haoshi = self.path + "dashou_haoshi.png"
        self.siji_haoshi_zhuye = self.path + "siji_haoshi_zhuye.png"
        self.siji_haoshi = self.path + "siji_haoshi.png"
        self.moren_yaoqing_zhuye = self.path + "moren_yaoqing_zhuye.png"
        self.moren_yaoqing_gouxuan = self.path + "moren_yaoqing_gouxuan.png"
        self.moren_yaoqing_queding = self.path + "moren_yaoqing_queding.png"
        self.moren_yaoqing_jiaru = self.path + "moren_yaoqing_jiaru.png"
        self.k28_zudui = self.path + "k28_zudui.png"
        self.k28_chuangjian = self.path + "k28_chuangjian.png"
        self.k28_tiaozhan_zudui = self.path + "k28_tiaozhan_zudui.png"
        #单人
        self.zhuye = self.path + "zhuye.png"
        self.tansuo = self.path + "tansuo.png"
        self.tansuo_zhuye = self.path + "tansuo_zhuye.png"
        self.tansuo_fanhui = self.path + "tansuo_fanhui.png"
        self.yuhun = self.path + "yuhun.png"
        self.yuhun_zhuye = self.path + "yuhun_zhuye.png"
        self.baqidashe = self.path + "baqidashe.png"
        self.baqidashe_zhuye = self.path + "baqidashe_zhuye.png"
        self.beiming = self.path + "beiming.png"
        self.tiaozhan = self.path + "tiaozhan.png"
        self.haoshi_zhuye = self.path + "haoshi_zhuye.png"
        self.haoshi_luxiang = self.path + "haoshi_luxiang.png"
        self.jiesuan_zhuye = self.path + "jiesuan_zhuye.png"
        self.jiesuan_damo = self.path + "jiesuan_damo.png"
        self.k28 = self.path + "k28.png"
        self.k28_zhuye = self.path + "k28_zhuye.png"
        self.k28_guanbi = self.path + "guanbi.png"
        self.k28_kunnan = self.path + "k28_kunnan.png"
        self.k28_tansuo = self.path + "k28_tansuo.png"
        self.k28_init = self.path + "k28_init.png"
        self.k28_zhandou = self.path + "k28_zhandou.png"
        self.k28_zhandou_boss = self.path + "k28_zhandou_boss.png"
        self.k28_baoxiang = self.path + "k28_baoxiang.png"
        self.k28_fanhui = self.path + "k28_fanhui.png"
        self.k28_fanhui_zhuye = self.path + "k28_fanhui_zhuye.png"
        self.k28_queren = self.path + "k28_queren.png"
        self.k28_jiesuan_baoxiang = self.path + "k28_jiesuan_baoxiang.png"
        self.yjsl = self.path + "yjsl.png"
        self.yjsl_zhuye = self.path + "yjsl_zhuye.png"
        self.gbyw = self.path + "gbyw.png"
        self.gbyw_zhuye = self.path + "gbyw_zhuye.png"
        self.gbyw_tiaozhan = self.path + "gbyw_tiaozhan.png"
        self.gbyw_jiesuan = self.path + "gbyw_jiesuan.png"
        self.gbyw_jinyan = self.path + "gbyw_jinyan.png"
        self.gbyw_fanhui = self.path + "gbyw_fanhui.png"
        self.yuling = self.path + "yuling.png"
        self.yuling_zhuye = self.path + "yuling_zhuye.png"
        self.yuling_mubiaoku = [self.path + "yuling_shenlong.png",
                                self.path + "yuling_xiaobai.png",
                                self.path + "yuling_heibao.png",
                                self.path + "yuling_kongque.png"]
        self.yuling_mubiao = self.yuling_mubiaoku[0]
        self.yuling_san = self.path + "yuling_san.png"
        self.yuling_tiaozhan = self.path + "yuling_tiaozhan.png"
        self.jiejietupo = self.path + "jiejietupo.png"
        self.jiejietupo_zhuye = self.path + "jiejietupo_zhuye.png"
        self.jiejietupo_mubiao = self.path + "jiejietupo_mubiao.png"
        self.jiejietupo_jingong = self.path + "jiejietupo_jingong.png"
        self.jiejietupo_fanhui = self.path + "jiejietupo_fanhui.png"
        self.jiejietupo_guanbi = self.path + "guanbi.png"
        self.jiejietupo_fanhui_zhuye = self.path + "jiejietupo_fanhui_zhuye.png"
        self.jiejietupo_queren = self.path + "jiejietupo_queren.png"
        self.jiejietupo_shibai = self.path + "jiejietupo_shibai.png"
        self.jiejietupo_shibai_anniu = self.path + "jiejietupo_shibai_anniu.png"
        self.jiejietupo_shuaxin = self.path + "jiejietupo_shuaxin.png"
        pass
    #截图目标模板并保存到路径str_path
    def get_muban_picture(self,str_path,x,y,width,height):
        screenshot = pyautogui.screenshot(region=(x,y,width,height))
        screenshot.save(str_path)
        self.update_data.emit("   "+str_path)
        return
    #模板库自动生成
    def auto_mubanku(self):
        self.update_data.emit("开始自动生成模板库文件，保存路径如下...")
        self.get_window_coordinate(self.hld)
        win32gui.MoveWindow(self.hld,self.left,self.top,self.Horizontal_dimensions,self.Vertical_dimensions,True)
        self.get_window_coordinate(self.hld)
        pyautogui.moveTo(self.left+1,self.top+1)
        pyautogui.click()
        self.get_muban_picture(self.zhuye,self.left,self.top,self.Horizontal_dimensions,self.Vertical_dimensions)
        self.get_muban_picture(self.tansuo,self.left+int(0.41*self.Horizontal_dimensions),self.top+int(0.11*self.Horizontal_dimensions),int(0.026*self.Vertical_dimensions),int(0.038*self.Horizontal_dimensions))
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time(),self.hld)
        pass
    #获取目标窗口属性
    def get_window_coordinate(self,hld):
        #通过窗口标题获取句柄
        #self.hld = win32gui.FindWindow(None,self.window_name)
        # 通过句柄值获取当前窗口的【左、上、右、下】四个方向的坐标位置
        self.left, self.top, self.right, self.bottom = win32gui.GetWindowRect(hld)
        #print(self.left,self.top,self.right,self.bottom)
        self.Horizontal_dimensions = self.right-self.left#水平尺寸
        self.Vertical_dimensions = self.bottom-self.top#垂直尺寸
        #print("({}x{})".format(self.right-self.left,self.bottom-self.top))
        return
    #1-3秒内随机
    def get_time(self):
        return random.uniform(1, 3)
    #0.1-0.3秒内随机
    def get_time_quick(self):
        return random.uniform(0.1, 0.3)
    #从目标窗口中点开始按住鼠标左建向左/右移动半个目标窗口宽度的距离
    def click_and_move(self,str_direction,hld):
        self.get_window_coordinate(hld)
        pyautogui.moveTo((self.left+self.right)/2,self.top+self.Vertical_dimensions/2)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(self.left,self.top+self.Vertical_dimensions/2,self.get_time_quick()) if str_direction == "left" else pyautogui.moveTo(self.right,self.top+self.Vertical_dimensions/2,self.get_time())
        pyautogui.mouseUp(x=self.left,button='left')
        return
    #截图目标窗口并保存到路径str_path
    def get_current_picture(self,str_path,hld):
        self.get_window_coordinate(hld)
        #print(self.left,self.top,self.right,self.bottom)
        screenshot = pyautogui.screenshot(region=(self.left, self.top, self.right-self.left, self.bottom-self.top))
        screenshot.save(str_path)
        return
    #读取路径pic_str的灰度图
    def open_picture(self,pic_str):
        return cv2.imread(pic_str,0)
    #用TM_CCOEFF_NORMED方法匹配模板得到其匹配阈值和矩阵图
    def get_max_val_find_template(self,p1,p2):
        """在p1图片中查找模板p2"""
        result = cv2.matchTemplate(p1,p2,cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #print("匹配阈值最大值:", max_val)
        return max_val,max_loc
    #根据模板相对目标窗口坐标推算该模板当前分辨率下的绝对坐标并随机选取模板中的某一像素点作为点击坐标返回
    def find_template(self,p1,p2,j,k):
        max_val,max_loc = self.get_max_val_find_template(p1,p2)
        #print("匹配阈值最大值:", max_val)
        if max_val > self.THRESHOLD:
            p_w,p_h=p2.shape[::-1]#获取模板宽度与高度(单位/像素)
            #推算模板四个顶点的绝对坐标
            top_left=(max_loc[0]+self.left,max_loc[1]+self.top)
            bottom_right=(top_left[0]+p_w,top_left[1]+p_h)
            #取模板四顶点中随机像素点
            x=random.randint(top_left[0], bottom_right[0])
            y=random.randint(top_left[1], bottom_right[1])
            #结算页面像素点击位置偏移
            if j == 1:
                #j==结算偏移标识
                x=random.randint(bottom_right[0], self.right-50)
                y=random.randint(top_left[1]+20, bottom_right[1])
                return (x,y)
            #取模板中心像素点作为点击位置
            if k == 1:
                #k==困28战斗图标取中心标识
                x=(top_left[0]+bottom_right[0])/2
                y=(top_left[1]+bottom_right[1])/2
                return (x,y)
            return(x,y)
        elif max_val > 0 or max_val <= self.THRESHOLD:
            #未匹配到模板
            # x=((self.left+self.right)/2+self.right)/2
            # y=((self.top+self.top+self.Vertical_dimensions)/2+self.top+self.Vertical_dimensions)/2
            return (0,0)
        return (0,0)
    #鼠标移动到指定位置并点击
    def click_coordinate(self,x,y,t):
        pyautogui.moveTo(x,y,t)
        pyautogui.click()
        return
    #线程加锁
    def thread_mutex_lock(self):
        self.mutex.lock()
        pass
    #线程解锁
    def thread_mutex_unlock(self):
        self.mutex.unlock()
        pass
    #根据模板p2_str在模板p1_str的相对位置点击
    def click_picture(self,p1_str,p2_str,j,k,t,hld):
        self.get_window_coordinate(hld)
        png_1 = self.open_picture(p1_str)
        png_2 = self.open_picture(p2_str)
        x, y = self.find_template(png_1,png_2,j,k)
        if (x,y) == (0,0):
            return (x,y)
        self.click_coordinate(x,y,t)
        return (x,y)
    #向父进程传递信息
    def send_to_UI(self,text):
        text = str(self.hld) + ":" + text
        self.update_data.emit(text)
        pass
    #接受父进程信息
    def recv_from_UI(self,num):
        pass
    #组队挖土
    def yys_watu_zudui(self):
        n1 = 0
        #self.thread_mutex_lock()
        #操作_司机窗口
        current_hld = self.hld
        self.get_current_picture(self.zhuye,current_hld)
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,current_hld)
        self.click_picture(self.tansuo_zhuye,self.yuhun,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.yuhun_zhuye,current_hld)
        self.click_picture(self.yuhun_zhuye,self.baqidashe,0,0,self.get_time_quick(),current_hld)
        self.click_picture(self.baqidashe_zhuye,self.beiming,0,0,self.get_time_quick(),current_hld)
        #司机窗口发起组队
        self.click_picture(self.baqidashe_zhuye,self.yuhun_zudui,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.zudui_chuangjian,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.chuangjian,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.yaoqing_,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.zudui_haoyou,0,0,self.get_time_quick(),current_hld)
        self.click_picture(self.zudui_zhuye,self.yaoqing,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        #操作_打手窗口
        current_hld = self.main_window_hld
        self.get_current_picture(self.zhuye,current_hld)
        self.click_picture(self.zhuye,self.shouyao,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        #循环挑战
        self.send_to_UI("---huntu开始执行---循环{}次".format(self.n))
        while self.n != 0:
            self.n -= 1
            n1 += 1
            #操作_司机窗口
            current_hld = self.hld
            self.get_current_picture(self.zudui_zhuye,current_hld)
            self.click_picture(self.zudui_zhuye,self.tiaozhan_x8,0,0,self.get_time_quick(),current_hld)
            #开始战斗
            time.sleep(self.Duration_of_battle_h11)
            #战斗结束
            self.click_picture(self.siji_haoshi_zhuye,self.siji_haoshi,1,0,self.get_time_quick(),current_hld)
            self.click_picture(self.siji_haoshi_zhuye,self.siji_haoshi,1,0,self.get_time_quick(),current_hld)
            #操作_打手窗口
            current_hld = self.main_window_hld
            self.click_picture(self.dashou_haoshi_zhuye,self.dashou_haoshi,1,0,self.get_time_quick(),current_hld)
            self.click_picture(self.dashou_haoshi_zhuye,self.dashou_haoshi,1,0,self.get_time_quick(),current_hld)
            time.sleep(1.5)
            #操作_司机窗口
            current_hld = self.hld
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
            #操作_打手窗口
            current_hld = self.main_window_hld
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
            time.sleep(1)
            if n1 == 1:
                #操作_司机窗口
                current_hld = self.hld
                self.click_picture(self.moren_yaoqing_zhuye,self.moren_yaoqing_gouxuan,0,1,self.get_time_quick(),current_hld)
                self.click_picture(self.moren_yaoqing_zhuye,self.moren_yaoqing_queding,0,0,self.get_time_quick(),current_hld)
                time.sleep(2)
                #操作_打手窗口
                current_hld = self.main_window_hld
                self.get_current_picture(self.zhuye,current_hld)
                self.click_picture(self.zhuye,self.moren_yaoqing_jiaru,0,0,self.get_time_quick(),current_hld)
                pass
            self.send_to_UI("     huntu执行次数={},体力开销={},剩余次数={}".format(n1,n1*12,self.n))
            time.sleep(1)
            pass
        #操作_打手窗口
        self.send_to_UI("---huntu执行完毕---花费体力{}---".format(n1*12))
        self.send_to_UI("---返回主页---")
        current_hld = self.main_window_hld
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.gbyw_fanhui,0,0,self.get_time(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.moren_yaoqing_queding,0,0,self.get_time(),current_hld)
        self.click_picture(self.tansuo_zhuye,self.tansuo_fanhui,0,0,self.get_time(),current_hld)
        #操作_司机窗口
        current_hld = self.hld
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.gbyw_fanhui,0,0,self.get_time(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.moren_yaoqing_queding,0,0,self.get_time(),current_hld)
        self.click_picture(self.tansuo_zhuye,self.tansuo_fanhui,0,0,self.get_time(),current_hld)
        pass
    #组队困28
    def yys_k28_zudui(self):
        s = 0
        sl = 0
        n1 = 0
        #操作_司机窗口
        current_hld = self.hld
        self.get_current_picture(self.zhuye,current_hld)
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,current_hld)
        self.click_picture(self.tansuo_zhuye,self.k28,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.k28_zhuye,self.hld)
        self.click_picture(self.k28_zhuye,self.k28_kunnan,0,0,self.get_time_quick(),self.hld)
        time.sleep(1)
        self.get_current_picture(self.k28_zhuye,current_hld)
        self.click_picture(self.k28_zhuye,self.k28_zudui,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        #司机窗口发起组队
        self.get_current_picture(self.k28_zhuye,current_hld)
        self.click_picture(self.k28_zhuye,self.k28_chuangjian,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.yaoqing_,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        self.get_current_picture(self.zudui_zhuye,current_hld)
        self.click_picture(self.zudui_zhuye,self.zudui_haoyou,0,0,self.get_time_quick(),current_hld)
        self.click_picture(self.zudui_zhuye,self.yaoqing,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        #操作_打手窗口
        current_hld = self.main_window_hld
        self.get_current_picture(self.zhuye,current_hld)
        self.click_picture(self.zhuye,self.shouyao,0,0,self.get_time_quick(),current_hld)
        time.sleep(2)
        #循环挑战
        self.send_to_UI("---k28开始执行---循环{}次".format(self.n))
        while self.n != 0:
            sl = s
            #操作_司机窗口
            current_hld = self.hld
            self.get_current_picture(self.zudui_zhuye,current_hld)
            self.click_picture(self.zudui_zhuye,self.k28_tiaozhan_zudui,0,0,self.get_time_quick(),current_hld)
            time.sleep(2)
            self.get_current_picture(self.k28_init,current_hld)
            png_1 = self.open_picture(self.k28_init)
            png_2 = self.open_picture(self.k28_zhandou)
            max_val,max_loc = self.get_max_val_find_template(png_1,png_2)
            #没有怪物
            if self.THRESHOLD > max_val:
                time.sleep(1)
                self.click_and_move("left",current_hld)
                time.sleep(1)
                pass
            #有怪物
            else:
                # #点击小怪战斗
                self.click_picture(self.k28_init,self.k28_zhandou,0,1,0.1,current_hld)
                s += 1
                self.send_to_UI("     小怪次数={},体力开销={},剩余次数={}".format(s,n1*24+s*3,7-s))
                pass
            if sl != s:
                #战斗操作
                time.sleep(self.Duration_of_battle_k28)
                #打手结算
                current_hld = self.main_window_hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                #司机结算
                current_hld = self.hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                time.sleep(1.5)
                #打手结算
                current_hld = self.main_window_hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                #司机结算
                current_hld = self.hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                #time.sleep(2)
                pass
            if s == 7:
                time.sleep(2)
                # 截图k28
                current_hld = self.hld
                self.get_current_picture(self.k28_init,current_hld)
                png_1 = self.open_picture(self.k28_init)
                png_2 = self.open_picture(self.k28_zhandou_boss)
                self.click_picture(self.k28_init,self.k28_zhandou_boss,0,0,self.get_time_quick(),current_hld)
                self.send_to_UI("     BOSS战斗,体力开销={}".format(n1*24+s*3+3))
                time.sleep(self.Duration_of_battle_k28+2)
                #打手结算
                current_hld = self.main_window_hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                #司机结算
                current_hld = self.hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                time.sleep(1.5)
                #打手结算
                current_hld = self.main_window_hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                #司机结算
                current_hld = self.hld
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),current_hld)
                #time.sleep(1)
                time.sleep(2)
                self.get_current_picture(self.k28_init,current_hld)
                png_1 = self.open_picture(self.k28_init)
                png_2 = self.open_picture(self.k28_baoxiang)
                max_val,max_loc = self.get_max_val_find_template(png_1,png_2)
                #有宝箱
                if self.THRESHOLD <= max_val:
                    #司机退出
                    self.click_picture(self.k28_init,self.k28_fanhui,0,0,self.get_time_quick(),current_hld)
                    self.click_picture(self.k28_fanhui_zhuye,self.k28_queren,0,0,self.get_time_quick(),current_hld)
                    pass
                # #司机退出请求
                # current_hld = self.hld
                # self.get_current_picture(self.k28_init,current_hld)
                # self.click_picture(self.k28_init,self.k28_fanhui,0,0,self.get_time_quick(),current_hld)
                # #司机退出
                # current_hld = self.hld
                # self.click_picture(self.k28_fanhui_zhuye,self.k28_queren,0,0,self.get_time_quick(),current_hld)
                #打手退出请求
                current_hld = self.main_window_hld
                self.get_current_picture(self.k28_init,current_hld)
                self.click_picture(self.k28_init,self.k28_fanhui,0,0,self.get_time_quick(),current_hld)
                #打手退出
                self.click_picture(self.k28_fanhui_zhuye,self.k28_queren,0,0,self.get_time_quick(),current_hld)
                time.sleep(2)
                s = 0
                sl = 0
                self.n -= 1
                n1 += 1
                self.send_to_UI("k28执行次数={},体力开销={},剩余次数={}".format(n1,n1*24,self.n))
                #k28每次循环需要邀请队友加入
                if self.n != 0:
                    #操作_司机窗口
                    current_hld = self.hld
                    self.click_picture(self.moren_yaoqing_zhuye,self.moren_yaoqing_queding,0,0,self.get_time_quick(),current_hld)
                    time.sleep(2)
                    #操作_打手窗口
                    current_hld = self.main_window_hld
                    self.get_current_picture(self.zhuye,current_hld)
                    self.click_picture(self.zhuye,self.shouyao,0,0,self.get_time_quick(),current_hld)
                    pass
                time.sleep(2)
                pass
            pass
        #--------
        #操作_司机窗口
        current_hld = self.hld
        self.send_to_UI("---k28执行完毕---花费体力{}---".format(n1*24))
        pass
    #阴阳师挖土逻辑实现
    def yys_watu(self):
        n1 = 0
        self.get_current_picture(self.zhuye,self.hld)
        #加锁防止多个线程抢占鼠标指针
        self.thread_mutex_lock()
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time_quick(),self.hld)
        #完成模拟点击后解锁释放资源
        self.thread_mutex_unlock()
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.yuhun,0,0,self.get_time_quick(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        self.get_current_picture(self.yuhun_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.yuhun_zhuye,self.baqidashe,0,0,self.get_time_quick(),self.hld)
        self.thread_mutex_unlock()
        self.thread_mutex_lock()
        self.click_picture(self.baqidashe_zhuye,self.beiming,0,0,self.get_time_quick(),self.hld)
        self.thread_mutex_unlock()
        self.send_to_UI("---huntu开始执行---循环{}次".format(self.n))
        time.sleep(1)
        while self.n != 0:
            self.n -= 1
            n1 += 1
            self.thread_mutex_lock()
            self.click_picture(self.baqidashe_zhuye,self.tiaozhan,0,0,self.get_time_quick(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(self.Duration_of_battle_h11)
            self.thread_mutex_lock()
            self.click_picture(self.haoshi_zhuye,self.haoshi_luxiang,1,0,self.get_time_quick(),self.hld)
            self.click_picture(self.haoshi_zhuye,self.haoshi_luxiang,1,0,self.get_time_quick(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(1.5)
            self.thread_mutex_lock()
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(1.5)
            self.send_to_UI("     huntu执行次数={},体力开销={},剩余次数={}".format(n1,n1*12,self.n))
            pass
        self.send_to_UI("---huntu执行完毕---花费体力{}---".format(n1*12))
        self.thread_mutex_lock()
        self.click_picture(self.baqidashe_zhuye,self.tansuo_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(1)
        self.send_to_UI("---返回主页---")
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.tansuo_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(1)
        pass
    #阴阳师鬼兵演武逻辑实现
    def yys_gbyw(self):
        n1 = 0
        self.get_current_picture(self.zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.yjsl,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        self.thread_mutex_lock()
        self.click_picture(self.yjsl_zhuye,self.gbyw,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        self.send_to_UI("---gbyw开始执行---循环{}次".format(self.n))
        while self.n != 0:
            self.n -= 1
            n1 += 1
            self.thread_mutex_lock()
            self.click_picture(self.gbyw_zhuye,self.gbyw_tiaozhan,0,0,self.get_time(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(self.Duration_of_battle_gbyw)
            self.thread_mutex_lock()
            self.click_picture(self.gbyw_jiesuan,self.gbyw_jinyan,1,0,self.get_time_quick(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(1)
            self.send_to_UI("gbyw执行次数={},体力开销={},剩余次数={}".format(n1,n1*3,self.n))
            pass
        self.send_to_UI("---gbyw执行完毕---花费体力{}---".format(n1*3))
        self.send_to_UI("---返回主页---")
        self.thread_mutex_lock()
        self.click_picture(self.gbyw_zhuye,self.gbyw_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        self.thread_mutex_lock()
        self.click_picture(self.yjsl_zhuye,self.gbyw_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.tansuo_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        pass
    #阴阳师探索困难28章逻辑实现
    def yys_k28(self):
        s = 0
        sl = 0
        n1 = 0
        self.get_current_picture(self.zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.k28,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        self.get_current_picture(self.k28_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.k28_zhuye,self.k28_kunnan,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        self.thread_mutex_lock()
        self.click_picture(self.k28_zhuye,self.k28_tansuo,0,0,self.get_time_quick(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        self.send_to_UI("---k28开始执行---循环{}次".format(self.n))
        while self.n != 0:
            sl = s
            self.thread_mutex_lock()
            self.get_current_picture(self.k28_init,self.hld)
            png_1 = self.open_picture(self.k28_init)
            png_2 = self.open_picture(self.k28_zhandou)
            max_val,max_loc = self.get_max_val_find_template(png_1,png_2)
            #没有怪物
            if self.THRESHOLD > max_val:
                time.sleep(1)
                self.click_and_move("left",self.hld)
                time.sleep(1)
                pass
            #有怪物
            else:
                # #点击小怪战斗
                # p_w,p_h=png_2.shape[::-1]#获取模板宽度与高度(单位/像素)
                # #推算模板四个顶点的绝对坐标
                # top_left=(max_loc[0]+self.left,max_loc[1]+self.top)
                # bottom_right=(top_left[0]+p_w,top_left[1]+p_h)
                # #k==困28战斗图标取中心标识
                # x=(top_left[0]+bottom_right[0])/2
                # y=(top_left[1]+bottom_right[1])/2
                # self.click_coordinate(x,y,0.1)
                self.click_picture(self.k28_init,self.k28_zhandou,0,1,0.1,self.hld)
                s += 1
                self.send_to_UI("     小怪次数={},体力开销={},剩余次数={}".format(s,n1*24+s*3,7-s))
                pass
            self.thread_mutex_unlock()
            #self.click_picture(self.k28_init,self.k28_zhandou,0,1,0.1,self.hld)
            if sl != s:
                time.sleep(self.Duration_of_battle_k28)
                self.thread_mutex_lock()
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                self.thread_mutex_unlock()
                time.sleep(1.5)
                self.thread_mutex_lock()
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                self.thread_mutex_unlock()
                time.sleep(2)
                pass
            if s == 7:
                time.sleep(1)
                # 截图k28
                self.thread_mutex_lock()
                self.get_current_picture(self.k28_init,self.hld)
                png_1 = self.open_picture(self.k28_init)
                png_2 = self.open_picture(self.k28_zhandou_boss)
                    # x, y = self.find_template(png_1,png_2,0,1)
                    # self.click_coordinate(x,y,0.1)
                self.click_picture(self.k28_init,self.k28_zhandou_boss,0,0,self.get_time_quick(),self.hld)
                self.thread_mutex_unlock()
                self.send_to_UI("     BOSS战斗,体力开销={}".format(n1*24+s*3+3))
                time.sleep(self.Duration_of_battle_k28+2)
                self.thread_mutex_lock()
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                self.thread_mutex_unlock()
                time.sleep(1.5)
                self.thread_mutex_lock()
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
                #self.thread_mutex_unlock()
                time.sleep(2)
                #self.thread_mutex_lock()
                self.get_current_picture(self.k28_init,self.hld)
                png_1 = self.open_picture(self.k28_init)
                png_2 = self.open_picture(self.k28_baoxiang)
                max_val,max_loc = self.get_max_val_find_template(png_1,png_2)
                #有宝箱
                if self.THRESHOLD <= max_val:
                    self.click_picture(self.k28_init,self.k28_fanhui,0,0,self.get_time_quick(),self.hld)
                    #self.get_current_picture(self.k28_fanhui_zhuye,self.hld)
                    self.click_picture(self.k28_fanhui_zhuye,self.k28_queren,0,0,self.get_time_quick(),self.hld)
                    pass
                self.thread_mutex_unlock()
                time.sleep(1)
                s = 0
                sl = 0
                self.n -= 1
                n1 += 1
                if self.n != 0:
                    self.thread_mutex_lock()
                    self.click_picture(self.tansuo_zhuye,self.k28,0,0,self.get_time(),self.hld)
                    self.thread_mutex_unlock()
                    self.thread_mutex_lock()
                    self.click_picture(self.k28_zhuye,self.k28_kunnan,0,0,self.get_time(),self.hld)
                    self.thread_mutex_unlock()
                    self.thread_mutex_lock()
                    self.click_picture(self.k28_zhuye,self.k28_tansuo,0,0,self.get_time_quick(),self.hld)
                    self.thread_mutex_unlock()
                    time.sleep(2)
                    pass
                self.send_to_UI("k28执行次数={},体力开销={},剩余次数={}".format(n1,n1*24,self.n))
                pass
            pass
        self.send_to_UI("---k28执行完毕---花费体力{}---".format(n1*24))
        self.thread_mutex_lock()
        self.click_picture(self.k28_zhuye,self.k28_guanbi,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,self.hld)
        self.send_to_UI("---返回主页---")
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.tansuo_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        pass
    #阴阳师御灵副本逻辑实现
    def yys_yuling(self):
        n1 = 0
        self.get_current_picture(self.zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.yuling,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(2)
        #星期判断
        current_datetime = datetime.datetime.now()
        weekday = current_datetime.weekday()
        if weekday > 4:
            weekday -= 3#周五打白藏主，周六打黑豹
            pass
        elif weekday == 0:
            self.send_to_UI("无法挑战，周一不开放御灵副本")
            return
        self.yuling_mubiao = self.yuling_mubiaoku[weekday - 1]
        self.get_current_picture(self.yuling_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.yuling_zhuye,self.yuling_mubiao,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        time.sleep(1)
        #完成星期判断
        self.get_current_picture(self.yuling_zhuye,self.hld)
        self.thread_mutex_lock()
        self.click_picture(self.yuling_zhuye,self.yuling_san,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        self.send_to_UI("---御灵副本开始执行---循环{}次".format(self.n))
        while self.n != 0:
            n1 += 1
            self.thread_mutex_lock()
            self.click_picture(self.yuling_zhuye,self.yuling_tiaozhan,0,0,self.get_time(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(self.Duration_of_battle_yuling)
            self.thread_mutex_lock()
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(1.5)
            self.thread_mutex_lock()
            self.click_picture(self.jiesuan_zhuye,self.jiesuan_damo,1,0,self.get_time_quick(),self.hld)
            self.thread_mutex_unlock()
            time.sleep(1.5)
            self.n -= 1
            self.send_to_UI("     御灵执行次数={},门票开销={},剩余次数={}".format(n1,n1,self.n))
            pass
        self.send_to_UI("---御灵执行完毕---花费门票{}---".format(n1))
        self.send_to_UI("---返回主页---")
        self.thread_mutex_lock()
        self.click_picture(self.yuling_zhuye,self.tansuo_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        self.thread_mutex_lock()
        self.click_picture(self.tansuo_zhuye,self.tansuo_fanhui,0,0,self.get_time(),self.hld)
        self.thread_mutex_unlock()
        pass
    #阴阳师结界突破逻辑实现
    def yys_jiejietupo(self):
        self.send_to_UI("---结界突破开始执行---循环{}次".format(self.n))
        s = 0
        self.get_current_picture(self.zhuye,self.hld)
        self.click_picture(self.zhuye,self.tansuo,0,0,self.get_time(),self.hld)
        time.sleep(2)
        self.get_current_picture(self.tansuo_zhuye,self.hld)
        self.click_picture(self.tansuo_zhuye,self.jiejietupo,0,0,self.get_time(),self.hld)
        time.sleep(2)
        while self.n != 0:
            self.jiejietupo_finished = 0
            #选择进攻目标并获取点击坐标
            self.get_current_picture(self.jiejietupo_zhuye,self.hld)
            x,y = self.click_picture(self.jiejietupo_zhuye,self.jiejietupo_mubiao,0,0,self.get_time(),self.hld)
            time.sleep(1)
            #进攻该目标
            self.get_current_picture(self.jiejietupo_zhuye,self.hld)
            self.click_picture(self.jiejietupo_zhuye,self.jiejietupo_jingong,0,0,self.get_time(),self.hld)
            time.sleep(7)
            #投降
            self.get_current_picture(self.jiejietupo_zhuye,self.hld)
            self.click_picture(self.jiejietupo_zhuye,self.jiejietupo_fanhui,0,0,0.1,self.hld)
            self.click_picture(self.jiejietupo_fanhui_zhuye,self.jiejietupo_queren,0,0,self.get_time_quick(),self.hld)
            time.sleep(2)
            self.click_picture(self.jiejietupo_shibai,self.jiejietupo_shibai_anniu,1,0,self.get_time(),self.hld)
            time.sleep(2)
            #重新发起进攻
            self.click_coordinate(x,y,self.get_time())
            time.sleep(1)
            #进攻该目标
            self.get_current_picture(self.jiejietupo_zhuye,self.hld)
            self.click_picture(self.jiejietupo_zhuye,self.jiejietupo_jingong,0,0,self.get_time(),self.hld)
            #每间隔十秒匹配一次结算达摩或失败按钮
            while self.jiejietupo_finished == 0:
                x=0
                y=0
                time.sleep(1)
                self.get_current_picture(self.jiejietupo_zhuye,self.hld)
                png_1 = self.open_picture(self.jiejietupo_zhuye)
                png_2 = self.open_picture(self.jiesuan_damo)
                x,y = self.find_template(png_1,png_2,1,0)
                if x!=0 and y!=0:
                    print (x,y)
                    self.jiejietupo_finished = 1
                    self.click_coordinate(x,y,self.get_time())
                    time.sleep(2)
                    pass
                self.get_current_picture(self.jiejietupo_zhuye,self.hld)
                png_1 = self.open_picture(self.jiejietupo_zhuye)
                png_2 = self.open_picture(self.jiejietupo_shibai_anniu)
                x,y = self.find_template(png_1,png_2,1,0)
                if x!=0 and y!=0:
                    print (x,y)
                    self.jiejietupo_finished = 2
                    self.click_coordinate(x,y,self.get_time())
                    time.sleep(2)
                    pass
                pass
            #计数
            if self.jiejietupo_finished == 1:
                self.n -= 1
                s += 1
                self.send_to_UI("  完成突破{}次，剩余{}次".format(s,self.n))
                time.sleep(2)
                pass
            elif self.jiejietupo_finished == 2:
                self.send_to_UI("  挑战失败，刷新对手")
                self.get_current_picture(self.jiejietupo_zhuye,self.hld)
                self.click_picture(self.jiejietupo_zhuye,self.jiejietupo_shuaxin,0,0,self.get_time(),self.hld)
                time.sleep(2)
                self.get_current_picture(self.jiejietupo_zhuye,self.hld)
                self.click_picture(self.jiejietupo_zhuye,self.jiejietupo_queren,0,0,self.get_time(),self.hld)
                time.sleep(2)
                pass
            pass
        pass
    def ceshi(self):
        # 循环10次，每秒钟传递一次时间给UI
        n = 10
        while n:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_data.emit(str(currentTime))
            n -= 1
            time.sleep(1)
            pass
        pass
    def copy_file(self):
        # 源文件夹路径
        src_dir = self.arg['path']
        # 获取源文件夹中所有文件的路径
        src_files = glob(os.path.join(src_dir, '*'))
        # 目标文件夹路径
        self.path = self.arg['path'] + str(self.hld) + "/"
        # 创建目标文件夹
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            print("Folder created")
            # 遍历文件列表，拷贝每个文件
            for file_path in src_files:
                shutil.copy(file_path, self.path)
                pass
            pass
        else:
            print("Folder already exists")
            pass
        pass
    def del_file(self):
        if not os.listdir(self.path):
            print('目录为空！')
            os.rmdir(self.path)
            pass
        else:
            shutil.rmtree(self.path)
            pass
        pass
    def run(self):
        self.finished.emit("False",self.arg['hld'])
        self.window_name = self.arg['window_name']
        self.hld = int(self.arg['hld'])
        self.main_window_hld = int(self.arg['main_window_hld'])
        self.copy_file()
        self.Duration_of_battle_h11 = self.arg['Duration_of_battle_h11']
        self.Duration_of_battle_k28 = self.arg['Duration_of_battle_k28']
        self.Duration_of_battle_gbyw = self.arg['Duration_of_battle_gbyw']
        self.Duration_of_battle_yuling = self.arg['Duration_of_battle_yuling']
        self.update_mubanku()
        self.start_time = time.time()
        if self.arg['run_name'] == "ceshi":
            self.ceshi()
            pass
        elif self.arg['run_name'] == "huntu":
            self.n = self.arg['Duration_of_battle_h11_n']
            self.yys_watu()
            pass
        elif self.arg['run_name'] == "huntu_zudui":
            self.n = self.arg['Duration_of_battle_h11_n']
            self.yys_watu_zudui()
            pass
        elif self.arg['run_name'] == "k28":
            self.n = self.arg['Duration_of_battle_k28_n']
            self.yys_k28()
            pass
        elif self.arg['run_name'] == "k28_zudui":
            self.n = self.arg['Duration_of_battle_k28_n']
            self.yys_k28_zudui()
            pass
        elif self.arg['run_name'] == "gbyw":
            self.n = self.arg['Duration_of_battle_gbyw_n']
            self.yys_gbyw()
            pass
        elif self.arg['run_name'] == "yuling":
            self.n = self.arg['Duration_of_battle_yuling_n']
            self.yys_yuling()
            pass
        elif self.arg['run_name'] == "mubanku":
            self.n = 1
            self.auto_mubanku()
            pass
        elif self.arg['run_name'] == "jiejietupo":
            self.n = 30
            self.yys_jiejietupo()
            pass
        self.end_time = time.time()
        self.m, self.s = divmod(self.end_time-self.start_time, 60)
        self.h, self.m = divmod(self.m, 60)
        self.update_data.emit("花费时间---%02d:%02d:%02d"%(self.h,self.m,self.s))
        self.del_file()
        self.finished.emit("True",self.arg['hld'])
        pass
    pass
pass
