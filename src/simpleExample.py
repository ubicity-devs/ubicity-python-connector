#!/usr/bin/env python3
import time
import os
import stomp

from lib import ConfigReader
from lib import EventEntry

class MyListener(object):
	def on_error(self, headers, message):
		print('received an error %s' % message)
		
	def on_message(self, headers, message):
		print('received a headers %s' % headers)
		print('received a message %s' % message)
		
		entry = EventEntry.EventEntry(message)
		print (entry.get_header()["ES_INDEX"])
		print (entry.get_body())
		print (entry.to_json())

cfg = ConfigReader.ConfigReader(os.path.dirname(__file__), 'connector.cfg', 'ubicity')

conn = stomp.Connection([(cfg.get_string('host'), cfg.get_int('port'))])
conn.set_listener('', MyListener())
conn.start()
conn.connect(wait=True)

conn.subscribe(destination=cfg.get_string('destination'), id=1, ack='auto')
conn.send(body='{"header":{"ES_TYPE":"type","ES_INDEX":"index"},"body":"Body"}', destination=cfg.get_string('destination'))

time.sleep(2)
conn.disconnect()