from application import application, db
from application.models import User

if __name__ == '__main__':
    #application.run(host='0.0.0.0')
    application.run(port=5000)


@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}