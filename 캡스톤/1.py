from gpiozero import OutputDevice
import time

in_a = OutputDevice(23)
in_b = OutputDevice(24)

def fan_on():
    in_a.on()
    in_b.off()
    print("팬 모터 on - 정방향")

def fan_reverse():
    in_a.on()
    in_b.on()
    print("반대 방향")
def fan_off():
    in_a.off()
    in_b.on()
    print("팬 모터 off")
while True:
    try:
        fan_on()
        time.sleep(2)
        fan_reverse()
        time.sleep(2)
        fan_off()
    finally:
        print("종료")
