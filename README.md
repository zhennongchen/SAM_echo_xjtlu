# Tailor segment-anything-model (SAM) for echo segmentation
**Author: Zhennong Chen, PhD**<br />

## Important Notice

- first and the most important: <br />
    - step 1: make sure you can run the code successfully in your own laptop <br />
    - step 2: read and read again the code. Understand what each part does. Find out which part you need to change to fit our project (echo competition) <br />
    - do not jump to change the code right away without understanding it. you will get lost easily. <br />

## Guideline to use the code
1. the code needs to be run inside specific environment. please refer to **docker** folder for details.<br />
 - if you fail to install a docker, you can try to manually install the packages in ```docker/docker_SAM/dockerfile``` and ```docker/docker_SAM/requirements.txt``` and  into your conda environment. <br />
 - there is a guideline included. <br />

2. train model: ```step1_train_new.ipynb``` <br />

3. predict on new cases: ```step2_predict_new.ipynb``` <br />

4. make sure you change all paths - data path, code path (including the path saved in patient_list.xlsx) - to your own paths before running the code. <br />

5. make sure you set the parameters (marked with ###!!) properly before running the code. <br />

6. the code includes extensive augmentations, use based on what you need! <br />

7. pay attention to your image dimension!
    - here I center-crop all images to 128x128 (so you need to understand, there are two steps: find a meaningful center and crop; read ```data_loader/generator.py```), and turn the dimension back to each individual case's original size when saving the prediction. <br />
    - maybe you need a different uniform size
