import os,sys
w = '''\033[96mdb   d8b   db db    db db    db db    db d8888b.  .d88b.  d888888b 
88   I8I   88 88    88 `8b  d8' 88    88 88  `8D .8P  Y8. `~~88~~' 
88   I8I   88 88    88  `8bd8'  88    88 88oooY' 88    88    88    
Y8   I8I   88 88    88    88    88    88 88~~~b. 88    88    88    
`8b d8'8b d8' 88b  d88    88    88b  d88 88   8D `8b  d8'    88    
 `8b8' `8d8'  ~Y8888P'    YP    ~Y8888P' Y8888P'  `Y88P'     YP    
                                                                   
                                                                   \033[0m'''
def oobe():
    print("\033[96mWelcome to use wuyubot!\033[0m")
    print("\033[96m找不到配置文件，即将生成默认配置到.\data\config\并退出，请填写后再运行。\033[0m")
    
def init():
    print(w)
    if not os.path.exists('./data/config/config.yaml'):
        oobe()
        # 退出程序
        sys.exit(0)
