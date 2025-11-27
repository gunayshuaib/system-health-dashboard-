from flask import Flask, render_template, jsonify
import psutil
import time


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/metrics')
def metrics():
	# simple example metrics — adapt to your needs
	cpu = psutil.cpu_percent(interval=0.2)
	mem = psutil.virtual_memory().percent
	now = int(time.time() * 1000)
	data = {
		'timestamp': now,
		'cpu': cpu,
	'memory': mem
	}
	return jsonify(data)


if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)