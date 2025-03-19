# Dressing characters in real-world clothes (MapleStory ver)
*Do you have a favorite outfit? And do you have a favorite game character?*<br>
*Imagine how amazing it would be if your character were dressed in your favorite clothes!*<br>
<br>
This is a model that **applies real-world clothing to virtual characters**. <br>
With just a few preliminary settings, game characters can wear your own clothes. <br>
This model utilizes CP-VTON.
<br>
<br>
Referenced from [minar09/cp-vton-plus](https://github.com/minar09/cp-vton-plus) 🤗
<br>
<br>
## Run
```
!pip install tensorboardX
```
```
%cd /content/drive/MyDrive/AI_project/5. CP-VTON_maple/CP-VTON_sohyeon/CP-VTON_customdata_fixver
```
TOM
```
! python test.py --name gmm --stage GMM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/gmm/gmm_final.pth
```
GMM
```
! python test.py --name tom --stage TOM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/tom/tom_final.pth
```
<br>

## Results
```data/test/try_on```
<div style="width:80%; margin:0 auto;">
<img src = "https://github.com/user-attachments/assets/92e4d200-7b92-4246-a77a-7432ca184fad" width="13%">
<img src = "https://user-images.githubusercontent.com/64413742/183881567-d642b629-69cc-4673-a5d8-300f2fc1f351.png" width="15%">
<img src = "https://user-images.githubusercontent.com/64413742/183881615-da1ed498-df01-4ead-92fb-cffde8d009e2.png" width="15%">
</div>
<br>
<br>

## Model
### Data Preparation
```data/test/image``` : character image<br>
```data/test/cloth``` : real-world clothes *(we add black outline along the edges to give it a dotted appearance.)* <br>

### Character's body boundaries
```data/test/image-parse``` : character's boundaries<br>
```data/test/pose``` : keypoints<br>

### Generating clothes for character's body
CP-VTON
```python
def train_tom(opt, train_loader, model, board):
    model.cuda()
    model.train()
    
    # Criterion
    criterionL1 = nn.L1Loss()
    criterionVGG = VGGLoss()
    criterionMask = nn.L1Loss()
    
    # Optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=opt.lr, betas=(0.5, 0.999))
    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda = lambda step: 1.0 -
            max(0, step - opt.keep_step) / float(opt.decay_step + 1))
    
    for step in range(opt.keep_step + opt.decay_step):
        iter_start_time = time.time()
        inputs = train_loader.next_batch()
            
        im = inputs['image'].cuda()
        im_pose = inputs['pose_image']
        im_h = inputs['head']
        shape = inputs['shape']

        agnostic = inputs['agnostic'].cuda()
        c = inputs['cloth'].cuda()
        cm = inputs['cloth_mask'].cuda()
        
        # Model Forward
        outputs = model(torch.cat([agnostic, c],1))
        p_rendered, m_composite = torch.split(outputs, 3,1)
        p_rendered = F.tanh(p_rendered)
        m_composite = F.sigmoid(m_composite)
        
        # Mask Composition
        p_tryon = c * m_composite+ p_rendered * (1 - m_composite)
        
        visuals = [[im_h, shape, im_pose], 
                   [c, cm*2-1, m_composite*2-1], 
                   [p_rendered, p_tryon, im]]
        
        # Loss Functions
        loss_l1 = criterionL1(p_tryon, im) # L1 Loss
        loss_vgg = criterionVGG(p_tryon, im) # Perceptual (VGG19) Loss
        loss_mask = criterionMask(m_composite, cm) # Cloth Mask Loss
        loss = loss_l1 + loss_vgg + loss_mask
        
        # Model Backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```
<br>
<br>

## Contributors
[Shyun Im](https://github.com/shyun46), [Joshua Park](https://github.com/Hinterhalter), [Sohyeon Baek](https://github.com/baeksh0420)
<br>
<br>
<br>

## If improvements are made...
- body 대비 옷의 boundary 정보를 더해 옷의 형태를 유지해 warp 한다
- 백그라운드 노이즈를 제거해 화질 개선
