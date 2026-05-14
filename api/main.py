import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from fastapi import FastAPI, BackgroundTasks
from services.email_service import send_email




app = FastAPI()

@app.post("/send-mail/")
async def send_mail(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Welcome!", "Thanks for joining us.")
    return {"message": "Email is being sent!"}
