## main - cp vton 코드에 있는 test.py의 골자를 따라감

# [A] MODE
mode = "live"

# [B] PIEPLINE - COLAB CODE
from step.pixelate_new import *
from step.segmentation import *
from step.keypoint import *
from step.model import *

pipeline_pixelate     = {
                         "step"    : Pixelate
                        ,"method"  : Pixelate.method1
                        ,"mode"    : mode
                        ,"load_dir": "./data/test/cloth-raw/"
                        ,"save_dir": "./data/test/cloth/"
                        }

pipeline_segmentation = {
                         "step"    : Segmentation
                        ,"method"  : Segmentation.method1
                        ,"mode"    : mode
                        ,"load_dir": "./data/test/cloth/"
                        ,"save_dir": "./data/test/cloth-mask/"
                        }

# 이거 path 찾아라
pipeline_keypoint     = {
                         "method": Keypoint.method1
                        ,"mode": mode
                        ,"load_dir": "a"
                        ,"save_dir": "b"
                        }

pipeline_tryon        = {
                         "method": Tryon.method1
                         ,"mode": mode
                         ,"load_dir": "a"
                         ,"save_dir": "b"
                        }


pipeline = {"pixelate": pipeline_pixelate
           ,"segmentation": pipeline_segmentation
           ,"keypoint": pipeline_keypoint
           ,"tryon": pipeline_tryon}


pipeline = {"pixelate": pipeline_pixelate
           ,"segmentation": pipeline_segmentation}



# pipeline = {"segmentation": pipeline_segmentation}

# [C] FUNCTION FOR FITTING
def active_pipeline(step,pipeline):
    kwargs = pipeline[step].copy()
    kwargs.pop("step")
    return pipeline[step]['step'].fit(**kwargs)

def fit(pipeline,mode=None):
    step_num = 0
    for step in list(pipeline.keys()):
        step_num += 1
        mode      = pipeline[step]['mode']
        print("\n** PIPELINE {step_num} (mode = {mode}) ___________________________________________________________________________________________".format(step_num=step_num,mode=mode))
        active_pipeline(step,pipeline)
        print("\n")
        
        
        
# [D] FOR RUNNING        
fit(pipeline)    