import rospy
import math
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def move_to_goal(x, y, orientation):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = math.sin(orientation / 2)
    goal.target_pose.pose.orientation.w = math.cos(orientation / 2)

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
    else:
        return client.get_result()

def main():
    rospy.init_node('move_robot')
    
    # Check connection to the move_base action server
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    rospy.loginfo("Waiting for move_base action server...")
    connected = client.wait_for_server(rospy.Duration(5.0))  # Wait for 5 seconds
    if not connected:
        rospy.logwarn("Failed to connect to move_base action server")
        return  # Stop the script if not connected to the server
    
    rospy.loginfo("Connected to move_base action server")
    
    # Move to each location
    move_to_goal(-2, 1, 0)
    move_to_goal(-1.5, -2, 0)
    move_to_goal(2, 1, 0)
    move_to_goal(0.5, -2, 0)

if __name__ == '__main__':
    main()


