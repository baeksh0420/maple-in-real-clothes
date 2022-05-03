# !pip install opencv-python
# !pip install matplotlib
# !pip install tqdm
# !pip install git
# !pip install git+https://github.com/sedthh/pyxelate.git

# Open cv library

class Pixelate:
    def plot_(subplots=[], save_as=None, fig_h=9):
        import cv2
        from os import path
        import os
        import numpy as np
        
        # matplotlib for displaying the images 
        from matplotlib import pyplot as plt
        
        from tqdm import tqdm
        from skimage import io
        
        from pyxelate import Pyx, Pal
        """Plotting helper function"""
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
        
    def pix1(img_path, mode=None, is_save=None, save_path=None):
        # Open cv library
        import cv2
        from os import path
        import numpy as np
        # matplotlib for displaying the images 
        from matplotlib import pyplot as plt
        from skimage import io
        from pyxelate import Pyx, Pal

        # load image with 'skimage.io.imread()'
        # 원본 이미지 불러 오기
        image = io.imread(img_path)  
        # 이미지 복사
        img_bgr = image.copy()
        # 이미지 경계 탐색
        img_bitwise_not_bgr = cv2.bitwise_not(img_bgr)
        img_bitwise_not_bgr2gray = cv2.cvtColor(img_bitwise_not_bgr, cv2.COLOR_BGR2GRAY)
        # 이미지 경계 쓰레시 홀드 찾아서 검정색 outline 그리기
        ret, img_binary = cv2.threshold(img_bitwise_not_bgr2gray, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,255,cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        img_contour = cv2.drawContours(img_bgr, contours, -1, (0, 0, 0), 2)
        
        # 도트화(pixelation 하는 부분)
        downsample_by = 4  # new image will be 1/14th of the original in size
        palette = 8  # find 7 colors

        # 1) Instantiate Pyx transformer
        pyx = Pyx(factor=downsample_by, palette=palette)

        # 2) fit an image, allow Pyxelate to learn the color palette
        pyx.fit(img_bgr)
        
        th = img_bgr

        # 3) transform image to pixel art using the learned color palette
        new_image = pyx.transform(img_bgr)
        
        # save new image with 'skimage.io.imsave()'
        if mode=="show":
            Pixelate.plot_([image, new_image], save_as=None)
        if is_save=="save":
            cv2.imwrite(save_path, new_image)
        
      
