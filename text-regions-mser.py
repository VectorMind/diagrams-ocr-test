import cv2

# Load the image
img = cv2.imread('test_slide.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect text regions using MSER
mser = cv2.MSER_create()
regions, _ = mser.detectRegions(gray)

# Extract the text regions as bounding boxes
boxes = []
for region in regions:
    x, y, w, h = cv2.boundingRect(region)
    boxes.append((x, y, x+w, y+h))

# Draw the bounding boxes on the image
for box in boxes:
    cv2.rectangle(img, box[:2], box[2:], (0, 255, 0), 2)

# Display the image with bounding boxes
cv2.imshow('image', img)
cv2.waitKey(0)