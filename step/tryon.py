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

class Tryon:
      def fit(method, mode, name, stage, workers, datamode, datalist, checkpoint, print_format = "      |     "):

        print_method_description = 0
        
        # ! python test.py --name gmm --stage GMM --workers 1 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/gmm_final.pth
        # ! python test.py --name tom --stage TOM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/tom_final.pth
        for i in range(len(name)):
            text, command_script = method(name[i], stage[i], workers[i], datamode[i], datalist[i], checkpoint[i], mode="none")
            os.system(command_script) ; print("** RUN COMMAND SCRIPT - "+ command_script)
            
            print_method_description += 1
            if print_method_description == 1:
                print(text)

        
        if mode == "test":
            print(print_format+"test mode, no write")        
            
            
            
      def method1(name, stage, workers, datamode, data_list, checkpoint, mode="none"):
        
        """
        작업 히스토리 (역순으로 작성)
        - 2022/05/08 (olive46) - 함수 기본 골자 세팅    
        - 2022/05/01 (olive46) - load_dir내 모든 이미지에 적용하도록 for문 포함
        """
        
        # [A] 방식 설명 (= 각 파이프라인 스텝별 방법을 구분할 수 있는 설명 또는 버전)

        step        = "Tryon"                   
        method_name = Tryon.method1.__name__    
        method_str  = method_name.rstrip('0123456789') 
        method_num  = method_name[len(method_str):]    
        version     = "0.0"                            
        description = "cp-vton 논문의 pretrained checkpoint 사용한 방법"              
        text_1      = "\n   [STEP : {step}, METHOD : {method_num}, VERSION : {version}]  : {description}\n   ".format(step=step
                                                                                                                     ,method_num=method_num
                                                                                                                     ,version=version
                                                                                                                     ,description =description)
        text_2      = "\n      |-> log :\n      |"
        text        = text_1 + text_2
        print_format = "      |     "                        
        
        command_script = "python test.py --name {name} --stage {stage} --workers {workers} --datamode {datamode} --data_list {data_list} --checkpoint {checkpoints}".format(method = method
        , name = name
        , stage = stage
        , workers = workers
        , datamode = datamode
        , datalist = datalist
        , checkpoint = checkpoint)    
    
        
        # [B] 함수 본문
        return text, command_script
 