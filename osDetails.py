import platform

keys = [x for x in dir(platform) if not x.startswith('_')]
if platform.system() == "Windows":
    keys.remove('dist')
    keys.remove('linux_distribution')

err = []
pythondata ={}
for k in keys:
    try:
        if k.startswith('py'):
            pythondata.update({k : str(eval('platform.' + k + '()'))})
        else:
            print(k + ' :=>> ' + str(eval('platform.' + k + '()')))

    except Exception as e:
        err.append(f'{k}:{e}')

print("****************************************")
for k,v in pythondata.items():
    print(k+" : "+v)
