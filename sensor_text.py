import time
from pyuptech import OnBoardSensors

def main():
    sensor_controller = OnBoardSensors()
    sensor_controller.adc_io_open().set_all_io_mode(0)
    while True:
        try:
            gpio_levels = sensor_controller.io_all_channels()
            print(f"GPIO 引脚的电平状态（二进制）: {gpio_levels:08b}")
            for i in range(8):
                pin_level = (gpio_levels >> i) & 1
                print(f"引脚 {i} 的电平: {'高' if pin_level else '低'}")
            # 每隔 1 秒获取一次电平信息
            time.sleep(1)
        except Exception as e:
            print(f"获取 GPIO 引脚电平时出现错误: {e}")


if __name__ == "__main__":
    main()