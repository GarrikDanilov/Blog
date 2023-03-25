import os
from blog.app import app
from blog.models.database import db


@app.cli.command('create-admin')
def create_admin():
    """
    flask create-admin
    """

    from blog.models import User

    admin = User(username='admin', is_staff=True)
    admin.password = os.environ.get('ADMIN_PASSWORD') or 'adminpass'

    db.session.add(admin)
    db.session.commit()

    print('done! created admin:', admin)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )


@app.cli.command("create-tags")
def create_tags():

    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag

    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
