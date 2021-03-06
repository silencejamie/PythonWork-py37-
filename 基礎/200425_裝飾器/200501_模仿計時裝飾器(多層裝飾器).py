import time

# elapsed:0.5f => 表elapsed只取到小數點後五位
DEFAULT_FMT = "【{elapsed:0.5f}】 {name}({parameter}) -> {result}"


def auth(func):
    def wrapper(*args, **kwargs):
        print('使用auth裝飾器')
        username = input("帳號 ").strip()
        password = input("密碼 ").strip()
        if username == "jamie" and password == "123":
            print("歡迎登入【%s】" % username)
            print(func)
            res = func(*args, **kwargs)
            return res
        else:
            print("登入失敗，無法進行後續操作")
            return
    return wrapper


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print("使用clock裝飾器")
            start = time.time()
            print(func)
            res = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            name = func.__name__
            parameter = ", ".join(repr(arg) for arg in args)
            result = repr(res)
            print(fmt.format(**locals()))
            return res
        return wrapper
    return decorate


# 相當於 snooze = clock(fmt=DEFAULT_FMT)(snooze)
@clock()
def snooze(t):
    time.sleep(t)


# 相當於 snooze_2 = clock(fmt="{name}({parameter}) -> {elapsed}")(snooze_2)
@clock(fmt="{name}({parameter}) -> {elapsed}")
def snooze_2(t):
    time.sleep(t)


# 相當於 snooze_3 = auth(clock(fmt=DEFAULT_FMT)(snooze_3))
@auth
@clock()
def snooze_3(t):
    time.sleep(t)
# snooze_3 = auth(clock(fmt=DEFAULT_FMT)(snooze_3))


# snooze(1)
# snooze_2(1.5)

snooze_3(1)
# snooze_3(1)執行順序：
#   (1) 執行auth.wrapper，
#       此時wrapper中的func為clock(fmt=DEFAULT_FMT)(snooze_3)，也就是clock.decorate.wrapper
#   (2) 執行auth.wrapper中的func，相當於執行clock.decorate.wrapper
#   (3) 執行clock.decorate.wrapper下的func，相當於執行snooze_3本身
#   (4) 執行完(3)之後，return res，res相當於snooze_3的返回值
#   (5) 步驟(4)的res會先回傳給auth.wrapper下的res，最後回傳給用戶
