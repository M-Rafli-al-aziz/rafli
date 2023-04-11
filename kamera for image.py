import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
                help="max buffer size")
args =vars(ap.parse_args())

# Ruang warna
lower = {'red': np.array([0, 100, 70], np.uint8), 'green': np.array([30, 0, 132], np.uint8),
         'yellow': np.array([25, 140, 131], np.uint8),
         'orange': np.array([24, 255, 240], np.uint8)}
upper = {'red': np.array([10, 200, 255], np.uint8), 'green': np.array([39, 153, 150], np.uint8),
         'yellow': np.array([29, 210, 240], np.uint8),
         'orange': np.array([24, 255, 240], np.uint8)}

colors = {'red': (0, 0, 255), 'green': (0, 255, 0), 'yellow': (0,255,217),
          'orange': (0, 140, 255)}

warna = {'red': "Merah : Matang",
         'yellow': "kuning : Matang",
         'orange': "Oranye : Hampir Matang",
         'green': "Hijau : Mentah",}

if not args.get("video", False):
    camera = cv2.VideoCapture(0)

else:
    camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()
    if args.get("video") and not grabbed:
        break
    # Proses atau eksekusi
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    count = {'red': 0, 'yellow': 0, 'orange': 0, 'green': 0}

    for key, value in upper.items():
        kernel = np.ones((9, 9), np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key])
        mask = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=2)
        mask = cv2.GaussianBlur(mask, (11, 11), 0)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                cv2.putText(frame, warna[key], (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
                count[key] += 1

    # Show the output image
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to quit
    if key == ord("q"):
        break

# Release the video capture object and close the window
camera.release()
cv2.destroyAllWindows()
