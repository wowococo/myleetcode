import uuid
node = uuid.getnode()
# print node

print(uuid.UUID(int=node).hex[-12:].upper())
