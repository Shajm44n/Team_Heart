import joblib


def preprocess(values):
    values[1] = [int(1) if values[1] == 'Male' else int(2)][0]
    values[6] = [int(1) if values[6]== '1: normal' else int(2) if values[6] =='2: above normal' else int(3)][0]
    values[7]= [int(1) if values[7] == '1: normal' else int(2) if values[7] == '2: above normal' else int(3)][0]
    values[8] = [int(0) if values[8] == 'No' else int(1)][0]
    values[9] = [int(0) if values[9] == 'No' else int(1)][0]
    values[10] = [int(0) if values[10] == 'No' else int(1)][0]
    # print("preprocess completed")
    # print(values)
    pred=predict_h(values)
    # print(pred)
    return pred

def predict_h(listh):
    loaded_rf = joblib.load("svc_heart.joblib")
    y_pred = loaded_rf.predict([listh])
    print(y_pred)
    return y_pred