Visit http://localhost:5000/ to use the service.


## Usage
-Make a POST request to /predict with a JSON object containing loan application data. Ensure that the data includes 11 features.
-The application will respond with a prediction of loan eligibility or an error message.
-To retrieve a list of past loan records, make a GET request to /list.o clean the past loan records, make a GET request to /clean.
##API Endpoints
-POST /predict: Predicts loan eligibility based on user-provided data.
-GET /list: Retrieves a list of past loan records.
-GET /clean: Deletes all past loan records.
## Configuration
-Customize settings in app.py.
JSON Example
{
        "no_of_dependents": 45654,
        "education": " Not Graduate",
        "self_employed": " Yes",
        "income_annum": 45646456,
        "loan_amount": 23424,
        "loan_term": 255,
        "cibil_score": 3000,
        "residential_assets_value": 5000000,
        "commercial_assets_value": 7700000,
        "luxury_assets_value": 27200000,
        "bank_asset_value": 10600000 }

## You can find the relevant notebooks for EDA and model generation in the notebooks folder
--BusraUlkuKup (busraulku14@gmail.com)
