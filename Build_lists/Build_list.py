import numpy as np
import os
import pandas as pd


class Build():
    def __init__(self,file_list):
        self.file_list = file_list
        self.data = pd.read_excel(file_list, dtype = {'Patient_ID': str})

    def __build__(self,index_list):
        c = self.data.iloc[index_list]

        batch_list = np.asarray(c['batch'])
        patient_id_list = np.asarray(c['patient_id'])
        slice_index_list = np.asarray(c['slice_index'])
        img_file_list = np.asarray(c['img_file'])
        seg_file_list = np.asarray(c['seg_file'])
        
        return batch_list, patient_id_list, slice_index_list, img_file_list, seg_file_list