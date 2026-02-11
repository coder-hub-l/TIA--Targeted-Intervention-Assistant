import pandas as pd
import re

# Path to your CSV file
CSV_PATH = "../data/engagement_results.csv"

def load_and_parse_data():
    """
    Reads CSV, filters for 'is_selected=TRUE', and parses SHAP values.
    Returns a dictionary: { "EMP123": ["Issue_A", "Issue_B"] }
    """
    try:
        df = pd.read_csv(CSV_PATH)
    except FileNotFoundError:
        print(f"Error: File not found at {CSV_PATH}")
        return {}

    # 1. Filter: Only get employees marked for contact (is_selected = TRUE)
    # Note: Checking for boolean True or string 'TRUE' just in case
    target_employees = df[
        (df['is_selected'] == True) | 
        (df['is_selected'].astype(str).str.upper() == 'TRUE')
    ]

    employee_data = {}

    # 2. Parse the messy string: "FeatureA(0.5), FeatureB(0.2)"
    for index, row in target_employees.iterrows():
        emp_id = row['employee_id']
        shap_str = str(row['shap_values'])

        # Regex to find words before parenthesis and the number inside
        # Matches: "Days_since_last_reward(0.1779)"
        pattern = r"([a-zA-Z_0-9]+)\((-?\d+\.\d+)\)"
        matches = re.findall(pattern, shap_str)

        # Convert to dict, sort by impact (highest number first), and take Top 3
        # We convert the score to float for sorting
        sorted_features = sorted(matches, key=lambda x: float(x[1]), reverse=True)
        top_3_issues = [item[0] for item in sorted_features[:3]]

        employee_data[emp_id] = top_3_issues

    return employee_data

# Quick test to see if it works when you run this file directly
if __name__ == "__main__":
    data = load_and_parse_data()
    print("Successfully parsed data!")
    print(f"Loaded {len(data)} target employees.")
    if data:
        sample_id = list(data.keys())[0]
        print(f"Sample ({sample_id}): Top Issues -> {data[sample_id]}")