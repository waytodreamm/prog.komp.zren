import cv2
from camera_test import test_camera
from motion_detection import detect_motion
from object_tracking import track_object

def main_menu():
    while True:
        print("\n=== Система видеонаблюдения ===")
        print("1. Проверка камеры")
        print("2. Обнаружение движения")
        print("3. Отслеживание объекта")
        print("4. Выход")
        
        choice = input("\nВыберите режим (1-4): ")
        
        if choice == '1':
            print("\nЗапуск проверки камеры... (Для выхода нажмите 'q')")
            test_camera()
        elif choice == '2':
            print("\nЗапуск обнаружения движения... (Для выхода нажмите 'q')")
            detect_motion()
        elif choice == '3':
            print("\nЗапуск отслеживания объекта...")
            print("Выделите область для отслеживания и нажмите ENTER")
            print("Для выхода нажмите 'q'")
            track_object()
        elif choice == '4':
            print("\nЗавершение работы...")
            break
        else:
            print("\nНеверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
