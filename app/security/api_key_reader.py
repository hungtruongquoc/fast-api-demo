from app.services.firestore_client import db


class ApiKeyReader:
    def __init__(self):
        pass

    def read(self):
        # Access the "api0key" collection
        api_keys_collection = db.collection('api-key')
        docs = api_keys_collection.stream()

        # Check if docs is not None
        if docs is None:
            print("No documents found or error in fetching documents.")
        else:
            print(f"{api_keys_collection.id}")

        docs_list = list(docs)
        # Convert to list to check if it's empty
        if not docs_list:  # Check if the list is empty
            print("No documents found in the collection.")

        try:
            # Print all documents in the "api_keys" collection
            for doc in docs_list:
                print(f'{doc.id} => {doc.to_dict()}')
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_expiration(self, customer_name):
        # Fetch the document from the "api-key" collection
        doc_ref = db.collection('api-key').document(customer_name)
        doc = doc_ref.get()

        if doc.exists:
            # Extract the `expiration_timestamp` field from the document
            expiration_timestamp = doc.to_dict().get('expired', None)
            if expiration_timestamp:
                print(f"Expiration timestamp for {customer_name}: {expiration_timestamp}")
                return expiration_timestamp
            else:
                print(f"No expiration timestamp found for {customer_name}.")
                return None
        else:
            print("The document does not exist.")
            return None
