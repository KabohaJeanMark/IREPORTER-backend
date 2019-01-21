import datetime


class BaseRedFlags():
    def __init__(self, created_by, incident_type):

        self.created_by = created_by
        self.incident_type = incident_type
        self.created_on = datetime.datetime.now()


class Redflags():
    def __init__(self, base, redflag_id, status, images, videos, comment, location):
        self.base = base
        self.redflag_id = redflag_id
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment
        self.location = location

    def to_json(self):
        return{

            "created by": self.base.created_by,
            "incident type": self.base.incident_type,
            "id": self.redflag_id,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comments": self.comment,
            "location": self.location,
            "created on": datetime.datetime.now()
        }


class RedFlagsDb():

    def __init__(self):
        self.incident_list = []

    def add_redflag(self, redflag):
        self.incident_list.append(redflag)

    def get_redflags(self):
        return self.incident_list

    def get_one_redflag_by_id(self, redflag_id):
        for redflag in self.incident_list:
            if redflag.redflag_id == redflag_id:
                return redflag
        return None
