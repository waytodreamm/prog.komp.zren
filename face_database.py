import cv2
import os

def create_face_database(name):
    # Создаем папку для фотографий если её нет
    if not os.path.exists('faces'):
        os.makedirs('faces')
        
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    count = 0
    
    print(f"Создание базы данных лица для {name}")
    print("Держите голову прямо перед камерой")
    
    while count < 100:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            if count < 100:
                cv2.imwrite(f"faces/{name}_{count}.jpg", frame[y:y+h, x:x+w])
                count += 1
                print(f"Сохранено фото {count}/100")
        
        cv2.imshow('Создание базы лиц', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("База данных лица создана успешно!")

if __name__ == "__main__":
    name = input("Введите ваше имя: ")
    create_face_database(name)
