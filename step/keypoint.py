class Keypoint:        
    def method1(load_dir,save_dir,mode="none"):
        
        """
        작업 히스토리 (역순으로 작성)
        - 2022/05/08 (olive46) - 함수 기본 골자 세팅    
        """
        
       # [A] 방식 설명 (= 각 파이프라인 스텝별 방법을 구분할 수 있는 설명 또는 버전)

        step        = "Keypoint"                   
        method_name = Keypoint.method1.__name__    
        method_str  = method_name.rstrip('0123456789') 
        method_num  = method_name[len(method_str):]    
        version     = "0.0"                            
        description = "~~ 에서 제공하는 툴을 사용한 수동 감지법"              
        print("\n   [STEP : {step}, METHOD : {method_num}, VERSION : {version}]  : {description}\n   ".format(step=step
                                                                                                      ,method_num=method_num
                                                                                                      ,version=version
                                                                                                      ,description =description))
        print("      |-> log :\n      |")              
        print_format = "      |     "                        
        
        # [B] 함수 본문
        
    
    def method2(load_dir,save_dir,mode="none"):
        
        """
        작업 히스토리 (역순으로 작성)
        - 2022/05/08 (olive46) - 함수 기본 골자 세팅    
        """
        
       # [A] 방식 설명 (= 각 파이프라인 스텝별 방법을 구분할 수 있는 설명 또는 버전)

        step        = "Keypoint"                   
        method_name = Keypoint.method2.__name__    
        method_str  = method_name.rstrip('0123456789') 
        method_num  = method_name[len(method_str):]    
        version     = "0.0"                            
        description = "coco18을 사용한 자동 감지법"              
        print("\n   [STEP : {step}, METHOD : {method_num}, VERSION : {version}]  : {description}\n   ".format(step=step
                                                                                                      ,method_num=method_num
                                                                                                      ,version=version
                                                                                                      ,description =description))
        print("      |-> log :\n      |")              
        print_format = "      |     "                        
        
        # [B] 함수 본문                