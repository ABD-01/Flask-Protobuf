from flask import Flask, request, render_template, g, send_file, session, redirect, make_response, render_template_string
import logging
import time
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # Replace with a secret key in production

# Dictionary to store loggers for each client
client_loggers = {}

def create_logger(client_identifier):
    logger = logging.getLogger(client_identifier)
    handler = RotatingFileHandler(f'logs/{client_identifier}.log', maxBytes=10000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

@app.route('/')
def home():
    session.clear()
    if 'client_identifier' not in session:
        client_identifier = f"{request.remote_addr}_{int(time.time())}"
        # client_identifier = f"{request.remote_addr}_client"
        session['client_identifier'] = client_identifier
        client_loggers[client_identifier] = create_logger(client_identifier)
    logger = client_loggers[session['client_identifier'] ]
    logger.info('User visited home route.')
    return 'Home Page'

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    logger = client_loggers[session['client_identifier'] ]
    if request.method == 'POST':
        logger.info("User clicked the button")
    else:
        logger.info('User visited hello route.')
    return '''<h1>Hello World
    <form action="/hello" method="post"><button>Download Logs</button><form>
    <button><a href="/download_logs">Download Logs</a></button> 
    '''

@app.route('/download_logs')
def download_logs():
    client_identifier = session['client_identifier']

    # Assuming the log file is located in the 'logs' directory
    log_file_path = f'logs/{client_identifier}.log'

    response = send_file(log_file_path, as_attachment=True)

    # Send the log file as a response
    # return redirect('/', response=response)
    return send_file(log_file_path)


if __name__ == '__main__':
    app.run(debug=True)