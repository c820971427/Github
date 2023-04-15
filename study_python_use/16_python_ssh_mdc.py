import paramiko
import time
from scp import SCPClient


def remoteConnect(ssh, ip: str, port: str, user: str, password: str) -> None:
    # 连接远程机器，地址，端口，用户名密码
    try:
        ssh.connect(ip, port, user, password, timeout=10)
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("无法链接到远端服务器，请检查ip, port, user, password")
        return 1
    except TimeoutError:
        print("超时未连接到远程服务器")
        return 1
    print("check status %s OK\n" % ip)


# 向远程服务器传输文件
def transFile(ssh, trans_file: str, remote_file: str):
    scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
    try:
        scpclient.put(trans_file, remote_file)
    except FileNotFoundError as e:
        print(e)
        print(r'系统找不到指定文件' + trans_file)
    else:
        print('文件传输成功！')


def closeSSHConnect(ssh):
    # 关闭连接
    ssh.close()


# 输入远程服务器linux信息
linux_ip = "192.168.30.101"
linux_port = 22
linux_user = "root"
linux_password = "huawei"
# trans_file = r'./15_modify_userConf.py'
trans_file1 = r'D:\PycharmProjects\pythonProject' + r'\2_python.py'
remote_file1 = '/root'
# 创建SSHClient 实例对象
linux_ssh = paramiko.SSHClient()
# 调用方法，表示没有存储远程机器的公钥，允许访问
linux_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remoteConnect(linux_ssh, linux_ip, linux_port, linux_user, linux_password)
transFile(linux_ssh, trans_file1, remote_file1)
# 输入linux命令
# ssh.exec_command('echo "test" >> /a.txt')
# ls = "cat /etc/issue"
ls = 'python3 /home/mdc/csl/15_modify_userConf.py'
stdin, stdout, stderr = linux_ssh.exec_command(ls)
# 输出命令执行结果
result = (stderr.read(), stdout.read())
print(result)
time.sleep(10)
while remoteConnect(linux_ssh, linux_ip, linux_port, linux_user, linux_password):
    time.sleep(20)

linux_ssh.exec_command('python3 /root/2_python.py > out_file.txt')
file = linux_ssh.exec_command('python3 /root/2_python.py')
print(file)
closeSSHConnect(linux_ssh)
