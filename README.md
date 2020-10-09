# Personal Notes (CRUD)
In this article, we will build database operations e.g. CRUD (create, read, update, and delete) in Python. The app relies on mysql database to store our note data.


## Installation
- In order to host the database server on your system you can download and install mysql. There are several options but we’ll use the **XAMPP**, which is a popular open source Apache distribution and ships in with Mysql database.
- You can also  install **Postman**. Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.
- It is assumed that you have python3 installed as well. Other python packages needed for this task can be installed using pip:
`pip install flask flask-sqlalchemy pymysql`


## 1. How to run the application
- After installing all the necessary python libraries, run the python code as
`python codefile.py`. You can also run it in a virtual environment, if prefered. I am not going into details of how to setup a virtual environment here.
- Start the MySQL service: Click on MySQL Admin tab in XAMPP (open the phpMyAdmin); import the `notes.sql` file.


## 2. How to use the API
- Install and run the Postman;
Import the collection file: `noteapi.postman_collection.json`;
Click the options on the left.
- `GET, POST, PUT, DELETE` operations to create, save, update, and delete a note can be understood from the Postman collection import of the `noteapi.postman_collection.json` file or from the python code the `codefile.py`.
- `id, title, noteDescription, archivestatus` in XAMPP shows the respective id, title provided, some description given, and whether the note is archived or not (`0:inactive or archived, 1:active or not-archived`) for each entry present in the database.


## 3. Choice of technology
- I have used python, flask because of my familiarity with using python in the past.
- Alternatives to be considered include: Javascript, R (would like to explore it, as R is used in data analysis as well).


## 4. Other key features would you add
- Front end app system.
- Start the application with login system.

