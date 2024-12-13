import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image_files = [f for f in os.listdir('.') if f.endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    img = cv2.imread(image_file)
    if img is None:
        print(f"Could not read {image_file}. Skipping.")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(image_file, 'image face rectangle coordinate', f'({x}, {y}), ({x + w}, {y + h})')
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    output_file = f"detected_{image_file}"
    cv2.imwrite(output_file, img)
    print(f"Processed {image_file}, saved as {output_file}")

