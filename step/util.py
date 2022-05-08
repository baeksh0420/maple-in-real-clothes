# 함수별로 필요한 패키지 중복 많이되면 같이 넣고, 아니면 분리하는 것도 좋을듯 또는 개별 함수에 import문 넣던지

from tensorboardX import SummaryWriter
import torch
from PIL import Image
import os
import cv2
from matplotlib import pyplot as plt 

# ------ PJ01 util 신규 함수
def read_list(load_dir, file_type = "jpg"):
    """
    경로내 전체 파일 리스트 추출
    """
    path      = "./"
    file_name = os.listdir(load_dir)
    load_list = [load_dir + "/" + f for f in file_name if f.endswith("."+file_type)]
    
    if len(load_list) == 0:
        raise Exception("ERROR! - no image file in your directory, '{load_dir}''".format("load_dir"))

    return load_list

def save_path(save_dir, load_dir, load_path, file_type = "jpg"):
    """
    하나의 이미지를 저장할 경로
    """
    if not os.path.isdir(save_dir):
        print(print_format+"Make a new directory : {}".format(save_dir))
        os.mkdir(save_dir)
        exit(1)

    save_path = load_path.replace(load_dir, save_dir)  
        
    return save_path

def read_img(load_path, load_pkg , load_mode = cv2.IMREAD_COLOR ,file_type = "jpg"):
    """
    하나의 이미지를 읽음
    """
    if not os.path.isfile(load_path):
        raise Exception("ERROR! - no image file, '{load_path}' in your directory".format(load_path=load_path))
#     return cv2.imread(load_path,load_mode)
    if load_pkg == "cv2":
        return cv2.imread(load_path,load_mode)
    elif load_pkg == "io":
        from skimage import io
        return io.imread(load_path,load_mode)

def write_img(th, save_path, mode):
    """
    하나의 이미지를 저장
    """
    print_format = "      |     "  
    
    if "live" in mode:
        cv2.imwrite(save_path, th)
    if "show" in mode:
        plt.imshow(th,'gray')
        plt.show()  
        
        
# ------ cp-vton util 함수
def tensor_for_board(img_tensor):
    # map into [0,1]
    tensor = (img_tensor.clone()+1) * 0.5
    tensor.cpu().clamp(0,1)

    if tensor.size(1) == 1:
        tensor = tensor.repeat(1,3,1,1)

    return tensor

def tensor_list_for_board(img_tensors_list):
    grid_h = len(img_tensors_list)
    grid_w = max(len(img_tensors)  for img_tensors in img_tensors_list)
    
    batch_size, channel, height, width = tensor_for_board(img_tensors_list[0][0]).size()
    canvas_h = grid_h * height
    canvas_w = grid_w * width
    canvas = torch.FloatTensor(batch_size, channel, canvas_h, canvas_w).fill_(0.5)
    for i, img_tensors in enumerate(img_tensors_list):
        for j, img_tensor in enumerate(img_tensors):
            offset_h = i * height
            offset_w = j * width
            tensor = tensor_for_board(img_tensor)
            canvas[:, :, offset_h : offset_h + height, offset_w : offset_w + width].copy_(tensor)

    return canvas

def board_add_image(board, tag_name, img_tensor, step_count):
    tensor = tensor_for_board(img_tensor)

    for i, img in enumerate(tensor):
        board.add_image('%s/%03d' % (tag_name, i), img, step_count)


def board_add_images(board, tag_name, img_tensors_list, step_count):
    tensor = tensor_list_for_board(img_tensors_list)

    for i, img in enumerate(tensor):
        board.add_image('%s/%03d' % (tag_name, i), img, step_count)

def save_images(img_tensors, img_names, save_dir):
    for img_tensor, img_name in zip(img_tensors, img_names):
        tensor = (img_tensor.clone()+1)*0.5 * 255
        tensor = tensor.cpu().clamp(0,255)

        array = tensor.numpy().astype('uint8')
        if array.shape[0] == 1:
            array = array.squeeze(0)
        elif array.shape[0] == 3:
            array = array.swapaxes(0, 1).swapaxes(1, 2)
            
        Image.fromarray(array).save(os.path.join(save_dir, img_name))

