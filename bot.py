import nonebot
from nonebot.adapters.qq import Adapter


nonebot.init()

driver = nonebot.get_driver()
nonebot.get_driver().register_adapter(Adapter)

nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()
