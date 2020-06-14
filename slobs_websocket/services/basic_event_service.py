"""
	Base Service that has Events associated with it
"""
from slobs_websocket import exceptions
from slobs_websocket.converter import *
from slobs_websocket.service_connection import ServiceConnection
from .basic_service import BasicService
import inspect

class EventsException(Exception):
	pass

class BasicEventService(BasicService):

	def __init__(self, *args):
		super().__init__(*args)

	def __getattr__(self,name):
		try:
			return getattr(ServiceConnection,name)
		except AttributeError:
			if name.startswith('__'):
				raise AttributeError("type object '{}' has no attribute '{}'".format(self.__class__.__name__, name))

			if hasattr(self, '__events__'):
				if name not in self.__events__:
					raise EventsException("Event '{}' is not declared".format(name))
			elif hasattr(self.__class__, '__events__'):
				if name not in self.__class__.__events__:
					raise EventsException("Event '{}' is not declared".format(name))
			self.__dict__[name] = ev = _EventSlot(name)

			frm = inspect.stack()[0]
			cls = frm[0].f_locals.get('self',None)
			method = name
			resource = cls.__class__.__name__

			decorated_event = "{}.{}".format(resource,method)

			if not decorated_event in ServiceConnection.instance.conn.thread_recv.events:
				ServiceConnection.instance.log.debug("Registering Event: {}".format(decorated_event))
				res = ServiceConnection._send_packet(method=method, resource=resource)
				if "_type" in res:
					if res["_type"] == "SUBSCRIPTION" and res["emitter"] == "STREAM":
						ServiceConnection.instance.log.debug("Event Registration completed for {}, now adding to Receiver Thread.".format(decorated_event))
						ServiceConnection.instance.conn.thread_recv.events[decorated_event] = self

			return ev

	def __repr__(self):
		return "<{}.{} object at {}>".format(self.__class__.__module__,self.__class__.__name__,hex(id(self)))

	__str__ = __repr__

	def __len__(self):
		return len(self.__dict__.items())

	def __iter__(self):
		def gen(dictitems=__dict__.items()):
			for attr, val in dictitems:
				if isinstance(val, _EventSlot):
					yield val
		return gen()

	def _processEvent(self, event, data):
		if has_converter(event):
			ndata = convert(event, data)
		else:
			ndata = data
		
		self.__dict__[event](ndata)

class _EventSlot:
	def __init__(self, name):
		self.targets = []
		self.__name__ = name

	def __repr__(self):
		return "<EVENT '{}'>".format(self.__name__)

	def __call__(self, *a, **kw):
		for f in tuple(self.targets):
			f(*a,**kw)

	def __iadd__(self, f):
		self.targets.append(f)
		return self
	
	def __isub__(self, f):
		while f in self.targets:
			self.targets.remove(f)
		return self

	def __len__(self):
		return len(self.targets)

	def __iter__(self):
		def gen():
			for target in self.targets:
				yield target
		return gen()

	def __getitem__(self, key):
		return self.targets[key]