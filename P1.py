import cv2                                                                           #import کردن کتابخانه opencv
import numpy as np                                                                   #importکردن کتابخانه numpy    

def zoomin(event,x,y,flags,param):
    
    if event==cv2.EVENT_LBUTTONDBLCLK :                                              #با دابل کلیک کاربر بدنه اجرا شود

        mask=np.zeros((img.shape[:2]), dtype='uint8')                                #ایجاد ارایه  هم اندازه تصویر
        cv2.rectangle(mask,(x-130,y-30),(x+130,y+30),(255,255,255),-1)               #ایجاد مستطیلی با این اندازه ها روی ارایه ایجاد شده

        x1 = x - 160
    
        x2 = x + 160
        
        y1 = y - 96
    
        y2 = y + 96
    
        p1 = np.float32([[x1,y1],[x2,y1],[x1,y2],[x2,y2]])                        #ماتریس مختصات نقاط اولیه و نهایی عکس.       
        p2 = np.float32([[0,0],[320,0],[0,192],[320,192]])                        #مختصات نقاط بالا-چپ  بالا-راست  پایین-چپ  پایین-راست

        M = cv2.getPerspectiveTransform(p1,p2)                                    #ماتریس M ماتریس انتقال perspective

        dst = cv2.warpPerspective(img,M,(320,192))                                #اعمال perspective
        zoom=cv2.resize(dst,(dst.shape[1]+130,dst.shape[1]+30))                   #بزرگتر کردن تصویر با عمل resize
        cv2.imshow('zoom in',zoom)
        cv2.waitKey(0)

        cpy=zoom.copy()                                                          #کپی گرفتن از محدوده انتخابی کاربر
        blur=cv2.blur(cpy,(10,10))                                               #بلور کردن محدوه انتخابی
        cv2.imshow('blurred',blur)

img=cv2.imread('obama.png')                                                      #وارد کردن عکس
cv2.namedWindow('image')                                                         #ایجاد پنجره جدید
cv2.setMouseCallback('image',zoomin)                                             #کنترل کننده موس را برای پنجره ایجاد شده تنظیم میکنیم

while(1):

    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xff==ord('e'):                                          # زمانی ک کاربر کلید e را فشار داد از برنامه خارج شود
        break

cv2.destroyAllWindows()                                                          #بستن همه پنجره های باز