import urllib.request
import cv2
import numpy as np
import time
from paddleocr import PaddleOCR
from check import check_v4
from collections import Counter
# from modules import change_contrast

################### url 연결 ###################
url='http://192.168.0.174:8080/shot.jpg'

class IpCam():

    def last_return(l):
        cnt = Counter(l)
        return cnt.most_common()[0][0]
    

    def cam_2(url):
        # ocr = PaddleOCR()
        cnt = 0
        warning_code =""
        wear = ""
        start = time.time()
        l =[]

        while cnt<5:
            while_start = time.time()
            imgResp = urllib.request.urlopen(url)
            imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
            img = cv2.imdecode(imgNp,-1)  # 뭐여
            
            # 이미지 사이즈 줄이기
            img = cv2.resize(img, (640 , 640), interpolation=cv2.INTER_AREA)
            
            cnt+=1
            # image = cv2.imread(img)
            result = check_v4.Model.calculate(img)
            l.append(result)
            while_end = time.time()
            print(f"{cnt}번째 while문 소요시간",while_end-while_start)
            print("l : ", l)

        warning_code = IpCam.last_return(l)
        print("warning_code : ", warning_code)
        if warning_code == "G":
            wear = "헬멧, 조끼"
        elif warning_code == "VG":
            wear = "헬멧"
        elif warning_code == "HVG":
            wear = "모두착용하지않음"
        elif warning_code == "HG":
            wear = "조끼"
        elif warning_code == "V":
            wear = "헬멧, 고글"
        elif warning_code == "HV":
            wear = "고글"
        elif warning_code == "H":
            wear = "고글, 조끼"
        elif warning_code == "N":
            wear = "모두착용했습니다."

        end = time.time()
        print(f"총소요시간 : ",end-start)
        
        
        return {"wc" : warning_code, "wr" : wear}
        #     return img
        #     ######################################
        #     # OCR 실행
        #     result = ocr.ocr(img)

        #     # 인식된 텍스트를 화면에 출력
        #     if result:
        #         for res in result[0]:
        #             text = res[1][0]  # text
        #             percentage = res[1][1]  # 확률
        #             show_text = text + ' : ' + str(round(percentage,3))

        #             # 인식된 텍스트를 화면에 출력
        #             font = cv2.FONT_HERSHEY_SIMPLEX
        #             frame_with_text = cv2.putText(img, show_text, (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        #             # put the image on screen
        #             cv2.imshow('IPWebcam', frame_with_text)
        #             return img
        #     else:
        #         cv2.imshow('IPWebcam', img)
        #         return img

        #     # To give the processor some less stress
        #     time.sleep(0.1)

        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         cv2.destroyAllWindows()
        #         break
        # return img
        # cv2.destroyAllWindows()
        # return img