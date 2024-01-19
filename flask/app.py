from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models import PersonModel, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)

with app.app_context():
    db.create_all()

class PersonViews(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('data', type=list, required=True, help='Data must be a list of persons.')

    def get(self):
        persons = PersonModel.query.all()
        return {'persons': [person.json() for person in persons]}

    def post(self):
        try:
            args = self.parser.parse_args()
            print("args:", args)
            
            data = args['data']
            print("data:", data)

            for person_data in data:
                new_person = PersonModel(
                    FullName=person_data.get('FullName', 'DefaultName'),
                    SSN=person_data.get('SSN', 'DefaultSSN'),
                    Title=person_data.get('Title', 'DefaultTitle')
                )
                db.session.add(new_person)

            db.session.commit()
            db.session.flush()

            return {'message': 'Data added successfully'}, 201

        except Exception as e:
            print(f"Error in POST request: {e}")
            return {'message': 'Internal Server Error', 'error': str(e)}, 500


api.add_resource(PersonViews, '/person', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)
