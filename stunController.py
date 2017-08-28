import json

def requestProcesser(data):
    try:
        reqDic = dict(json.loads(data))

        strMetho = reqDic.get("method")

        if strMetho=='request_p2p':            #客户端发起请求
            p2pStart(reqDic)
    except:
        pass

def p2pStart(reqDic):
    pass
    # method”:”request_p2p”,
    # “hd_id”:”12345678”，
    # "pn_id": "123456",
    # “session”:”abcdefg”,
    # “nat”:”pub | full | resi | resp | sym”,
    # “local_ip”:”xx.xxx.xxx”,
    # ”extend_ip”:”xxx.xxx.xxx.xxx”,
    # "sport": "3449",
    # “eport1:”111”,
    # ”eport2”:”222”,
    # ”eport3”:”3333”,
    # ”eport4”:”5555”