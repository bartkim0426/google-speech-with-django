# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_ALLOW_REGISTRATION = True

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_REQUIRED = True

# ACCOUNT_ADAPTER = 'artsumer.users.adapters.AccountAdapter'
# SOCIALACCOUNT_ADAPTER = 'artsumer.users.adapters.SocialAccountAdapter'

LOGIN_REDIRECT_URL = "/"

SITE_ID = 1

# allauth settings
# AUTH_USER_MODEL = 'artsumersuser.ArtsumersUser'

# ACCOUNT_SIGNUP_FORM_CLASS = 'artsumers.artsumersuser.forms.ArtsumersUserCreationForm'

# SOCIALACCOUNT_FORMS = {
#     'signup': 'artsumers.artsumersuser.forms.ArtsumersUserCreationForm'
# }

# Avoid SMPT
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
