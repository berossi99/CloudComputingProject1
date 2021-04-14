from flask import Flask
from flask import render_template, redirect, url_for
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/git')
def git():
    subprocess.call(['xterm', '-e', 'docker exec -it Git_Container bash'])
    return redirect(url_for("main"))

@app.route('/tf')
def tf():
    subprocess.call(['xterm', '-e', 'docker exec -it Tensorflow_Container bash'])
    return redirect(url_for("main"))

@app.route('/md')
def md():
    subprocess.call(['xterm', '-e', 'docker exec -it Markdown_Container bash'])
    return redirect(url_for("main"))

@app.route('/spy')
def spy():
    os.system("docker exec -t Spyder_Container adduser test")
    os.system("docker exec -t Spyder_Container usermod -a -G sudo test")
    subprocess.call(['xterm', '-e', 'docker exec -it Spyder_Container su - test'])

    return redirect(url_for("main"))

@app.route('/had')
def had():
    subprocess.call(['xterm', '-e', 'docker exec -it Hadoop_Container bash'])
    return redirect(url_for("main"))

@app.route('/spark')
def spark():
    subprocess.call(['xterm', '-e', 'docker exec -it Spark_Container ./bin/pyspark'])
    return redirect(url_for("main"))


