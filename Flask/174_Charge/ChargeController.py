from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///charge.db'
db = SQLAlchemy(app)

class Charge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/charge', methods=['GET'])
def get_all_charge():
    items = Charge.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/charge/<int:id>', methods=['GET'])
def get_charge(id):
    item = Charge.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/charge', methods=['POST'])
def create_charge():
    data = request.get_json()
    item = Charge(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/charge/<int:id>', methods=['PUT'])
def update_charge(id):
    item = Charge.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/charge/<int:id>', methods=['DELETE'])
def delete_charge(id):
    item = Charge.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
