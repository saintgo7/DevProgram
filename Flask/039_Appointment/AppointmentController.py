from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointment.db'
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/appointment', methods=['GET'])
def get_all_appointment():
    items = Appointment.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/appointment/<int:id>', methods=['GET'])
def get_appointment(id):
    item = Appointment.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/appointment', methods=['POST'])
def create_appointment():
    data = request.get_json()
    item = Appointment(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/appointment/<int:id>', methods=['PUT'])
def update_appointment(id):
    item = Appointment.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/appointment/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    item = Appointment.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
