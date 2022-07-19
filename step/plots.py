# 정리해야함...

def compare_plot(subplots=[], save_as=None, fig_h=9):
    """
    Plotting helper function
    """
    import cv2
    from os import path
    import os
    import numpy as np
    
    # matplotlib for displaying the images 
    from matplotlib import pyplot as plt
    
    from tqdm import tqdm
    from skimage import io
    
    from pyxelate import Pyx, Pal
    
    fig, ax = plt.subplots(int(np.ceil(len(subplots) / 3)), 
                           min(3, len(subplots)), 
                           figsize=(18, fig_h))
    if len(subplots) == 1:
        ax = [ax]
    else:
        ax = ax.ravel()
    for i, subplot in enumerate(subplots):
        if isinstance(subplot, dict):
            ax[i].set_title(subplot["title"])
            ax[i].imshow(subplot["image"])
        else:
            ax[i].imshow(subplot)
    fig.tight_layout()
    if save_as is not None and SAVE_IMAGES:
        # Save image as an example in README.md
        plt.savefig(path.join("examples/", save_as), transparent=True)
    plt.show()
    
def img_show(ori_img, result_img, show_mode = "result"):
    """
    하나의 이미지를 출력
    """
    if show_mode == "result":
        plt.imshow(result_img,'gray')
        plt.show()
    if show_mode == "compare"
        plot_([ori_img, result_img], save_as=None)
