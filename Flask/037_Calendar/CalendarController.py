from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
db = SQLAlchemy(app)

class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/calendar', methods=['GET'])
def get_all_calendar():
    items = Calendar.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/calendar/<int:id>', methods=['GET'])
def get_calendar(id):
    item = Calendar.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/calendar', methods=['POST'])
def create_calendar():
    data = request.get_json()
    item = Calendar(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/calendar/<int:id>', methods=['PUT'])
def update_calendar(id):
    item = Calendar.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/calendar/<int:id>', methods=['DELETE'])
def delete_calendar(id):
    item = Calendar.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
