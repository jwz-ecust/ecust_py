# -*- coding: utf-8 -*-
import urllib2
import urllib

AUTOAUTHS = []


class _Request(urllib2.Request):
	def __init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None):
		urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
		self.method = method

	def get_method(self):
		if self.method:
			return self.method

		return urllib2.Request.get_method(self)


class Request(object):
	_METHODS = ('GET', 'HEAD', 'PUT', 'POST', 'DELETE')

	def __init__(self):
		#  self.url 赋值都会调用  __setattr__
		self.url = None
		self.headers = dict()
		self.method = None
		self.params = {}
		self.data = {}
		self.response = Response()
		self.auth = None
		self.sent = False

	def __repr__(self):
		try:
			repr = '<Request> [%s]' %(self.method)
		except:
			repr = '<Request Object>'
		return  repr

	def __setattr__(self, key, value):
		if (key == 'method') and (value):
			if value not in self._METHODS:
				raise InvalidMethod()
		object.__setattr__(self, key, value)

	def _checks(self):
		if not self.url:
			raise URLRequired

	def _get_opener(self):
		if self.auth:
			authr = urllib2.HTTPPasswordMgrWithDefaultRealm()

			authr.add_password(None, self.url, self.auth.urername, self.auth.password)
			handler = urllib2.HTTPBasicAuthHandler(authr)
			opener = urllib2.build_opener(handler)
			return opener.open
		else:
			return urllib2.urlopen

	def send(self):
		self._checks()

		success = False
		if self.method in ("GET", "HEAD", "DELETE"):

			if isinstance(self.params, dict):
				params = urllib.urlencode(self.params)
			else:
				params = self.params
			# combine to generate url
			req = _Request("%s?%s" %(self.url, params), method=self.method)

			if self.headers:
				req.headers = self.headers

			opener = self._get_opener()

			try:
				resp = opener(req)
				self.response.status_code = resp.code
				self.response.headers = resp.info().dict
				if self.method.lower() == 'get':
					self.response.content = resp.read()
				success = True
			except urllib2.HTTPError as why:
				self.response.status_code = why.code

		elif self.method = "PUT":
			if not self.sent:
				req = _Request(self.url, method="PUT")

				if self.headers:
					req.headers = self.headers

				req.data = self.data
				try:
					opener = self._get_opener()
					resp = opener(req)

					self.response.status_code = resp.code
					self.response.headers = resp.info().dict
					self.response.content = resp.read()

					success = True

				except urllib2.HTTPError as why:
					self.response.status_code = why.code
			elif self.method == "POST":
				if not self.sent:
					req = _Request(self.url, method='POST')
					if self.headers:
						req.headers = self.headers

					if isinstance(self.data, dict):
						req.data = urllib.urlencode(self.data)
					else:
						req.data = self.data

					try:
						opener = self._get_opener()
						resp = opener(req)

						self.response.status_code = resp.code
						self.response.headers = resp.info().dict
						self.response.content = resp.read()

						success = True

					except urllib2.HTTPError as why:
						self.response.status_code = why.code

			self.sent = True if success else False

			return success


class Response(object):
	def __init__(self):
		self.content = None
		self.status_code = None
		self.headers = dict()

	def __repr__(self):
		try:
			repr = '<Response [%s]>' % (self.status_code)
		except:
			repr = '<Response object>'
		return repr


class AuthObject(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password


def get(url, params={}, headers={}, auth=None):
	r = Request()
	r.method = "GET"
	r.url = url
	r.params = params
	r.headers = headers
	r.auth = _detect_auth(url, auth)

	r.send()
	return r.response


def head(url, params={}, headers={}, auth=None):
	r = Request()
	r.method = "HEAD"
	r.url = url
	r.params = params
	r.headers = headers
	r.auth = _detect_auth(url, auth)

	r.send()
	return r.response


def post(url, data="", headers={}, auth=None):
	r = Request()
	r.method = "GET"
	r.url = url
	r.data = data
	r.headers = headers
	r.auth = _detect_auth(url, auth)

	r.send()
	return r.response


def delete(url, params={}, headers={}, auth=None):
	r = Request()
	r.method = "DELETE"
	r.url = url
	r.headers = headers
	r.auth = _detect_auth(url, auth)

	r.send()
	return r.response


def add_autoauth(url, authobject):
	global AUTOAUTHS
	AUTOAUTHS.append((url, authobject))


def _detect_auth(url, auth):
	return _get_autoauth(url) if not auth else auth


def _get_autoauth(url):
	for (autoauth_url, auth) in AUTOAUTHS:
		if autoauth_url in url:
			return auth

	return None


class RequestException(Exception):
	"""There was an ambiguous exception that occured while handling your request."""


class InvalidMethod(RequestException):
	"""An inappropriate method was attempted."""


class URLRequired(RequestException):
	"""A valid URL is required to make a request."""
