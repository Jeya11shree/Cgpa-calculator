import pandas as pd
import json

# Define grade points dictionary
grade_points ={'O': 10,
 'A+':9,
 'A':8,
 'B+':7,
 'B':6,
 'C':5,
 'RA':0,
 'SA':0}

filenames = input("Enter the filenames of the CSV files (separated by commas): ").split(',')
output = {}

     
if len(filenames)>=1:
    total_credits = 0
    total_grade_points = 0

    for filename in filenames:
        try:
            df = pd.read_csv(filename.strip())
        
            file_gpa = (df['credits'] * df['grade'].map(grade_points)).sum() / df[df['grade'].isin(grade_points.keys())]['credits'].sum()
        
            total_credits += df[df['grade'].isin(grade_points.keys())]['credits'].sum()
            total_grade_points += (df['credits'] * df['grade'].map(grade_points)).sum()
            
            total_credits = int(total_credits)
            total_grade_points = int(total_grade_points)
        
            output[filename.strip()] = {
                "GPA": round(file_gpa, 2),
                "Total Credits": total_credits
            }
        except FileNotFoundError:
            output[filename.strip()] = f"File '{filename.strip()}' not found"
       

    cgpa = round(total_grade_points / total_credits, 2)
    output["CGPA"] = cgpa

json_output = json.dumps(output, indent=4)
print(json_output)