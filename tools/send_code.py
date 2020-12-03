
codes = {
    # 文章
    10001: {"code": 10001, "msg": "请求成功"},
    
    # 通用
    12001: {"code": 12001, "msg": "请用POST请求"}，
    12002: {"code": 12002, "msg": "请用GET请求"},
    
}



def GetCode(code):
    return codes[code]