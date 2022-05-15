# !pip install opencv-python
# !pip install matplotlib
# !pip install tqdm
# !pip install git
# !pip install git+https://github.com/sedthh/pyxelate.git

import step.util as util
import cv2
# from skimage import io

class Pixelate:
    def fit(method, mode, load_dir, save_dir, print_format = "      |     "):
        
        file_type = "jpg"
        load_mode = None #cv2.IMREAD_COLOR
        load_list = util.read_list(load_dir, file_type)
        
        print_method_description = 0
        
        for load_path in load_list:
            img             = util.read_img(load_path, "cv2", load_mode)
#             img             = util.read_img(load_path, "io", load_mode) # 메모리 큼. 비교 필요
            th, text        = method(img, mode)
            th             = cv2.resize(th, dsize=(192,256), interpolation=cv2.INTER_LINEAR)
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
        - 2022/04/24 (joshua)  - load_dir내 모든 이미지에 적용하도록 for문 포함
        """
        
        # [A] 방식 설명 __________________________________________________________________________________________________________
        step        = "Pixelate"                   
        method_name = Pixelate.method1.__name__    
        method_str  = method_name.rstrip('0123456789') 
        method_num  = method_name[len(method_str):]    
        version     = "0.0"                            
        description = "https://github.com/sedthh/pyxelate.git의 pyxelate를 사용한 방법"              
        text_1      = "\n   [STEP : {step}, METHOD : {method_num}, VERSION : {version}]  : {description}\n   ".format(step=step
                                                                                                      ,method_num=method_num
                                                                                                      ,version=version
                                                                                                      ,description =description)
        text_2      = "\n      |-> log :\n      |"
        text        = text_1 + text_2
        print_format = "      |     "                        
                
        # [B] 함수 본문 __________________________________________________________________________________________________________
        import cv2
        from pyxelate import Pyx, Pal  
        
        # 1. 이미지 경계 탐색
        img_bgr             = img.copy()   
        img_bitwise_not_bgr = cv2.bitwise_not(img_bgr) 
        img_bitwise_not_bgr2gray = cv2.cvtColor(img_bitwise_not_bgr, cv2.COLOR_BGR2GRAY)
        
        # 2. 이미지 경계 쓰레시 홀드 찾아서 검정색 outline 그리기
        ret, img_binary = cv2.threshold(img_bitwise_not_bgr2gray, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,255,cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        img_contour = cv2.drawContours(img_bgr, contours, -1, (0, 0, 0), 2)
        
        # 3. 도트화(pixelation 하는 부분)
        downsample_by = 4  # new image will be 1/14th of the original in size
        palette = 8  # find 7 colors

        # 3_1. Instantiate Pyx transformer
        pyx = Pyx(factor=downsample_by, palette=palette)

        # 3_2. fit an image, allow Pyxelate to learn the color palette
        pyx.fit(img_bgr)
        
        th = img_bgr

        # 3_3. transform image to pixel art using the learned color palette
        new_image = pyx.transform(img_bgr)
        
        return new_image, text

    
         
    
    

     
    
