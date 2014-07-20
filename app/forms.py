from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid',  validators = [Required()])
    remember_me = BooleanField('remember_me',  default = False)
