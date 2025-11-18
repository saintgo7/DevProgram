from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///message.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/message', methods=['GET'])
def get_all_message():
    items = Message.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/message/<int:id>', methods=['GET'])
def get_message(id):
    item = Message.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/message', methods=['POST'])
def create_message():
    data = request.get_json()
    item = Message(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/message/<int:id>', methods=['PUT'])
def update_message(id):
    item = Message.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/message/<int:id>', methods=['DELETE'])
def delete_message(id):
    item = Message.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
