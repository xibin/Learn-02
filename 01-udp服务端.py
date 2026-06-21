import socket

#创建一个udp的socket的对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ip = 192.168.1.63 其他主机可以和当前的服务端通信
# ip = 127.0.0.1 其他主机不可以和当前的服务器通信,除非客户端都在本地
# ip = '' 该服务端绑定到所有的ip地址
# server_socket.bind(('192.168.1.63', 6666))
server_socket.bind(('', 6666))

# 注意 recvfrom是个阻塞函数，如果没有接收到数据包，那么程序暂停到这里不动


while True:
    # msg是收到的数据，addr是原地址和端口号
    msg, addr = server_socket.recvfrom(1024*10)
    if msg.decode("utf8") == 'quit' or msg.decode("utf8") == 'exit' or msg.decode("utf8") == 'q':
        break
    print(f'来自客户端ip:{addr[0]},端口号:{addr[1]}的消息:{msg.decode("utf8")}')

    #服务端也可以发送数据到客户端
    send_msg = input('服务端>>')

    if send_msg== 'quit' or send_msg == 'exit' or send_msg == 'q':
        server_socket.sendto(send_msg.encode('utf8'), addr)
        break
    # sendto发送的数据不能是字符串，只能是字节数据，字符串的encoding函数
    server_socket.sendto(send_msg.encode('utf8'), addr)

#关闭socket
server_socket.close()