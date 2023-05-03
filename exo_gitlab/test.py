 
import requests 
import unittest

class TestAPI(unittest.TestCase):
	def test_requests(self):
		self.assertEqual(requests.get("http://127.0.0.1:4999/StartingNewProjetFlask/querystring/payload").status_code,200)
		
	def test_requestsb(self):
		self.assertEqual(requests.get("http://127.0.0.1:4999/ActiverAudit/querystring/payload/id_projet").status_code,200)

	def test_requestsc(self):
		self.assertEqual(requests.get("http://127.0.0.1:4999/ExecuterAuditFlask/querystring/id_projet").status_code,200)

	def test_requestsd(self):
		self.assertEqual(requests.get("http://127.0.0.1:4999/ObtenirRapportFlask/querystring/id_projet").status_code,200)
                

if __name__ == '__main__':
  unittest.main()





#request.get http://127.0.0.1:4999/ActiverAudit/querystring/payload/id_projet
		#request.get http://127.0.0.1:4999/ExecuterAuditFlask/querystring/id_projet
		#request.get http://127.0.0.1:4999/ObtenirRapportFlask/querystring/id_projet
