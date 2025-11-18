from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///input.db'
db = SQLAlchemy(app)

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/input', methods=['GET'])
def get_all_input():
    items = Input.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/input/<int:id>', methods=['GET'])
def get_input(id):
    item = Input.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/input', methods=['POST'])
def create_input():
    data = request.get_json()
    item = Input(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/input/<int:id>', methods=['PUT'])
def update_input(id):
    item = Input.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/input/<int:id>', methods=['DELETE'])
def delete_input(id):
    item = Input.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
