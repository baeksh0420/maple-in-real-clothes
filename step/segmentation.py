class Segmentation:

    def method1(load_dir,save_dir,mode="none"):
        
        """
        작업 히스토리 (역순으로 작성)
        - 2022/05/08 (olive46) - 함수 기본 골자 세팅    
        - 2022/05/01 (olive46) - load_dir내 모든 이미지에 적용하도록 for문 포함
        """
        
       # [A] 방식 설명 (= 각 파이프라인 스텝별 방법을 구분할 수 있는 설명 또는 버전)

        step        = "Segmentation"                   
        method_name = Segmentation.method1.__name__    
        method_str  = method_name.rstrip('0123456789') 
        method_num  = method_name[len(method_str):]    
        version     = "0.0"                            
        description = "cv2를 활용한 방법"              
        print("\n   [STEP : {step}, METHOD : {method_num}, VERSION : {version}]  : {description}\n   ".format(step=step
                                                                                                      ,method_num=method_num
                                                                                                      ,version=version
                                                                                                      ,description =description))
        print("      |-> log :\n      |")              
        print_format = "      |     "                        
        
        # [B] 함수 본문
        
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
            
            # 2. segmentation
            img       = cv2.medianBlur(img,5) # -- 노이즈 제거
            ret, th1  = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 

            # 3. write
            if mode == "live":
                if not os.path.isdir(save_dir):
                    print(print_format+"Make a new directory : {}".format(save_dir))
                    os.mkdir(save_dir)
                    exit(1)

                save_path = jpg.replace(load_dir, save_dir)    
                cv2.imwrite(save_path, th1)    
                
            # 4. additional mode - show, debug, ....
            if mode == "show":
                plt.imshow(th1,'gray')
                plt.show()

        # 3. no write - test mode, for setting to print once
        if mode == "test":
            print(print_format+"test mode, no write")
                
