import paramiko
from scp import SCPClient


class ConnectShell:
    def remoteConnect(self):
        # 服务器相关信息,下面输入你个人的用户名、密码、ip等信息
        ip = "192.168.30.101"
        port = 22
        user = "root"
        password = "huawei"

        # 创建SSHClient 实例对象
        ssh = paramiko.SSHClient()
        # 调用方法，表示没有存储远程机器的公钥，允许访问
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接远程机器，地址，端口，用户名密码
        ssh.connect(ip, port, user, password, timeout=10)
        # 输入linux命令
        print("check status %s OK\n" % ip)
        # ssh.exec_command('echo "test" >> /a.txt')
        ls = "pwd"
        stdin, stdout, stderr = ssh.exec_command(ls)
        # 输出命令执行结果
        result = stdout.read()
        print(result)
        trans_file = r'D:\PycharmProjects\pythonProject' + r'\2_python.py'
        remote_file = '/root'
        scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
        try:
            scpclient.put(trans_file, remote_file)
        except FileNotFoundError as e:
            print(e)
            print(r'系统找不到指定文件' + trans_file)
        else:
            print('文件传输成功！')
        # ssh.exec_command('python3 /root/2_python.py > out_file.txt')
        # file = ssh.exec_command('python3 /root/2_python.py')
        # print(file)
        # 关闭连接
        ssh.close()


Connect_linux = ConnectShell()
Connect_linux.remoteConnect()
