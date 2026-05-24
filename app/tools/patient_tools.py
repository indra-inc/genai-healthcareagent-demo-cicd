import json

import pandas as pd
from langchain.tools import tool

df_patient = pd.read_csv("data/patient_data.csv")


@tool
def get_patient_record(patient_id: str) -> str:
    """
    Retrieve complete patient medical record.
    """

    row = df_patient[df_patient["patient_id"].str.lower() == patient_id.strip().lower()]

    if row.empty:
        return json.dumps({"status": "not_found", "patient_id": patient_id})

    patient_data = row.iloc[0].to_dict()

    return json.dumps(
        {"status": "found", "patient_id": patient_id, "patient_data": patient_data},
        indent=2,
        default=str,
    )
