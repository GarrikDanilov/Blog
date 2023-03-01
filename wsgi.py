from blog.app import app
from blog.models.database import db


@app.cli.command('init-db')
def init_db():
    """
    flask init-db
    """

    db.create_all()
    print('done!')

    
@app.cli.command('create-users')
def create_users():
    """
    flask create-users
    """

    from blog.models import User
    admin = User(username='admin', is_staff=True)
    james = User(username='james')

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print('done! created users:', admin, james)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )
    