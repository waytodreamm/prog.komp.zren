import cv2

def test_camera():
    print("Попытка подключения к камере...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Ошибка: Не удалось получить доступ к камере")
        print("Проверьте, подключена ли камера и не используется ли она другой программой")
        return False
    
    print("Камера успешно подключена!")
    print("Для выхода нажмите клавишу 'q'")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        cv2.imshow('Тест камеры', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Выключение камеры...")
            break
    
    # Корректное освобождение ресурсов
    print("Закрытие окон и освобождение камеры...")
    cap.release()
    cv2.destroyAllWindows()
    print("Камера успешно выключена")
    return True

if __name__ == "__main__":
    try:
        test_camera()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("Убедитесь, что OpenCV установлен командой: python -m pip install --user opencv-python")
