from reactpy import event
import shutil

@event(prevent_default=True)
async def handle_upload(event):
    print(event)
    
    """
    path = event.get("currentTarget").get("value")
    localPath = "processing/"
    for file in path:
        shutil.copy(file, localPath)"""