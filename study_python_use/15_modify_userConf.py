# -*- coding: utf-8 -*-
"""
des: modify camera_tool's userConf.json file
auther: Mr.Chen
date: 2023-4-15
"""
import os
import json
import shutil


def modifyUserConfFile(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        json_list = json.load(f)
        for j in json_list:
            if 'A' in j['slotId'] or 'B' in j['slotId'] or 'D' in j['slotId']:
                try:
                    del j['ldc']
                except KeyError:
                    pass
                j['rawPub'] = 'true'
                j['instanceId'] += 1000
        f.close()
    with open(filename, 'w', encoding='utf-8') as fw:
        fw.write('[\n')
        for j in json_list:
            json.dump(j, fw, indent=4, ensure_ascii=False)
            if 'D1' not in j['slotId']:
                fw.write(',\n')
        fw.write('\n]')
        fw.close()


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
    modifyUserConfFile(filename)


if __name__ == '__main__':
    run()
