import time
import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class ContactService(addressbook_pb2.EarlyAdopterContactServiceServicer):

	def __init__(self):
		self.Contacts = []


	def AddContact(self, request, context):
		# add to a list
		self.Contacts.append(request)
		ack = addressbook_pb2.ContactAck(msg = "Added!")
		return ack


	def QueryContactName(self, request, context):
		contact = next((c for c in self.Contacts if c.name == request.name ), None)
		return contact


def serve():
	server = addressbook_pb2.early_adopter_create_ContactService_server(
		ContactService(), 50052, None, None)
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop()

if __name__ == '__main__':
	serve()
