from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///widget.db'
db = SQLAlchemy(app)

class Widget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/widget', methods=['GET'])
def get_all_widget():
    items = Widget.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/widget/<int:id>', methods=['GET'])
def get_widget(id):
    item = Widget.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/widget', methods=['POST'])
def create_widget():
    data = request.get_json()
    item = Widget(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/widget/<int:id>', methods=['PUT'])
def update_widget(id):
    item = Widget.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/widget/<int:id>', methods=['DELETE'])
def delete_widget(id):
    item = Widget.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
