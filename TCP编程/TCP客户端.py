import socket

# 需求：即时聊天

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('192.168.1.63', 8000)
client_socket.connect(server_addr)

while True:
    # 正式开始聊天

    # 给服务端发送聊天信息
    send_msg = input('客户端>>')

    if send_msg == 'quit' or send_msg == 'exit' or send_msg == 'q':
        client_socket.send(send_msg.encode('utf8'))
        break

    client_socket.send(send_msg.encode('utf8'))

    msg = client_socket.recv(1024).decode('utf8')

    if msg == 'quit' or msg == 'exit' or msg == 'q':
        break

    print(f'来自客户端ip:{server_addr[0]},端口号:{server_addr[1]}:{msg}')

client_socket.close()