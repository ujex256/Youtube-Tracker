class VideoNotRegistered(Exception):
    id: str = "VIDEO_NOT_REGISTERED"


class VideoAlreadyRegistered(Exception):
    id: str = "VIDEO_ALREADY_REGISTERED"


class VideoNotFound(Exception):
    id: str = "VIDEO_NOT_FOUND"
