import cv2

def scan():
    y = 1
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()
    while y <= 150:
        i, img = cap.read()
        data, array, i = detector.detectAndDecode(img)
        if array is not None:
            if data:
                return data

        y += 1
    return "No Code Detected"

