from app import create_app, db
from app.models.user import User
from app.models.plant import Plant
from app.models.reminder import Reminder

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Plant': Plant, 'Reminder': Reminder}

if __name__ == '__main__':
    app.run(debug=True)
