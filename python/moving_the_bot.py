import math 
import rospy
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion


rospy.init_node('robot_controller', anonymous=True)


pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


rospy.Subscriber('/odom', Odometry, odom_callback)



def odom_callback(msg):
    global x, y, theta
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    quaternion = (
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w)
    euler = euler_from_quaternion(quaternion)
    theta = euler[2]


def mov_bot(x2,y2)
    vel_msg = Twist()



    target_x = x2  # set target x coordinate
    target_y = y2  # set target y coordinate



    tolerance = 0.1  # set tolerance for how close the robot needs to be to the target coordinates



    while not rospy.is_shutdown():
        # calculate the distance and angle to the target coordinates
        distance = ((target_x - x) ** 2 + (target_y - y) ** 2) ** 0.5
        angle = math.atan2(target_y - y, target_x - x)
        angle_diff = angle - theta

        # adjust the angular velocity to face the target coordinates
        if abs(angle_diff) > tolerance:
            vel_msg.angular.z = k * angle_diff                                # k is constant to adjust speed
        else:
            vel_msg.angular.z = 0

        # adjust the linear velocity to move towards the target coordinates
        if distance > tolerance:
            vel_msg.linear.x = k * distance
        else:
            vel_msg.linear.x = 0

        # publish the velocity commands to the robot
        pub.publish(vel_msg)

        # check if the robot has reached the target coordinates
        if distance <= tolerance:
            break

        # sleep for a short period of time to allow the robot to move
        rospy.sleep(0.1)

    # stop the robot by setting the velocities to zero
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)



    rospy.spin()

