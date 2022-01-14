import cv2
import numpy as np
import imutils
import easyocr

def detectPlate(img):
   
   text = ""
   
   try:
      # frame gri tona cevirdik
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

      # filtre ile gürültüleri sildik
      bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
      # kenar tespiti yaptik
      edged = cv2.Canny(bfilter, 30, 200)  # Edge detection

      # countur lari bulduk
      keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      contours = imutils.grab_contours(keypoints)
      contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

      location = None
      for contour in contours:
         approx = cv2.approxPolyDP(contour, 10, True)
         if len(approx) == 4:
            location = approx
            break 
         
      # maskeleme islemi yaptik
      mask = np.zeros(gray.shape, np.uint8)

      # plakanin icinde bulundugu kırpılmıs resmi bulduk
      (x, y) = np.where(mask == 255)
      (x1, y1) = (np.min(x), np.min(y))
      (x2, y2) = (np.max(x), np.max(y))
      cropped_image = gray[x1:x2+1, y1:y2+1]

      # easyocr ile plakayı okuduk ve plakayı return ile dondurduk
      reader = easyocr.Reader(['en'])
      result = reader.readtext(cropped_image)

      text = result[0][-2]

   except:
      pass

   return text