import os
import cv2

path = "imagens/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])
altura, largura, canais = frame.shape
tamanho = (largura, altura)
print(tamanho)

out = cv2.VideoWriter('Nascer.mp4', cv2.VideoWriter_fourcc(*'DIVX'),10 ,tamanho)
for i in range(0, count -1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("foi")