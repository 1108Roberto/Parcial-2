from flask import Flask, jsonify, abort
import pandas as pd

app = Flask(__name__)

# Load the dataset with Pandas
df = pd.read_csv('vaccination_data.csv')

# Filter the dataset to only include Panama
df_panama = df[df['Country'] == 'Panama']

# Get all vaccination data for Panama
@app.route('/api/vaccination/panama', methods=['GET'])
def get_all_data():
    result = df_panama.to_dict(orient='records')
    return jsonify(result)

# Get vaccination data for a specific year in Panama
@app.route('/api/vaccination/panama/<int:year>', methods=['GET'])
def get_data_by_year(year):
    df_year = df_panama[df_panama['Year'] == year]
    if df_year.empty:
        abort(404, description="Data not found")
    else:
        result = df_year.to_dict(orient='records')
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
