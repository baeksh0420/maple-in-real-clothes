import step.util as util        
import cv2

class Segmentation:
    def fit(method, mode, load_dir, save_dir, print_format = "      |     "):
        
        file_type = "jpg"
        load_mode = 0
        load_list = util.read_list(load_dir, file_type)
        
        print_method_description = 0

        
        for load_path in load_list:
            img             = util.read_img(load_path, "cv2", load_mode)
            img             = cv2.resize(img, dsize=(192,256), interpolation=cv2.INTER_LINEAR)
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

          
            
    def method2(img, mode="none"):
        
        """
        작업 히스토리 (역순으로 작성)
        - 2022/06/06 (olive46) - 보정 작업
        """
        
       # [A] 방식 설명 (= 각 파이프라인 스텝별 방법을 구분할 수 있는 설명 또는 버전)

        step        = "Segmentation"                   
        method_name = Segmentation.method2.__name__    
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
        
#         img       = cv2.medianBlur(img,5) # -- 노이즈 제거
#         ret, th   = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 
        
#         # --- new part
#         #components of the skin
#         stats = regionprops(img,'centroid');
#         topCentroid = stats(1).Centroid;
#         rightCentroid = stats(1).Centroid;
#         leftCentroid = stats(1).Centroid;
#         for x in range(1,len(stats),1):
#             centroid = stats(x).Centroid;
#             if topCentroid(2)>centroid(2):
#                 topCentroid = centroid;
#             elif centroid(1)<leftCentroid(1):
#                 leftCentroid = centroid;
#             elif centroid(1)>rightCentroid(1):
#                 rightCentroid = centroid;
#             end
#         end

#         #first seed - the average of the most left and right centroids.
#         centralSeed = int16((rightCentroid+leftCentroid)/2);

#         #second seed - a pixel which is right below the face centroid.
#         faceSeed = int(topCentroid)
#         faceSeed(2) = faceSeed(2)+40; 

#         #stage 3: std filter
#         varIm = stdfilt(rgb2gray(im));

#         #stage 4 - region growing on varIm  using faceSeed and centralSeed
#         res1=regiongrowing(varIm,centralSeed(2),centralSeed(1),8);
#         res2=regiongrowing(varIm,faceSeed(2),faceSeed(1),8);
#         res = res1|res2;

#         #noise reduction
#         res = imclose(res,strel('disk',3));
#         res = imopen(res,strel('disk',2));
        # --- check part
        #         print(type(sure_bg))
        from matplotlib import pyplot as plt 
        plt.imshow(res,'gray')
        plt.show()  
        return ret, th, text
