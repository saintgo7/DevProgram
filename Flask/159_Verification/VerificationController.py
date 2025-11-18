from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///verification.db'
db = SQLAlchemy(app)

class Verification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/verification', methods=['GET'])
def get_all_verification():
    items = Verification.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/verification/<int:id>', methods=['GET'])
def get_verification(id):
    item = Verification.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/verification', methods=['POST'])
def create_verification():
    data = request.get_json()
    item = Verification(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/verification/<int:id>', methods=['PUT'])
def update_verification(id):
    item = Verification.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/verification/<int:id>', methods=['DELETE'])
def delete_verification(id):
    item = Verification.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
