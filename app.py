from flask import Flask,render_template


from flask_socketio import SocketIO,send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'hello'

@app.route('/chat')
def chat():
    return render_template('chat.html')




@socketio.on('message')
def handle_message(msg):
    print('消息:' + msg)
    send(msg,broadcast=True)


if __name__ == "__main__":
    app.run(debug=True)