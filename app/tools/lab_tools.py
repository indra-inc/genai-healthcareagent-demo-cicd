import json

import pandas as pd
from langchain.tools import tool

df_patient = pd.read_csv("data/patient_data.csv")


@tool
def analyze_lab_values(patient_id: str) -> str:
    """
    Analyze patient laboratory values.
    """

    row = df_patient[df_patient["patient_id"].str.lower() == patient_id.strip().lower()]

    if row.empty:
        return json.dumps({"status": "not_found"})

    patient = row.iloc[0].to_dict()

    lab_test = str(patient["lab_test"])
    lab_value = float(patient["lab_value"])

    risk_signals = []

    if lab_test == "HbA1c":
        if lab_value >= 9:
            risk_signals.append(f"Very high HbA1c: {lab_value}%")
        elif lab_value >= 7:
            risk_signals.append(f"Elevated HbA1c: {lab_value}%")
        else:
            risk_signals.append(f"Controlled HbA1c: {lab_value}%")

    return json.dumps(
        {
            "patient_id": patient_id,
            "lab_test": lab_test,
            "lab_value": lab_value,
            "risk_signals": risk_signals,
        },
        indent=2,
    )
