import requests
import json

rev_url = "http://staging.ecomexpress.in/apiv2/manifest_awb_rev_v2/"
awb_url = 'http://staging.ecomexpress.in/apiv2/fetch_awb/'
username = "ecomexpress"
pswd = "Ke$3c@4oT5m6h#$"


awb_data = {'username': username,
        'password': pswd,
        'type': 'REV',
        'count': 1,
        }


r = requests.post(awb_url, awb_data)
ecom_express_data = r.json()

awb_number = ecom_express_data["awb"][0]

details = {"ECOMEXPRESS-OBJECTS": {
    "SHIPMENT": {
        "AWB_NUMBER": awb_number,
        "ORDER_NUMBER": "500765301-001",
        "PRODUCT": "rev",
        "REVPICKUP_NAME": "Pia Bhaa",
        "REVPICKUP_ADDRESS1": "Test Address 1",
        "REVPICKUP_ADDRESS2": "Change Address 2",
        "REVPICKUP_ADDRESS3": "Change Address 3",
        "REVPICKUP_CITY": "Delhi",
        "REVPICKUP_PINCODE": "111111",
        "REVPICKUP_STATE": "DL",
        "REVPICKUP_MOBILE": "1234567891",
        "REVPICKUP_TELEPHONE": "0123456789",
        "PIECES": 1,
        "COLLECTABLE_VALUE": "0.0",
        "DECLARED_VALUE": "500.00",
        "ACTUAL_WEIGHT": 0.87,
        "VOLUMETRIC_WEIGHT": 0.87,
        "LENGTH": 320,
        "BREADTH": 200,
        "HEIGHT": 120,
        "VENDOR_ID": "",
        "DROP_NAME": "Drop Test Name",
        "DROP_ADDRESS_LINE1": "Drop Change Address 1",
        "DROP_ADDRESS_LINE2": "Drop Change Address 2,",
        "DROP_PINCODE": "111111",
        "DROP_MOBILE": "9999999999",
        "ITEM_DESCRIPTION": "XYZ",
        "DROP_PHONE": "0123456789",
        "EXTRA_INFORMATION": "test info",
        "DG_SHIPMENT ": "False",
        "ADDITIONAL_INFORMATION": {
            "SELLER_TIN": "",
            "INVOICE_NUMBER": "INV001230",
            "INVOICE_DATE": "12-04-2017",
            "ESUGAM_NUMBER": "",
            "ITEM_CATEGORY": "",
            "ITEM_VALUE": "0",
            "PACKING_TYPE": "",
            "PICKUP_TYPE": "",
            "RETURN_TYPE": "",
            "PICKUP_LOCATION_CODE": "WH",
            "SELLER_GSTIN": "GSTINB0012345",
            "GST_HSN": "123579D",
            "GST_ERN": "",
            "GST_TAX_NAME": "DELHI GST",
            "GST_TAX_BASE": 450.0,
            "GST_TAX_RATE_CGSTN": 0.0,
            "GST_TAX_RATE_SGSTN": 0.0,
            "GST_TAX_RATE_IGSTN": 5.0,
            "GST_TAX_TOTAL": 50.00,
            "GST_TAX_CGSTN": 0,
            "GST_TAX_SGSTN": 0,
            "GST_TAX_IGSTN": 50.00,
            "DISCOUNT": 0
            }
        }
        }
        }


rev_data = {'username': username,
        'password': pswd,
        'json_input': json.dumps(details),
        }


r = requests.post(rev_url, rev_data)
ecom_express_data = r.json()

print json.dumps(ecom_express_data)
