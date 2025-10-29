import cv2
import os
import numpy as np

def check_opencv_face():
    try:
        cv2.face.LBPHFaceRecognizer_create()
        return True
    except AttributeError:
        print("Ошибка: Модуль face не найден!")
        print("Выполните следующие команды:")
        print("1. pip uninstall opencv-python")
        print("2. pip install --user opencv-contrib-python")
        return False

def train_recognizer(data_folder):
    if not check_opencv_face():
        return None, None
        
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    faces = []
    labels = []
    label_dict = {}
    current_label = 0
    
    # Загружаем фотографии из базы
    for filename in os.listdir(data_folder):
        if filename.endswith(".jpg"):
            name = filename.split('_')[0]
            if name not in label_dict:
                label_dict[name] = current_label
                current_label += 1
            
            image_path = os.path.join(data_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces.append(image)
            labels.append(label_dict[name])
    
    recognizer.train(faces, np.array(labels))
    return recognizer, label_dict

def recognize_face():
    if not check_opencv_face():
        return
        
    if not os.path.exists('faces') or len(os.listdir('faces')) == 0:
        print("База данных лиц пуста! Сначала создайте базу.")
        return
        
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer, label_dict = train_recognizer('faces')
    
    # Инвертируем словарь для получения имени по метке
    name_dict = {v: k for k, v in label_dict.items()}
    
    cap = cv2.VideoCapture(0)
    print("Распознавание лиц запущено. Нажмите 'q' для выхода.")
    
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(roi_gray)
            
            # Если уверенность меньше 70, считаем что лицо распознано
            if confidence < 70:
                name = name_dict[label]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f"{name} ({int(100-confidence)}%)", 
                           (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.9, 
                           (0, 255, 0), 2, cv2.LINE_AA)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, "Неизвестный", (x, y-10), 
                           cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2, 
                           cv2.LINE_AA)
        
        cv2.imshow('Распознавание лиц', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_face()
