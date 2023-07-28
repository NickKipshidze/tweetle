import sqlite3, argon2, base64

connection: sqlite3.Connection = sqlite3.connect("./tweetle.db")
cursor: sqlite3.Cursor = connection.cursor()

user_columns: tuple[str] = (
    "id", "username", "password"
)

post_columns: tuple[str] = (
    "id", "author_id", "content", "likes"
)

def encrypt(password: str) -> str:
    return base64.b64encode(
        argon2.argon2_hash(
            password, 
            "tweetle_argon2_salt",
            t = 16, m = 8, p = 1,
            buflen = 128, 
            argon_type = argon2.Argon2Type.Argon2_i
        )
    ).decode()

def new_user(username: str, password: str) -> None:
    cursor.execute(
        f"INSERT INTO users (username, password)"
        f"VALUES ('{username}', '{encrypt(password)}');"
    )
    connection.commit()

def new_post(author_id: int, content: str, likes: int = 0) -> None:
    cursor.execute(
        f"INSERT INTO posts (author_id, content, likes) "
        f"VALUES ({author_id}, '{content}', {likes});"
    )
    connection.commit()

def get_user(id_: int = None, username: str = None) -> dict:
    if id_:
        cursor.execute(
            f"SELECT * FROM users "
            f"WHERE id = {id_};"
        )
    elif username:
        cursor.execute(
            f"SELECT * FROM users "
            f"WHERE username = '{username}';"
        )
    
    try:
        return {
            user_columns[index]: value 
            for index, value in enumerate(cursor.fetchone())
        }
    except TypeError:
        return None

def get_post(id_: int) -> dict:
    cursor.execute(
        f"SELECT * FROM posts "
        f"WHERE id = {id_};"
    )
    
    try:
        return {
            post_columns[index]: value 
            for index, value in enumerate(cursor.fetchone())
        }
    except TypeError:
        return None

def init_database() -> None:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,       
            username VARCHAR(64) NOT NULL UNIQUE,
            password VARCHAR(172) NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,       
            author_id INTEGER NOT NULL,
            content VARCHAR(256) NOT NULL,
            likes INTEGER DEFAULT 0
        );
    """)
    
    connection.commit()

init_database()