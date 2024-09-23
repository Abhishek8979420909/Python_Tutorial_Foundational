import qrcode
import cv2
import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function to generate QR Code
def generate_qr_code(id, filename):
    data = f"id:{id}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

# Function to create the SQLite database
def create_database():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id TEXT,
            date TEXT,
            time TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to mark attendance
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

# Function to scan QR code and mark attendanc
def scan_qr_code():
    # Initialize the QRCodeDetector
    detector = cv2.QRCodeDetector()
    
    # Start video capture (default camera)
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
        
        # Detect and decode the QR code
        data, bbox, _ = detector.detectAndDecode(frame)
        
        # If QR code is detected
        if data:
            print(f"QR Code data: {data}")
            # You can add code here to handle the detected data
        
        # Display the frame
        cv2.imshow("QR Code Scanner", frame)
        
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

# Function to open the QR code scanner
def open_scanner():
    scan_qr_code()

# Create the SQLite database
create_database()

# Create Tkinter UI
root = tk.Tk()
root.title("Automatic Attendance System")

btn = tk.Button(root, text="Start QR Code Scanner", command=open_scanner)
btn.pack(pady=20)

root.mainloop()

