from bdmc.modules.controller import CloseLoopController, MotorInfo
from bdmc.modules.cmd import CMD
import time


def main():
    # 假设我们有两个电机，根据实际情况修改电机信息
    motor_info_1 = MotorInfo(code_sign=1, direction=1)  # 电机 1 的信息，方向为正转
    motor_infos = [motor_info_1]

    # 查找可用的 USB 串口
    usb_ports = find_usb_tty()
    if not usb_ports:
        print("No USB serial ports found.")
        return
    # 假设使用第一个找到的 USB 串口
    port = usb_ports[0]

    # 创建 CloseLoopController 对象
    controller = CloseLoopController(motor_infos=motor_infos, port=port)

    try:
        # 打开串口连接
        controller.open(port)
        # 发送复位命令初始化电机
        controller.send_cmd(CMD.RESET)
        print("Motor controller initialized.")

        # 启动电机，设置速度
        controller.set_motors_speed([500, 500])  # 假设将两个电机的速度都设置为 500
        print("Motors started.")

        # 让电机运行一段时间
        time.sleep(10)  # 让电机运行 10 秒

        # 停止电机
        controller.set_motors_speed([0, 0])
        print("Motors stopped.")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # 关闭控制器
        if controller:
            controller.close()


def find_usb_tty(id_product=0, id_vendor=0):
    from bdmc import find_usb_tty
    usb_ports = find_usb_tty(id_product, id_vendor)
    return usb_ports


if __name__ == "__main__":
    main()
