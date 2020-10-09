from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/notes'
db = SQLAlchemy(app)


# Create database
class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    noteDescription = db.Column(db.String(100))
    archivestatus = db.Column(db.Integer)  # 0:inactive, 1:active

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self

    def __init__(self, title, noteDescription, archivestatus):
        self.title = title
        self.noteDescription = noteDescription
        self.archivestatus = archivestatus

    def __repr__(self):
        return '' % self.id

db.create_all()

class NoteSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Note
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    noteDescription = fields.String(required=True)
    archivestatus = fields.Number(required=True)

# Get all the notes
@app.route('/notes', methods = ['GET'])
def index():
    get_notes = Note.query.all()
    note_schema = NoteSchema(many=True)
    notes = note_schema.dump(get_notes)
    return make_response(jsonify({"note": notes}))

# Get a note by the specified id
@app.route('/notes/<id>', methods = ['GET'])
def get_note_by_id(id):
    get_note = Note.query.get(id)
    note_schema = NoteSchema()
    note = note_schema.dump(get_note)
    return make_response(jsonify({"note": note}))

# Update a particular note with id
@app.route('/notes/<id>', methods = ['PUT'])
def update_note_by_id(id):
    data = request.get_json()
    get_note = Note.query.get(id)
    if data.get('title'):
        get_note.title = data['title']
    if data.get('noteDescription'):
        get_note.noteDescription = data['noteDescription']
    if data.get('archivestatus'):
        get_note.archivestatus= data['archivestatus']
    db.session.add(get_note)
    db.session.commit()
    note_schema = NoteSchema(only=['id', 'title', 'noteDescription','archivestatus'])
    note = note_schema.dump(get_note)
    return make_response(jsonify({"note": note}))

# Update a particular note archivestatus with id
# archivestatus 1 becomes 0 and vice-versa
@app.route('/notes/archive/<id>', methods = ['PUT'])
def update_note_archive_by_id(id):
    data = request.get_json()
    get_note = Note.query.get(id)
    note_schema = NoteSchema()
    note = note_schema.dump(get_note)
    if note.get('archivestatus') == 1:
        get_note.archivestatus= 0
    else :
        get_note.archivestatus= 1
    db.session.add(get_note)
    db.session.commit()
    note_schema = NoteSchema(only=['id', 'title', 'noteDescription','archivestatus'])
    note = note_schema.dump(get_note)
    return make_response(jsonify({"note": note}))

# Get/Filter the first note with archive status
@app.route('/notes/archive/<status>', methods = ['GET'])
def get_note_archive_by_status(status):
    get_note = Note.query.filter_by(archivestatus=status).first()
    note_schema = NoteSchema()
    note = note_schema.dump(get_note)
    return make_response(jsonify({"note": note}))

# Delete a particular note with id
@app.route('/notes/<id>', methods = ['DELETE'])
def delete_note_by_id(id):
    get_note = Note.query.get(id)
    db.session.delete(get_note)
    db.session.commit()
    return make_response("",204)

@app.route('/notes', methods = ['POST'])
def create_note():
    data = request.get_json()
    note_schema = NoteSchema()
    note = note_schema.load(data)
    result = note_schema.dump(note.create())
    return make_response(jsonify({"note": result}),200)

if __name__ == "__main__":
    app.run(debug=True)
