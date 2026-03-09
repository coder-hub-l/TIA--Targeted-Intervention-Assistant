import pandas as pd
import os

# Path to your CSV file
# CSV_PATH = r"C:\Users\DELL\Documents\GitHub\opensoft-bot\data\engagement_results.csv"



def load_and_parse_data():


    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Dynamically build the path: Go up one level (..), then into 'data'
    csv_path = os.path.join(current_dir, "..", "data", "engagement_results.csv")
    
    # 3. Read the CSV using the dynamic path
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: File not found at {csv_path}}")
        return {}

    # 1. Filter: Only get employees marked for contact (is_selected = TRUE)
    target_employees = df[
        (df['is_selected'] == True) | 
        (df['is_selected'].astype(str).str.upper() == 'TRUE')
    ]

    employee_data = {}

    # 2. Parse the string using your split logic
    for index, row in target_employees.iterrows():
        emp_id = row['employee_id']
        shap_str = str(row['shap_values'])
        
        matches = []
        
        # First, split by comma to separate the features
        items = shap_str.split(",")
        
        # Next, loop through each item in the list
        for item in items:
            item = item.strip() # This removes any leading/trailing spaces
            if not item: 
                continue
            
            # Now split by the opening parenthesis
            parts = item.split("(")
            
            if len(parts) == 2:
                attribute = parts[0]
                # Take the second part (the number) and remove the closing parenthesis
                value_str = parts[1].replace(")", "")
                
                # Store them together as a tuple: ("FeatureName", "0.0323")
                matches.append((attribute, value_str))

        # Convert the string numbers to float for sorting, sort highest to lowest, take Top 3
        sorted_features = sorted(matches, key=lambda x: float(x[1]), reverse=True)
        top_3_issues = [item[0] for item in sorted_features[:3]]

        employee_data[emp_id] = top_3_issues

    return employee_data

