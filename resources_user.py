from schemas.user import UserSchema
user_schema = UserSchema(exclude='visits')


USER_ALREADY_EXIST = "A user with the same name already exists"
USER_CREATED_SUCCESSFULLY = "User was sucessfully created"


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
