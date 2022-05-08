class Segmentation:
    
    # 포맷팅 후 지우기
    def method1(load_dir,save_dir,mode="none"):
        """
        방식 설명 : ~~ 에서 제공하는 툴을 사용한 수동 감지법 
        """
        print("- Segmentation (method 1) : ~~ 에서 제공하는 툴을 사용한 수동 감지법")
    
    def seg1(load_dir,save_dir,mode="none"):
        import cv2
        import numpy as np 
        from matplotlib import pyplot as plt 
        import os
        path      = "./"
        load_file = os.listdir(load_dir)
        load_list = [load_dir + "/" + f for f in load_file if f.endswith(".jpg")]

        for jpg in load_list:
            # 1. load
            img       = cv2.imread(jpg,0)
            
            # 2. segentation
            img       = cv2.medianBlur(img,5) # -- 노이즈 제거
            ret, th1  = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 

            # write
            if not os.path.isdir(save_dir):
                print("Make a new directory : {}".format(save_dir))
                os.mkdir(save_dir)
                exit(1)
                
            save_path = jpg.replace(load_dir, save_dir)    
            cv2.imwrite(save_path, th1)    
        
            if mode == "show":
                plt.imshow(th1,'gray')
                plt.show()
