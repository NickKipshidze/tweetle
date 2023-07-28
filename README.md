# tweetle
Twitter clone made with Python FastAPI.

### Database

`tweetle.db` has some dummy accounts for testing:

```
sqlite> SELECT * FROM users;
+----+----------+--------------------------------------------------------------+
| id | username |                           password                           |
+----+----------+--------------------------------------------------------------+
| 1  | Nick     | W9U0hLJd8qLD3i2oo3TLu8E9Z9ko49m8Ik8/z1MhMR1rja+hzNmA9P4s8M38 |
|    |          | JFAJq9uJ60yFUmyporVEJKnhLp7+LCkiHHqFwL3d//Xt8hoxaVFFg8w7r5FT |
|    |          | vkJ/HW6q/CTEUv0fuQviyMxr1Igk3byCpKhwpgaCaMQevBz0wyM=         |
+----+----------+--------------------------------------------------------------+
| 2  | George   | PZ3VdhLPgKT7ER8crayEH3qE20YpNeizP6oTaOTG+V1sODG28TJJBLPurALx |
|    |          | 2QQI16XbMbJ/1zwXCLif80g3hj8+phsI3OwHm0HJMv6gCnyrb080h4e01rnf |
|    |          | kj7Nam2q05vFJffRIaW+WrKzMto7fZuAvvP4o43JXIU2fCMw4xc=         |
+----+----------+--------------------------------------------------------------+
```

In the future the user would also have email, bio, profile_picture and many other columns.

### Running the code

In the terminal run:

```bash
$ uvicorn API.main:app --reload
```

This will start the FastAPI server on localhost. After that you can open `./frontend/index.html` in the browser.
