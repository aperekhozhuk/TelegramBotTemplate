from app.database import session_maker
from app.models import User
from sqlalchemy.exc import IntegrityError


def start(update, context):
    message = update.message

    user = User(id=message.chat_id)
    session = session_maker()
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
    finally:
        session.close()

    message.reply_text(f"Hello, {message.from_user.first_name}!")
