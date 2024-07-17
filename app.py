from flask import Flask, request, jsonify
import csv
import json

app = Flask(__name__)


@app.route('/save-records', methods=['GET'])
def save_records():

    if 'playlist_file' not in request.files:
            return jsonify({"success": False, "message": "File not found!"})
    
    playlist_vivpro = request.files['playlist_file']
    input_data = json.load(playlist_vivpro)

    keys = list(input_data.keys())
    n = len(next(iter(input_data.values())))

    result_json = {}

    for i in range(n):
        result_json[input_data['id'][str(i)]] = {}
        for k in keys:
            result_json[input_data['id'][str(i)]][k] = input_data[k][str(i)]

    with open('output.json', 'w') as json_output:
        json.dump(result_json, json_output)

    with open('output.csv', 'w', encoding='utf-8', newline='') as csvoutput:
        writer = csv.writer(csvoutput)
        writer.writerow(keys)
    
        for k, v in result_json.items():
            row = list(v.values())
            writer.writerow(row)

    return jsonify({"success": True, "message": "File saved!"})
    

@app.route('/fetch-records', methods=['GET'])
def fetch_all_records():
    
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    with open('output.json', 'r') as saved_file:
        input_json = json.load(saved_file)

    start = (page-1) * per_page
    end = start + per_page

    paginated_data = list(input_json.items())[start:end]

    result_json = {k: v for k, v in paginated_data}

    return jsonify(result_json)


@app.route('/fetch-by-title/<title>', methods=['GET'])
def fetch_by_title(title):

    with open('playlist_vivpro.json', 'r') as saved_file:
        input_data = json.load(saved_file)

    result_json = {}
    keys = list(input_data.keys())

    for i, v in input_data['title'].items():
        if v == title:
            result_json[input_data['id'][str(i)]] = {}
            for key in keys:
                result_json[input_data['id'][str(i)]][key] = input_data[key][str(i)]
            return jsonify(result_json)

    return jsonify({"success": False, "message": "Title not found!"})



if __name__ == '__main__':
    app.run()

