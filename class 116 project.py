import cv2


img = cv2.imread("solar-system.jpg")


texts = {
    "Sun": {"text": "Sun", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (105, 60), "size": 1, "color": (0, 0, 0)},
    "Mercury": {"text": "Mercury", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (290, 35), "size": 0.7, "color": (0, 0, 0)},
    "Venus": {"text": "Venus", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (340, 65), "size": 0.7, "color": (0, 0, 0)},
    "Earth": {"text": "Earth", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (420, 20), "size": 0.7, "color": (0, 0, 0)},
    "Mars": {"text": "Mars", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (500, 60), "size": 0.7, "color": (0, 0, 0)},
    "Jupiter": {"text": "Jupiter", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (610, 15), "size": 0.7, "color": (0, 0, 0)},
    "Saturn": {"text": "Saturn", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (760, 25), "size": 0.7, "color": (0, 0, 0)},
    "Uranus": {"text": "Uranus", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (900, 70), "size": 0.7, "color": (0, 0, 0)},
    "Neptune": {"text": "Neptune", "font": cv2.FONT_HERSHEY_SIMPLEX, "pos": (980, 35), "size": 0.7, "color": (0, 0, 0)}
}


for planet, text in texts.items():
    cv2.putText(img, text["text"], text["pos"], text["font"], text["size"], text["color"], 2)


cv2.imshow("output", img)
img = cv2.imread("mercury.jpg")
img = cv2.imread("venus.jpg")
img = cv2.imread("earth.jpg")
img = cv2.imread("mars.jpg")
img = cv2.imread("jupiter.jpg")
img = cv2.imread("saturn.jpg")
img = cv2.imread("urnaus.jpg")
img = cv2.imread("neptune.jpg")






cv2.waitKey(0)


cv2.imwrite("Solar_systemwithname.jpg", img)
