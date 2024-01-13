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
  return render_template(
    'index.html',
    title='home'
  )
  
@app.route("/sh_clock")
def sh_clock():
  try:
    shh_connection = netmiko.ConnectHandler(**rt1)
    cmd_results = shh_connection.send_command('sh clock')
    cmd_results = cmd_results.split('\n')
    ssh_connection.disconnect()
    return render_template(
      'sh_clock.html',
      title='sh_clock',
      results = cmd_results
    )
  except:
    return render_template(
      'index.html',
      title='home - something went wrong!'
    )
  
@app.route("/sh_run")
def sh_run():
  try:
    shh_connection = netmiko.ConnectHandler(**rt1)
    cmd_results = shh_connection.send_command('sh run')
    cmd_results = cmd_results.split('\n')
    ssh_connection.disconnect()
    return render_template(
      'sh_run.html',
      title='sh_run',
      results = cmd_results
    )
  except:
    return render_template(
      'index.html',
      title='home - something went wrong!'
    )
  
@app.route("/sh_ip_int_br")
def sh_ip_int_br():
  try:
    shh_connection = netmiko.ConnectHandler(**rt1)
    cmd_results = shh_connection.send_command('sh ip int brief')
    cmd_results = cmd_results.split('\n')
    ssh_connection.disconnect()
    return render_template(
      'sh_ip_int_br.html',
      title='sh_ip_int_br',
      results = cmd_results
    )
  except:
    return render_template(
      'index.html',
      title='home - something went wrong!'
    )
  
@app.route("/sh_int")
def sh_int():
  try:
    shh_connection = netmiko.ConnectHandler(**rt1)
    cmd_results = shh_connection.send_command('sh int')
    cmd_results = cmd_results.split('\n')
    ssh_connection.disconnect()
    return render_template(
      'sh_int.html',
      title='sh_int',
      results = cmd_results
    )
  except:
    return render_template(
      'index.html',
      title='home - something went wrong!'
    )
