import cv2
from ultralytics import YOLO


model = YOLO("yolo11n.pt") 


cap = cv2.VideoCapture(0)

print("Starting Privacy Guard... Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    
    results = model(frame, stream=True, conf=0.4)

    for r in results:
        for box in r.boxes:
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])

            
            if model.names[cls] == 'person':
                
                x1, y1 = max(0, x1), max(0, y1)
                
                
                roi = frame[y1:y2, x1:x2]
                if roi.size != 0: 
                    blur_roi = cv2.GaussianBlur(roi, (51, 51), 0)
                    frame[y1:y2, x1:x2] = blur_roi

                    
                    cv2.putText(frame, "Privacy Filter", (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 5. Output display
    cv2.imshow("My Custom AI Project", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()