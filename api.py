from flask import Flask
from flask import request
from models import db


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{PROJECT_DB_USER}:{PROJECT_DB_PASSWORD}@localhost/{PROJECT_NAME}'

db.init_app(app)



@app.route('/')
def get_home():
    return 'OI ESTOU AQUI'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)



@app.route('/users')
class User(Resource):

    def post(self, *args, **kwargs):
        """ Creating a new User """
        data = request.get_json(force=True)
        schema = UserSchema()
        if data:
            logger.info("Data got by /api/test/testId method %s" % data)


            # Validation with schema.load() OPTION_2
            user, errors = schema.load(data)
            print(user)
            print(errors)

            if errors:
                return {"errors": errors}, 422
            user.save_to_db()
            return {"message": USER_CREATED_SUCCESSFULLY}, 201


    def get(self):
        return {"subscriberList":users}
