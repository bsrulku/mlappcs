import pickle
import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

def prediction(data):
    data = (pd.DataFrame(data, index=[0]))
    print(data.columns)
    sc = pickle.load(open('models/StandardScaler' + '.pkl', 'rb'))
    xgb = pickle.load(open('models/classification_model.pkl', 'rb'))

    for col in ['education', 'self_employed']:
        le = pickle.load(open('models/encoding_' + col + '.pkl', 'rb'))
        data[col] = le.transform(data[col])

    y_pred = xgb.predict(data)
    le_y = pickle.load(open('models/encoding_y.pkl', 'rb'))
    output = le_y.inverse_transform(y_pred)
    data['output'] = str(output)

    file = open('past_loans.csv', "r")
    file_content = file.read()
    file.close()

    if file_content == "":
        data.to_csv('past_loans.csv',index=False)
    else:
        logs = pd.read_csv('past_loans.csv')
        logs = pd.concat([data,logs],ignore_index=True)
        logs.to_csv('past_loans.csv',index=False)

    return output


if __name__ == "__main__":
    data = {
        'loan_id': 1700,
        'no_of_dependents': 5,
        'education': ' Not Graduate',
        'self_employed': ' Yes',
        'income_annum': 7700000,
        'loan_amount': 25800000,
        'loan_term': 18,
        'cibil_score': 578,
        'residential_assets_value': 5000000,
        'commercial_assets_value': 7700000,
        'luxury_assets_value': 27200000,
        'bank_asset_value': 10600000}
    print(prediction(data))

