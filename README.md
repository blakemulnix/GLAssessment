# GL Assessment

## How to setup and run the application (for unix systems)

1. Install Python 3 on your system 
2. Clone this repository
3. In the root of the repository, run the following commands:
   1. Create a virtual environment \
   `python3 -m venv venv`
   2. Activate the virtual environment \
   `source venv/bin/activate`
   3. Install the required packages \
   `pip install -r requirements.txt`
   4. Run the application \
   `python3 main.py` 

## How to use the application
- Send your POST request to `localhost:5000/invoices`
- Navigate to the URL in the response
- Enter a payment amount and hit the "Make Payment" button
- Once the you have paid the full amount (or more than the full amount), you will see the "Payment Complete" page
- To reset the stored data, overwrite the `data/invoice_data.json` with `{"invoices": {}}`
