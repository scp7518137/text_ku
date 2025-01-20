from pyuptech import OnBoardSensors


def main():
    # 创建OnBoardSensors对象
    sensor_controller = OnBoardSensors()
    # 初始化所有GPIO引脚为输入模式
    sensor_controller.set_all_io_mode(0)
    a = sensor_controller.get_all_io_mode()
    print(a)

if __name__ == "__main__":
    main()