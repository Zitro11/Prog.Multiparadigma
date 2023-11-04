class BasicConfig:
    User_DB='postgres'
    PASS_DB='Admin1'
    URL_DB='localhost'
    PORT_DB='5050'
    NAME_DB='flask'
    FULL_URL_DB=f'postgresql://{User_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI=FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY="llave_secreta"