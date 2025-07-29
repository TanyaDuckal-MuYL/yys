#链表节点
class Node:
    def __init__(self,text="",data=None,next=None):
        self.text = text
        self.data = data
        self.next = next
        pass
    pass
#数据结构——链表（对处理每个游戏窗口的线程进行记录）
class LinkList:
    def __init__(self):
        self.head = None
        pass
    def add(self,text,value):
        new_node = Node(text,value)
        new_node.next = self.head
        self.head = new_node
        pass
    def remove(self,text):
        current = self.head
        previous = None
        while current:
            if current.text == text:
                if previous:
                    previous.next = current.next
                    pass
                else:
                    self.head = current.next
                    pass
                return
            previous = current
            current = current.next
            pass
        pass
    def search(self, text):
        current = self.head
        while current:
            if current.text == text:
                return current.data
            current = current.next
            pass
        return None
    def display(self):
        current = self.head
        linklist_str = ""
        while current:
            #print(current.text,current.data, end=' ')
            linklist_str = linklist_str + "窗口句柄:" + current.text + " "
            linklist_str = linklist_str + "工作任务:" + current.data.arg["run_name"] + " "
            work_num = 0
            if current.data.arg["run_name"] == "huntu" or "huntu_zudui":
                work_num = current.data.arg["Duration_of_battle_h11_n"]
                pass
            elif current.data.arg["run_name"] == "k28" or "k28_zudui":
                work_num = current.data.arg["Duration_of_battle_k28_n"]
                pass
            elif current.data.arg["run_name"] == "gbyw":
                work_num = current.data.arg["Duration_of_battle_gbyw_n"]
                pass
            elif current.data.arg["run_name"] == "yuling":
                work_num = current.data.arg["Duration_of_battle_yuling_n"]
                pass
            linklist_str = linklist_str + str(work_num) + "次" + "\n"
            current = current.next
            pass
        return linklist_str
