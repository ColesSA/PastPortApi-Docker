"""API Runable"""

from api import app, sched

sched.safe_start()
#context = ('cert/cert.pem', 'cert/key.pem')
# place into the run function: ssl_context=context
app.run(host='0.0.0.0', port=5000)
