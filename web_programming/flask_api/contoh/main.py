# Daftar package yang kita pakai
from flask import Flask, request, jsonify, make_response
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

# Create an instance of Flask
app = Flask(__name__)

# Create an instance of MySQL
mysql = MySQL()

# Create an instance of Flask RESTful API
api = Api(app)

# Set database credentials.
app.config["MYSQL_DATABASE_USER"] = "remote"
app.config["MYSQL_DATABASE_PASSWORD"] = "ilham211"
app.config["MYSQL_DATABASE_DB"] = "contohdatabase"
app.config["MYSQL_DATABASE_HOST"] = "localhost"

# Initialize the MySQL extension
mysql.init_app(app)


# Mendapatkan dan menampilkan data semua user
class UserList(Resource):
    # Method for get all users
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from user""")
            row_headers = [x[0] for x in cursor.description]
            result = cursor.fetchall()
            json_data = []
            for r in result:
                json_data.append(dict(zip(row_headers, r)))
            return make_response(jsonify({"data": json_data}), 200)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


# Mendapatkan dan menampilkan data user berdasarkan id
class User(Resource):
    # Method to get user by id
    def get(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("select * from user where id = %s", user_id)
            row_headers = [x[0] for x in cursor.description]
            result = cursor.fetchall()
            json_data = []
            for r in result:
                json_data.append(dict(zip(row_headers, r)))
            return make_response(jsonify({"data": json_data}), 200)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


# Menambahkan data User
class AddUser(Resource):
    def post(self):
        # Method for create new user
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _email = request.form["email"]
            _password = request.form["password"]
            _name = request.form["name"]
            insert_user_cmd = (
                """INSERT INTO user(email, password, name) VALUES(%s, %s, %s)"""
            )
            cursor.execute(insert_user_cmd, (_email, _password, _name))
            conn.commit()
            response = jsonify(message="User added successfully.", id=cursor.lastrowid)
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify("Failed to add user.")
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return response


# Mengupdate data user berdasarkan id
class Update(Resource):
    # Method to edit / update
    def put(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            # Fungsi agar kita mudah dalam mengedit
            def edit(tabel, value, user_id):
                update_user_cmd = (
                    """UPDATE user SET """
                    + tabel
                    + """ = '"""
                    + value
                    + """' WHERE user.id = %s"""
                )
                cursor.execute(update_user_cmd, (user_id))
                conn.commit()

            email = request.form.get("email")
            password = request.form.get("password")
            name = request.form.get("name")

            if email:
                edit("email", email, user_id)

            if password:
                edit("password", password, user_id)

            if name:
                edit("name", name, user_id)

            response = jsonify("User updated successfully.")
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify("Failed to update user.")
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return response


# Menghapus data user berdasarkan id
class Delete(Resource):
    # Method to delete
    def delete(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("delete from user where id = %s", user_id)
            conn.commit()
            response = jsonify("User deleted successfully.")
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify("Failed to delete user.")
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return response


# API resource routes
api.add_resource(UserList, "/users", endpoint="users")
api.add_resource(AddUser, "/adduser", endpoint="adduser")
api.add_resource(User, "/user/<int:user_id>", endpoint="user")
api.add_resource(Update, "/update/<int:user_id>", endpoint="update")
api.add_resource(Delete, "/delete/<int:user_id>", endpoint="delete")

# Api running di localhost dengan port 2020
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=2020)
