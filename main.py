import numpy as np
from data import test_data_arr_final
from tensorflow import keras
import openpyxl as xl
workbook = xl.load_workbook('bc_data.xlsx')
sheet = workbook['breast-cancer-wisconsin (1)']
model = keras.models.load_model('cancer_model.h5')

model.summary()
st_row_predict = 500
prediction = model.predict(test_data_arr_final)
for row in np.squeeze(prediction):
    print(np.argmax(row))

    '''for saving the prediction'''
    prediction_position = sheet.cell(st_row_predict, 12)
    prediction_position.value =np.argmax(row)
    st_row_predict+=1
workbook.save('bc_data.xlsx')
print('prediction stored')
