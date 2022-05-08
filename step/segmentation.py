import step.util as util        
import cv2

class Segmentation:
    def fit(method, mode, load_dir, save_dir, print_format = "      |     "):
        
        file_type = "jpg"
        load_mode = 0
        load_list = util.read_list(load_dir, file_type)
        
        print_method_description = 0

        
        for load_path in load_list:
            img             = util.read_img(load_path, "cv2", load_mode, file_type)
            ret, th, text   = method(img, mode)
            save_path       = util.save_path(save_dir, load_dir, load_path, file_type) 
            
            util.write_img(th, save_path, mode)
            
            # 첫 이미지 실행시에만 method 설명 프린트
            print_method_description += 1
            if print_method_description == 1:
                print(text)
            
        if mode == "test":
            print(print_format+"test mode, no write")        
            
            
            
    def method1(img, mode="none"):
        
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
        text_1      = "\n   [STEP : {step}, METHOD : {method_num}, VERSION : {version}]  : {description}\n   ".format(step=step
                                                                                                      ,method_num=method_num
                                                                                                      ,version=version
                                                                                                      ,description =description)
        text_2      = "\n      |-> log :\n      |"
        text        = text_1 + text_2
        print_format = "      |     "                        
        
        # [B] 함수 본문
        
        import cv2
        import numpy as np 
        
        img       = cv2.medianBlur(img,5) # -- 노이즈 제거
        ret, th  = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 
        
        return ret, th, text
