from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Tom", "age": 20},
    {"id": 2, "name": "Jerry", "age": 16},
]


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/users")
def get_users():
    return jsonify(users)


@app.get("/users/<int:user_id>")
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "user not found"}), 404


@app.get("/users/search")
def search_users():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "name is required"}), 400
    result = [user for user in users if user["name"] == name]
    return jsonify(result)


@app.post("/users")
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "name and age are required"}), 400
    new_id = max(user["id"] for user in users) + 1
    new_user = {"id": new_id, "name": data["name"], "age": data["age"]}
    users.append(new_user)
    return jsonify(new_user), 201


@app.put("/users/<int:user_id>")
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            if "name" in data:
                user["name"] = data["name"]
            if "age" in data:
                user["age"] = data["age"]
            return jsonify(user)
    return jsonify({"error": "user not found"}), 404


@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"deleted": user_id}), 200
    return jsonify({"error": "user not found"}), 404


@app.post("/reset")
def reset_users():
    global users
    users = [
        {"id": 1, "name": "Tom", "age": 20},
        {"id": 2, "name": "Jerry", "age": 16},
    ]
    return jsonify({"status": "reset"})


# 正确的账号和密码，以及登录后返回的 token
VALID_USERNAME = "admin"
VALID_PASSWORD = "123456"
TOKEN = "abc123"


@app.post("/login")
def login():
    data = request.get_json()
    # 账号密码正确才返回 token
    if data.get("username") == VALID_USERNAME and data.get("password") == VALID_PASSWORD:
        return jsonify({"token": TOKEN})
    # 否则返回 401，表示未授权
    return jsonify({"error": "invalid credentials"}), 401


@app.get("/profile")
def profile():
    # 从请求头里拿 Authorization，也就是 token
    token = request.headers.get("Authorization")
    # token 不对就拒绝访问
    if token != TOKEN:
        return jsonify({"error": "unauthorized"}), 401
    return jsonify({"username": "admin", "email": "admin@example.com"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
