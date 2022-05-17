#coding=utf-8
# import torch
# import torch.nn as nn
# from torch.nn import init
# from torchvision import models
# import os

# import numpy as np
import step.util as util        
from step.model import *        
import os

# 포맷팅 후 지우기
class Tryon:
#     def fit(method, mode, load_dir, save_dir, print_format = "      |     "):
      def fit(method, mode, name, stage, workers, datamode, data_list, checkpoint, print_format = "      |     "):
#         ! python test.py --name name --stage stage --workers workers --datamode datamode --data_list data_list --checkpoint checkpoints
      

        os.system("python test.py --name gmm --stage GMM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/gmm_final.pth")    
            
        if mode == "test":
            print(print_format+"test mode, no write")        
            
            
            
#     def method1(img, mode="none"):
        
#         """
#         작업 히스토리 (역순으로 작성)
#         - 2022/05/08 (olive46) - 함수 기본 골자 세팅    
#         - 2022/05/01 (olive46) - load_dir내 모든 이미지에 적용하도록 for문 포함
#         """
        
#        # [A] 방식 설명 (= 각 파이프라인 스텝별 방법을 구분할 수 있는 설명 또는 버전)

#         step        = "Tryon"                   
#         method_name = Tryon.method1.__name__    
#         method_str  = method_name.rstrip('0123456789') 
#         method_num  = method_name[len(method_str):]    
#         version     = "0.0"                            
#         description = "cp-vton 논문의 pretrained checkpoint 사용한 방법"              
#         text_1      = "\n   [STEP : {step}, METHOD : {method_num}, VERSION : {version}]  : {description}\n   ".format(step=step
#                                                                                                       ,method_num=method_num
#                                                                                                       ,version=version
#                                                                                                       ,description =description)
#         text_2      = "\n      |-> log :\n      |"
#         text        = text_1 + text_2
#         print_format = "      |     "                        
        
#         # [B] 함수 본문
 