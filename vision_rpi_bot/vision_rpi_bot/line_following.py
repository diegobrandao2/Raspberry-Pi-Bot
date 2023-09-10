import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class camera_sub(Node):

    def __init__(self):
        super().__init__('qr_maze_solving_node')
        self.camera_sub = self.create_subscription(Image,'/vision_rpi_bot_camera/image_raw',self.camera_cb,10)
        self.bridge=CvBridge()
    


    def camera_cb(self, data):
        frame = self.bridge.imgmsg_to_cv2(data,'bgr8')
        frame = frame[290:479,130:400]
        edged = cv2.Canny(frame, 60, 100)
        
        white_index=[]
        for index,values in enumerate(edged[:][85]):
            if(values == 255):
                white_index.append(index)
        print(white_index)

        if(len(white_index) == 2):
            cv2.circle(img=edged, center = (white_index[0],85), radius = 2 , color = (255,0,0), thickness=1)
            cv2.circle(img=edged, center = (white_index[1],85), radius = 2 , color = (255,0,0), thickness=1)
            mid_point_line = int ( (white_index[0] + white_index[1]) /2 )
            cv2.circle(img=edged, center = (mid_point_line,85), radius = 3 , color = (255,0,0), thickness=2)
        
        
        cv2.imshow('Frame',frame)
        cv2.imshow('Canny output',edged)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    sensor_sub = camera_sub()

    rclpy.spin(sensor_sub)
    sensor_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()