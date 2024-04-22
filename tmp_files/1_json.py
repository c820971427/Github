import json

embed = {'id': 1, 'url': "www.baidu.com"}
with open('userConf1.json') as f:
    contents = f.read()
    # print(contents)
    model_list = json.loads(contents)
    # model_list = json.load(f)
    for model in model_list:
        print(model)
f.close()
for model in model_list:
    # for idx, value in model.items():
    #     print(idx, value)
    # jsObj = json.dumps(model, indent=4, ensure_ascii=False)
    with open('userConf.1bk.json', 'a') as fw:
        json.dump(model, fw, indent=4, ensure_ascii=False)
        # fw.write(jsObj)
    fw.close()
