import cv2
import numpy as np 
import sys
# Create a VideoCapture object and read from input file
vfile=sys.argv[1]
cap = cv2.VideoCapture(vfile)
print("Video is Playing")

# Check if camera opened successfully

if (cap.isOpened()== False):

  print("Error opening video  file")

# Read until video is completed

while(cap.isOpened()):


  # Capture frame-by-frame

  ret, video_play = cap.read()

  if ret == True:


    # Display the resulting frame

    cv2.imshow('PLAYER', video_play)
      # Press Q on keyboard to  exit

    if cv2.waitKey(25) & 0xFF == ord('q'):

      break

  # Break the loop
  else:

    break
# When everything done, release
# the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()