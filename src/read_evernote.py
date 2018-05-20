from evernote.api.client import EvernoteClient

developer_token = "S=s1:U=949fd:E=16ad2f8afd0:C=1637b478210:P=1cd:A=en-devtoken:V=2:H=1d7866568f6f8a7fcfb8511581a719f7"
 
# Set up the NoteStore client 
client = EvernoteClient(token=developer_token)
note_store = client.get_note_store()
 
# Make API calls
notebooks = note_store.listNotebooks()
for notebook in notebooks:
    print "Notebook: ", notebook.name