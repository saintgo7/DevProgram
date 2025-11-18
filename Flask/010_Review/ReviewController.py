from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///review.db'
db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/review', methods=['GET'])
def get_all_review():
    items = Review.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/review/<int:id>', methods=['GET'])
def get_review(id):
    item = Review.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/review', methods=['POST'])
def create_review():
    data = request.get_json()
    item = Review(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/review/<int:id>', methods=['PUT'])
def update_review(id):
    item = Review.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/review/<int:id>', methods=['DELETE'])
def delete_review(id):
    item = Review.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
