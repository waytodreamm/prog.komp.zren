try:
    import cv2
    print("OpenCV успешно установлен!")
    print("Версия OpenCV:", cv2.__version__)
except ImportError:
    print("Ошибка: OpenCV не установлен")
