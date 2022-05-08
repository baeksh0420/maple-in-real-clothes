## main - cp vton 코드에 있는 test.py의 골자를 따라감

# step 01 - pixelate
# step 02 - segmentation
# step 03 - keypoint
# step 04 - model (cp_vton)

from step.pixelate import *
from step.segmentation import *
from step.keypoint import *
from step.model import *
    
mode = "test"

pipeline_pixelate     = {"method": Pixelate.method1
                        ,"load_dir": "./data/test/cloth-raw/"
                        ,"save_dir": "./data/test/cloth/"
                        ,"mode": mode}

pipeline_segmentation = {"method": Segmentation.method1
                        ,"load_dir": "./data/test/cloth/"
                        ,"save_dir": "./data/test/cloth-mask/"
                        ,"mode": mode}

# 이거 path 찾아라
pipeline_keypoint     = {"method": Keypoint.method1
                        ,"load_dir": "a"
                        ,"save_dir": "b"
                        ,"mode": mode}

pipeline_tryon        = {"method": Tryon.method1
                         ,"load_dir": "a"
                         ,"save_dir": "b"
                         ,"mode": mode}


pipeline = {"pixelate": pipeline_pixelate
           ,"segmentation": pipeline_segmentation
           ,"keypoint": pipeline_keypoint
           ,"tryon": pipeline_tryon}


def active_pipeline(step,pipeline):
    kwargs = pipeline[step].copy()
    kwargs.pop("method")
    return pipeline[step]['method'](**kwargs)

def fit(pipeline,mode=None):
    step_num = 0
    for step in list(pipeline.keys()):
        step_num += 1
        mode      = pipeline[step]['mode']
        print("\n** PIPELINE {step_num} (mode = {mode}) ___________________________________________________________________________________________".format(step_num=step_num,mode=mode))
        active_pipeline(step,pipeline)
        print("\n")
        
fit(pipeline)    