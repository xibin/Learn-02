import socket

#创建一个udp的socket的对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#客户端的socket是不需要bind，所以由操作系统分配一个随机的端口号

while True:

    # 发送消息给服务端
    send_msg = input('客户端>>')
    if send_msg == 'quit' or send_msg == 'exit' or send_msg == 'q':
        # 把退出消息发送给服务器端，然后退出循环
        client_socket.sendto(send_msg.encode('utf8'), ('192.168.1.63', 6666))
        break
    # snedto必须要指定目标地址和端口号
    client_socket.sendto(send_msg.encode('utf8'), ('192.168.1.63', 6666))

    # 接受服务器发送来的数据
    msg, addr = client_socket.recvfrom(1024*10)

    if msg.decode("utf8") == 'quit' or msg.decode("utf8") == 'exit' or msg.decode("utf8") == 'q':
        break
    print(f'来自服务端ip:{addr[0]},端口号:{addr[1]}的消息:{msg.decode("utf8")}')

client_socket.close()
