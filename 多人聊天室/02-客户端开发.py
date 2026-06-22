from socket import *
from threading import Thread

import wx

class MyClientFrame(wx.Frame):

    def __init__(self, username):
        super().__init__(None,101,F'{username}的客户端',wx.DefaultPosition,(400, 520))
        self.is_on = True
        # 创建一个面板，把面板放到窗口里面
        pl = wx.Panel(self)


        # 创建一个可伸缩的网格布局
        fg =wx.FlexGridSizer(wx.HORIZONTAL)

        # 创建3个按钮，并且把三个按钮按照水平的网格布局，看成一个整体
        connect_button = wx.Button(pl, size= (200,40), label= '进入聊天室')
        laeve_button   = wx.Button(pl, size= (200,40), label= '离开聊天室')

        fg.Add(connect_button, 0, wx.ALL)
        fg.Add(laeve_button, 0, wx.ALL)

        # 创建一个只读的文本框
        self.log_text = wx.TextCtrl(pl, size=(400, 260), style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.input_text = wx.TextCtrl(pl, size=(400, 140), style = wx.TE_MULTILINE)

        fg2 = wx.FlexGridSizer(wx.HORIZONTAL)

        # 创建3个按钮，并且把三个按钮按照水平的网格布局，看成一个整体
        clear_button = wx.Button(pl, size=(200, 40), label='重置')
        send_button = wx.Button(pl, size=(200, 40), label='发送')

        fg2.Add(clear_button, 0, wx.ALL)
        fg2.Add(send_button, 0, wx.ALL)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(fg, 1, wx.ALIGN_CENTER)
        box.Add(self.log_text, 1, wx.ALIGN_CENTER)
        box.Add(self.input_text, 1, wx.ALIGN_CENTER)
        box.Add(fg2, 1, wx.ALIGN_CENTER)

        pl.SetSizer(box)

        self.username = username
        #绑定鼠标点击的事件
        self.Bind(wx.EVT_BUTTON, source=connect_button, handler=self.connect_server)
        self.Bind(wx.EVT_BUTTON, source=send_button, handler=self.send_message)
        self.Bind(wx.EVT_BUTTON, source=laeve_button, handler=self.leave)

    def connect_server(self, event):
        """客户端连接服务器，并且要把自己的用户名发送给服务器"""
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1',8111))
        self.client_socket.send(self.username.encode('utf8'))
        self.is_on = True #表示客户端用户在聊天室

        t = Thread(target=self.recv_data)
        t.daemon = True
        t.start()

    def recv_data(self):
        """
        专门负责：在客户端接收消息的
        第一步：接收到服务器的消息
        第二部：把消息展示到客户端的只读文本框中
        :return:
        """
        while self.is_on:
            message = self.client_socket.recv(1024).decode('utf8')
            if message == 'laoxiao^leave^laoxiao':
                self.is_on = False
            else:
                self.log_text.AppendText(message)
                self.log_text.AppendText("-" * 60)
                self.log_text.AppendText("\n")
        self.client_socket.close()
        self.client_socket = None

    def send_message(self, event):
        """
        负责发送聊天信息到服务器
        :param event:
        :return:
        """
        if self.is_on:
            message = self.input_text.GetValue().strip()
            if message:
                self.client_socket.send(message.encode('utf8'))
                self.input_text.SetValue('')

    def leave(self, event):
        """
                 客户端离开聊天室
                 规定：1、当客户端发送：laoxiao^leave^laoxiao。就代表客户端马上要离开了，2、服务器也要发送同样的消息，客户端收到之后确认离开
                 1.客户端的窗口不关闭
                 2.客户端的线程要结束，socket要关闭
        """
        # self.is_on = False
        self.client_socket.send('laoxiao^leave^laoxiao'.encode('utf8'))

if __name__ == '__main__':

    username = input('请输入一个用户名:')

    app = wx.App()

    frame = MyClientFrame(username)

    frame.Show(True)

    app.MainLoop()