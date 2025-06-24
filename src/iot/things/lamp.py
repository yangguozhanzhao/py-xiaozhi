from src.iot.thing import Thing
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

class Lamp(Thing):
    def __init__(self):
        super().__init__("Lamp", "一个测试用的灯")
        self.power = False

        logger.info("[虚拟设备] 灯设备初始化完成")

        # 定义属性
        self.add_property("power", "灯是否打开", lambda: self.power)

        # 定义方法
        self.add_method("TurnOn", "打开灯", [], lambda params: self._turn_on())

        self.add_method("TurnOff", "关闭灯", [], lambda params: self._turn_off())

    def _turn_on(self):
        self.power = True
        logger.info("[虚拟设备] 灯已打开")
        return {"status": "success", "message": "灯已打开"}

    def _turn_off(self):
        self.power = False
        logger.info("[虚拟设备] 灯已关闭")
        return {"status": "success", "message": "灯已关闭"}
