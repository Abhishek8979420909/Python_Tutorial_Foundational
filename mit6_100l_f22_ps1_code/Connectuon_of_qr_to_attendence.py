import cv2
import sqlite3
from datetime import datetime

def mark_attendance(id):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    now = datetime.now()
    c.execute('''
        INSERT INTO attendance (id, date, time)
        VALUES (?, ?, ?)
    ''', (id, now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S')))
    conn.commit()
    conn.close()

def scan_qr_code():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector(frame)
        if data:
            if data.startswith('id:'):
                id = data[3:]
                mark_attendance(id)
                print(f"Attendance marked for ID: {id}")
                cap.release()
                cv2.destroyAllWindows()
                break

        cv2.imshow('QR Code Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

# Main function
if __name__ == "__main__":
    scan_qr_code()
