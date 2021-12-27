from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
from loguru import logger
from config import LOGDIR, LOGFILE, ORIGINS, BASEDIR

#logging app on the file
LOGDIR = BASEDIR + "/" + LOGDIR

if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)

logger.add(LOGDIR + "/" + LOGFILE, rotation="5MB", level="ERROR")


# Initialize the app
app = FastAPI()


# Origins
# Multiple origins can be specified
origins = []

for o in ORIGINS.split(","):
    origins.append(o)

# CORS - for our API security
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from api.views import main
