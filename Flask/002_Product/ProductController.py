from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/product', methods=['GET'])
def get_all_product():
    items = Product.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/product/<int:id>', methods=['GET'])
def get_product(id):
    item = Product.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/product', methods=['POST'])
def create_product():
    data = request.get_json()
    item = Product(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/product/<int:id>', methods=['PUT'])
def update_product(id):
    item = Product.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    item = Product.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
