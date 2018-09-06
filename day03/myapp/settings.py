

class Config():
    DEBUG = False
    SECRET_KEY = "fhujkcxnijpdv"
    SESSION_TYPE = "redis"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def get_db_uri(db_conf):
    uri = "{db}+{engine}://{user}:{pwd}@{host}:{port}/{name}".format(
        db = db_conf.get("DB"),
        engine = db_conf.get("ENGINE"),
        user = db_conf.get("USER"),
        pwd = db_conf.get("PWD"),
        host = db_conf.get("HOST"),
        port = db_conf.get("PORT"),
        name = db_conf.get("NAME")
    )
    return uri



class DebugConfig(Config):
    DEBUG = True
    DATABASE = {
        "DB":"mysql",
        "ENGINE":"pymysql",
        "USER":"root",
        "PWD":"471753",
        "HOST":"106.12.109.74",
        "PORT":3306,
        "NAME":"fl03"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

config = {
    "debug":DebugConfig
}