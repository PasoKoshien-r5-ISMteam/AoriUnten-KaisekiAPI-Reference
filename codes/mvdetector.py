import cv2
import os
import sys
import torch
import json

args = sys.argv

#Writed By KanataSaito

#回収した画像を1秒あたり1フレーム切り出してpngで保存する
def mv_cut(videopath,uuid):
    capture = cv2.VideoCapture(f"./{videopath}")
    fps = capture.get(cv2.CAP_PROP_FPS)
    count = 0

    while True:
        ret, frame = capture.read()
        if(not ret):
            break
        if(int(count%fps) == 0):
            path_num = int(count//fps)
            cv2.imwrite(f"./{uuid}/detec_temp/{path_num:02}.png",frame)
        count += 1
    detecmvfile(uuid)

#切り出した画像から物体検出を行い、物体のサイズ、位置を出力、切り抜いて保存する関数
def detecmvfile(uuid):
    model = torch.hub.load("ultralytics/yolov5","yolov5s",pretrained=True)
    detec_list = []
    for i in range(0,19):
        results = model(f"{uuid}/detec_temp/{str(i).zfill(2)}.png")
        objects=results.pandas().xyxy[0]
        for j in range(len(objects)):
            name = objects.name[j]
            xmin = objects.xmin[j]
            ymin = objects.ymin[j]
            width = objects.xmax[j] - objects.xmin[j]
            height = objects.ymax[j] - objects.ymin[j]
            detec_list.append({"number":i,"kind":name,"size":{"height":height,"width":width},"point":{"x":xmin,"y":ymin}})
    #print(json.dumps(detec_list,indent=2))
    detectedDataParse(detec_list,uuid)

#出力した物体のサイズ、位置から煽ってきている車輌を特定し、煽られ率を算出できる形式に変換する
def detectedDataParse(detectedData, uuid):
    maxsize_obj = []
    detec_car_obj = []
    temp_list = []

    for value in detectedData: #検知した中で、車、トラックだけを絞り込む
        if(value['kind'] == "car" or value['kind'] == "truck"):
            temp_list.append(value)
    sorted(temp_list,key=lambda x: x['number'])
    for i in range(0,20):
        maxh=0
        maxw=0
        for j in range(0,len(temp_list)):
            if(temp_list[j]['number'] == i):
                if(temp_list[j]['size']['height'] > maxh and temp_list[j]['size']['width'] > maxw):
                    maxh = temp_list[j]['size']['height']
                    maxw = temp_list[j]['size']['width']
                    try:
                        maxsize_obj[i] = temp_list[j]
                    except:
                        maxsize_obj.insert(i,temp_list[j])

    calculateAorarePoint(maxsize_obj,uuid)

def calculateAorarePoint(targetcar,uuid):
    size = []
    for value in targetcar:
        size.append(value['size']['height']*value['size']['width'])
    
    print(int((sum(size)/len(size))/85000*100))

mv_cut(args[1],args[2])