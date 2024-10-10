from flask import Flask, request, jsonify, render_template
from kalkulator_statistika import calculate_mean, calculate_median, calculate_mode, calculate_midrange, calculate_midhinge
from kalkulator_statistika import calculate_quartile, calculate_decile, calculate_percentile, calculate_iqr
from kalkulator_statistika import stem_and_leaf_plot, box_whisker_plot

app = Flask(__name__)

# Rute untuk frontend
@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk menghitung statistik
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json['data']
    operation = request.json['operation']

    if operation == 'mean':
        result = calculate_mean(data)
    elif operation == 'median':
        result = calculate_median(data)
    elif operation == 'mode':
        result = calculate_mode(data)
    elif operation == 'midrange':
        result = calculate_midrange(data)
    elif operation == 'midhinge':
        result = calculate_midhinge(data)
    elif operation == 'quartile':
        result = calculate_quartile(data)
    elif operation == 'decile':
        result = calculate_decile(data)
    elif operation == 'percentile':
        result = calculate_percentile(data)
    elif operation == 'iqr':
        result = calculate_iqr(data)
    elif operation == 'stemandleaf':
        result = stem_and_leaf_plot(data)
    elif operation == 'boxplot':
        result = box_whisker_plot(data)
    else:
        result = "Operasi tidak valid"

    return jsonify(result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
