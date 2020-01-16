import os
from django.core.exceptions import ValidationError

def audioFile(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('file must be a .mp3')
    filesize= value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")

def pfp(value):
    filesize = value.size
    if filesize > 250000:
        raise ValidationError("The maximum file size that can be uploaded is 250KB")