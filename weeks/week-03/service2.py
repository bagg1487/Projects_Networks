from flask import Flask, jsonify

app = Flask(__name__)

OTHER_DATA = [
    {"id": 1, "description": "заглушка номер раз"},
    {"id": 2, "description": "заглушка номер дыва"},
    {"id": 3, "description": "загушка номер три"}
]

@app.route('/other', methods=['GET'])
def get_other():
    return jsonify(OTHER_DATA)

@app.route('/other/<int:other_id>', methods=['GET'])
def get_other_item(other_id):
    item = next((i for i in OTHER_DATA if i['id'] == other_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8288)