from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
db = SQLAlchemy(app)

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/invoice', methods=['GET'])
def get_all_invoice():
    items = Invoice.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/invoice/<int:id>', methods=['GET'])
def get_invoice(id):
    item = Invoice.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/invoice', methods=['POST'])
def create_invoice():
    data = request.get_json()
    item = Invoice(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/invoice/<int:id>', methods=['PUT'])
def update_invoice(id):
    item = Invoice.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/invoice/<int:id>', methods=['DELETE'])
def delete_invoice(id):
    item = Invoice.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
