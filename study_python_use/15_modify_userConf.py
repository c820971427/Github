"""
des: modify camera_tool's userConf.json file
auther: Mr.Chen
date: 2023-4-15
"""
import os
import json
import shutil
import jsonlines


# def modifyUserConfFile(filename: str):
#     with open('filename', 'w') as f:
#         contents = f.read()
#         print(contents)

# cameraJsonData = json.loads(filename)
# print(cameraJsonData)


def run():
    os.chdir('../tmp_files')
    # os.chdir('/home/mdc/csl/json')
    filename = 'userConf.json'
    if os.path.isfile('./userConf.json.bk'):
        pass
    else:
        shutil.copy(filename, 'userConf.json.bk')
        # os.popen(f'cp userConf.json userConf.json.bk')
        print('hello word!')
    print(filename)
    with open(filename, 'r') as f:
        # for item in jsonlines.Reader(f):
        #     print(item)
        contents = f.read()
        # f.close()
        result = json.loads(contents)
        # # content_
        print(result)
        result["cameraID"] = 1021
        result["rawPub"] = True
        try:
            del result["ldc"]
        except KeyError:
            pass
        print(result)
    with open(filename, 'w') as fw:
        json.dump(result, fw, indent=4, ensure_ascii=False)
        fw.close()

    # with open(filename, 'w') as ft:
    #     ft.write()

    # modifyUserConfFile(filename)


if __name__ == '__main__':
    run()
