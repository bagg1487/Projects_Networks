from flask import Flask, jsonify
import random

app = Flask(__name__)

EVENTS = [
    {"id": 1, "name": "Концерт", "location": "Москва"},
    {"id": 2, "name": "Ресторан", "location": "Казань"},
    {"id": 3, "name": "Конференция", "location": "ОАЭ"}
]

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(EVENTS)

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = next((e for e in EVENTS if e['id'] == event_id), None)
    if event:
        return jsonify(event)
    return jsonify({"error": "Event not found"}), 404

@app.route('/events', methods=['POST'])
def create_event():
    return jsonify({"id": random.randint(10, 100), "name": "New Event", "location": "Unknown"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8277)