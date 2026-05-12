python
# Importing necessary libraries
import pandas as pd
from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# Load the Freelancer Business Activities Dataset
data_path = "DL06-Freelance-Activities-ADRA-OD-010-AFR.xlsx"
df = pd.read_excel(data_path)

# Endpoint to fetch all activities
@app.route('/api/activities', methods=['GET'])
def get_activities():
    activities = df.to_dict(orient='records')
    return jsonify(activities)

# Endpoint to search activities by category or keyword
@app.route('/api/search', methods=['GET'])
def search_activities():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({'error': 'Query parameter q is required'}), 400

    filtered_activities = df[df.apply(lambda row: query in str(row['Activity Name']).lower() or query in str(row['Category']).lower(), axis=1)]
    return jsonify(filtered_activities.to_dict(orient='records'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
