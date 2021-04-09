from 类 import commons

def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    if hasattr(commons, inp):
        func = getattr(commons, inp)
        func()
    else:
        print("404")


    # if inp == "login":
    #     login()
    # elif inp == "logout":
    #     logout()
    # elif inp == "home":
    #     home()
    # else:
    #     print("404")


if __name__ == '__main__':
     while True:
         run()