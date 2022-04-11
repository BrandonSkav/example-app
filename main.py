from flask import Flask, jsonify
from multiprocessing import Value
import streamlit as st

app = Flask(__name__)

counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def index():
    clicker = st.button("CLICK")
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return jsonify(count=out)

app.run()