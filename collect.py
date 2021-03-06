import os, keyboard
import cv2

cap = cv2.VideoCapture(1)

# Labels for image classes and the keyboard event keys associated with them
#label = {"s":"STRAIGHT", "r":"RIGHT", "l":"LEFT"}
label = {"x":"XBOX", "m":"MOUSE", "u":"USB"}
number = {label[i]:0 for i in label}

# Directory where data will be saved (will be created if does not exist)
data_dir = '/home/trim/Data/'
for index, value in enumerate(label):
    if not os.path.exists(data_dir+label[value]):
        os.makedirs(data_dir+label[value])

# Number of pictures to be taken per one class
pic_per_class = 500

while True:
    # Read in single frame from webcam
    ret, frame = cap.read()

    # Display the current frame
    cv2.imshow('FRAME', frame)

    for index, value in enumerate(label):
        if cv2.waitKey(1) & keyboard.is_pressed(value):
            if number[label[value]] <= pic_per_class:
                image_dir = data_dir + label[value] + "/" + str(number[label[value]]) + ".png"
                frame = cv2.resize(frame,(360,360), interpolation = cv2.INTER_NEAREST)
                cv2.imwrite(image_dir, frame)
                print image_dir
            number[label[value]]+=1


    # Press ESCAPE to quit the program
    if cv2.waitKey(1) & keyboard.is_pressed("esc"):
        break

cap.release()
cv2.destroyAllWindows()
