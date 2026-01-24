import numpy as np
import os
import pandas as pd


class Build():
    def __init__(self,file_list):
        self.file_list = file_list
        self.data = pd.read_excel(file_list, dtype = {'Patient_ID': str})

    def __build__(self,index_list):
        c = self.data.iloc[index_list]

        batch_list = np.asarray(c['batch']) if hasattr(c, 'batch') else np.zeros(len(c))
        patient_id_list = np.asarray(c['patient_id']) if hasattr(c, 'patient_id') else np.asarray(c['Patient_ID'])
        # slice_index_list = np.asarray(c['slice_index'])
        img_file_list = np.asarray(c['img_file']) if hasattr(c, 'img_file') else np.asarray(c['image_file'])
        seg_file_list = np.asarray(c['seg_file']) if hasattr(c, 'seg_file') else np.asarray(c['mask_file'])
        
        return batch_list, patient_id_list,  img_file_list, seg_file_list