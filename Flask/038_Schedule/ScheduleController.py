from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'
db = SQLAlchemy(app)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/schedule', methods=['GET'])
def get_all_schedule():
    items = Schedule.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/schedule/<int:id>', methods=['GET'])
def get_schedule(id):
    item = Schedule.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/schedule', methods=['POST'])
def create_schedule():
    data = request.get_json()
    item = Schedule(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/schedule/<int:id>', methods=['PUT'])
def update_schedule(id):
    item = Schedule.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/schedule/<int:id>', methods=['DELETE'])
def delete_schedule(id):
    item = Schedule.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
