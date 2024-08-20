from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar datos
df = pd.read_csv('975f3705-b7e2-4555-b14b-a9a3a07503b0_Data.csv')

# Ruta para obtener todos los datos
@app.route('/api/v1/vaccination', methods=['GET'])
def get_vaccination_data():
    data = df.to_dict(orient='records')
    return jsonify(data)

# Ruta para obtener datos de un año específico
@app.route('/api/v1/vaccination/<int:year>', methods=['GET'])
def get_vaccination_data_by_year(year):
    data = df[df['Year'] == year].to_dict(orient='records')
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
