#!/usr/bin/python2
import rospy
if __name__=='__main__':
	rospy.init_node('Ai_kak')
	inp = str(input())
	n1 = int(input())
	n2 = int(input())
	if inp == '1' :
		ans = n1 + n2
		print('{:.2f}' .format(ans))
	elif inp == '2' :
		ans = n1 - n2
		print('{:.2f}' .format(ans))


