# made at 2021-08-19 05:07:00
# by Rahul-404

try:
	import cv2
	img = cv2.imread('images.jpeg', cv2.IMREAD_COLOR)
	print('Image loaded.')

	cv2.imshow('Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
except Exception as e:
	print('Image Not loaded.')
	print('Error: %s' % e)



	