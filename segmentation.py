class Segmentation:
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
