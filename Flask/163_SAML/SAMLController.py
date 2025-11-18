from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saml.db'
db = SQLAlchemy(app)

class SAML(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/saml', methods=['GET'])
def get_all_saml():
    items = SAML.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/saml/<int:id>', methods=['GET'])
def get_saml(id):
    item = SAML.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/saml', methods=['POST'])
def create_saml():
    data = request.get_json()
    item = SAML(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/saml/<int:id>', methods=['PUT'])
def update_saml(id):
    item = SAML.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/saml/<int:id>', methods=['DELETE'])
def delete_saml(id):
    item = SAML.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
