import cv2

mode = 0
res = ((640, 480, 0), (1280, 1024, 2700000), (1600, 1200, 0))

avg = res[mode][2]

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

def isThereMotion(t0, t1):
  d1 = cv2.absdiff(t0, t1)
  sum = cv2.sumElems(d1)[0]
  global avg
  avg = avg*0.8 + sum*0.2 
  if sum > avg*1.05: print('ding!')
  print(sum, avg)
  return sum

cam = cv2.VideoCapture(0)
cam.set(3, res[mode][0])
cam.set(4, res[mode][1])

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:
  cv2.imshow( winName, diffImg(t_minus, t, t_plus) )

  # Read next image
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  print(isThereMotion(t, t_minus))

  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "Goodbye"
