import os


def recursion_file_catalogue(path, indent=0, maxi=-1):
    """按字典序递归输出目录结构
    :param path: str 文件路径
    :param indent: int 首次缩进空格(默认为 0，一般不用改变)
    :param maxi: int 最大展开层数(默认为 -1，表示全部展开)
    :return: 文件目录
    """
    if maxi != 0:
        try:
            lsdir = os.listdir(path)
        except PermissionError:  # 对于权限不够的文件不作处理
            pass
        else:
            for item in lsdir:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(' ' * indent, '+', item)
                    recursion_file_catalogue(full_path, indent + 4, maxi - 1)
                if os.path.isfile(full_path):
                    print(' ' * indent, '-', item)


if __name__ == '__main__':
    file_path = r'D:\my_temporary_files'
    print('---按字典序递归输出目录结构---')
    recursion_file_catalogue(file_path, 0, 2)
