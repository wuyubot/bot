'''
Author: y68 yeqiu6080@outlook.my
Date: 2025-02-03 17:30:04
LastEditors: yeqiu6080
LastEditTime: 2025-02-05 22:28:26
Description: file content
'''
import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
import wuyubot


wuyubot.init()
cfg = wuyubot.load_config()
nonebot.init(driver='~fastapi+~httpx+~websockets',**cfg)


driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)


nonebot.load_from_toml("pyproject.toml")


if __name__ == "__main__":
    
    nonebot.run()