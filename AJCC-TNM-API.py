import pandas as pd
import requests
from dotenv import load_dotenv
import numpy as np
import os
import xml.etree.ElementTree as ET

# Documentation for this program
#
# Data format wrangling: https://stackoverflow.com/questions/44802160/convert-json-api-response-to-pandas-dataframe
# API documentation: https://ajcc.3scale.net/docs/dev-testing
# API key handling: https://blog.gitguardian.com/how-to-handle-secrets-in-python/
# API key in request: https://stackoverflow.com/questions/53075939/calling-rest-api-with-an-api-key-using-the-requests-package-in-python

load_dotenv()
api_key = os.getenv("API_KEY")

uri_header = "https://ajcc-apicast-v2.easydita.com/sandbox/V2/ajcc-api/diseases/MAG-PRO/content/definitions/"
uri_list = ["cT", "pT", "ycT", "ypT",
            "cN", "pN", "ycN", "ypN",
            "cM", "pM", "ycM", "ypM"]
headers = {'user_key': api_key}

frames = []

for tnm_type in uri_list:

    r = requests.get(uri_header + tnm_type, headers=headers)
    data = r.text

    xpath = "//AJCCcriteria | //AJCCcategory/validvalue | //critdates/revised | //vrmlist/vrm"

    df_raw = pd.read_xml(data, xpath=xpath).drop(["class", "valid"], axis=1)
    df_raw.loc[::2, ["golive", "modified"]] = df_raw.loc[0, ["golive", "modified"]].to_numpy()
    df_raw.loc[::2, ["version"]] = df_raw.loc[1, ["version"]].to_numpy()
    df_raw = df_raw.drop([0, 1]).reset_index().drop("index", axis=1)
    df_grouped = df_raw.groupby(np.arange(len(df_raw)) // 2).sum()
    df_grouped["Organ"] = ['Prostate'] * len(df_grouped)
    frames.append(df_grouped)

result = pd.concat(frames)
result.to_csv("prostate.csv")
