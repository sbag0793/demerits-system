import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# 제약조건 이름 자동으로 설정
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)



db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

def create_app():
  app = Flask(__name__)
  app.config.from_object(config)
  app.jinja_env.add_extension('jinja2.ext.loopcontrols')

  # ORM
  db.init_app(app)
  migrate.init_app(app, db)
  from . import models

  # Blueprint
  from .views import main_views, regist_views, event_views, chart_views
  app.register_blueprint(main_views.bp)
  app.register_blueprint(regist_views.bp)
  app.register_blueprint(event_views.bp)
  app.register_blueprint(chart_views.bp)

  return app