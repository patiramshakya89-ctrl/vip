import os


class Config:

    BOT_TOKEN = os.environ.get("8302055391:AAF-WPMNl_Z-CwSWpmsUI2fPooK8VIBrCN4")

    SESSION_NAME = os.environ.get("@VIP_PRO_Tg2Yt_Uploader_BOT", ":memory:")

    API_ID = int(os.environ.get("22518279"))

    API_HASH = os.environ.get("61e5cc94bc5e6318643707054e54caf4")

    CLIENT_ID = os.environ.get("581448970865-ebph14mds85o4e52r60iif1783rafa95.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("BOT_OWNER"))

    AUTH_USERS_TEXT = os.environ.get("7836790905,7968584207,7212452634,8117793426,5817712634,7958016772,7341059064,7714608838,8007442798,7068000043,7062964338,6947024366,5682377441,7504558633,6440249117,7943069140,5486913681,1959279443,1511257208,1226915008,7080838404,6148865829,7346516859,6660248311,8056915809,6660248311,7518770522,6507311220", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
