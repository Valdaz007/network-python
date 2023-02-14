from flask import Flask, render_template, url_for
import netmiko

app = Flask(__name__)

rt1 = {
  "ip":"<device_ip_address>",
  "device_type":"<device_type>",
  "username":"<username>",
  "password":"<pasword>"
}

@app.route("/")
def index():
  return "#"
  
@app.route("/sh_clock")
def sh_clock():
  return "#"
  
@app.route("/sh_run")
def sh_run():
  return "#"
  
@app.route("/sh_ip_int_br")
def sh_ip_int_br():
  return "#"
  
@app.route("/sh_int")
def sh_int():
  return "#"
