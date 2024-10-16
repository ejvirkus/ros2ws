import rclpy
import serial
import struct
import time
from stanleycontroller import implementation
from TERA_gps import GpsPublisher

from std_msgs.msg import String
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0.1)
GPS = GpsPublisher()
#rclpy.init(args=None)

def listener_callback():
    #print(info)
    steering = implementation()
    print(f"steering value: ", steering)
    arduino.write(struct.pack("2h", int(steering), int(100)))
    #print(f"Pedals: {pedals}")
    #print(f"Sent: {sent}")
    time.sleep(0.05)
    #self.get_logger().info('I heard: "%s"' % msg.data)
    try:
        (val, ) = struct.unpack("h", arduino.read(struct.calcsize("h")))
        #print(f"Received: {val}")
        #print(struct.calcsize("i"))
    except:
        pass

if __name__ == '__main__':
    #rclpy.init(args=None)
    GPS.open_serial_connection()
    #rclpy.spin(listener_callback())
    while True:
        listener_callback()
    GPS.destroy_node()
    #rclpy.shutdown()
    