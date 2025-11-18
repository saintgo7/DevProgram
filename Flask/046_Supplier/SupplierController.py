from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supplier.db'
db = SQLAlchemy(app)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/supplier', methods=['GET'])
def get_all_supplier():
    items = Supplier.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/supplier/<int:id>', methods=['GET'])
def get_supplier(id):
    item = Supplier.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/supplier', methods=['POST'])
def create_supplier():
    data = request.get_json()
    item = Supplier(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/supplier/<int:id>', methods=['PUT'])
def update_supplier(id):
    item = Supplier.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/supplier/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    item = Supplier.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
