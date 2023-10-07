from db.database import Base, engine

import models.users as users
import models.seiyuus as seiyuus
import models.characters as characters
import models.companies as companies
import models.franchises as franchises
import models.roles as roles
import models.voice_samples as voice_samples
import models.works as works

def init_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)