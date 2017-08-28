import json
import threading
import copy

mcdic = {}

#创建锁
mcdic_mutex = threading.Lock()

#更新计算节点状态
def setmc(pn_code,mcjson):
    # 锁定
    mcdic_mutex.acquire()
    try:
        mcdic[pn_code] = dict(json.loads(mcjson))
        printmc()
    except:
        pass
    # 释放
    mcdic_mutex.release()

#获取计算节点状态
def getmc(pn_code):
    mcdic_mutex.acquire()
    sdic = copy.deepcopy(mcdic[pn_code])

    mcdic_mutex.release()
    return sdic

def printmc():
    for key in mcdic.keys():
        print("key=%s value=%s" % (key,mcdic[key]))
        smdic = mcdic[key]
        for skey in smdic.keys():
            print("skey=%s value=%s" % (skey,smdic[skey]))