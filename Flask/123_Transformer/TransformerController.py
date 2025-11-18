from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transformer.db'
db = SQLAlchemy(app)

class Transformer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/transformer', methods=['GET'])
def get_all_transformer():
    items = Transformer.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/transformer/<int:id>', methods=['GET'])
def get_transformer(id):
    item = Transformer.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/transformer', methods=['POST'])
def create_transformer():
    data = request.get_json()
    item = Transformer(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/transformer/<int:id>', methods=['PUT'])
def update_transformer(id):
    item = Transformer.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/transformer/<int:id>', methods=['DELETE'])
def delete_transformer(id):
    item = Transformer.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
