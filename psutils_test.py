import psutil

keys = [x for x in dir(psutil) if not x.startswith('_')]
print(keys)

err = {}
cpu = {}
net = {}
mem = {}
running_services = {}
for k in keys:
    try:
        if k.startswith('cpu'):
            cpu.update({k: str(eval('psutil.' + k + '()'))})
        elif k.startswith('net'):
            net.update({k: str(eval('psutil.' + k + '()'))})
        elif k.endswith('_memory'):
            mem.update({k: str(eval('psutil.' + k + '()'))})
        elif k == 'sys' or k == 'pids' or k == 'test':
            continue
        else:
            print(k + ' : ' + str(eval('psutil.' + k + '()')))

    except Exception as e:
        err.update({k: str(e)})

print("****************************************")
print("************     DATA     **************")
print("****************************************")
for k, v in cpu.items():
    print(k + " : " + v)

for k, v in mem.items():
    print(k + " : " + v)

print("****************************************")
print("*********  Running services  ***********")
print("****************************************")
psutil.test()

# print("****************************************")
# print("************    error    ***************")
# print("****************************************")
# for k, v in err.items():
#     print(k + " : " + v)
