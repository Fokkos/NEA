import os
from django.core.exceptions import ValidationError #Returns error if data is not valid

def audioFile(value): #Validator for audio files
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3'] #Only accept .mp3
    if not ext.lower() in valid_extensions: #If not the correct filetype...
        raise ValidationError('file must be a .mp3') #Return an error
    filesize= value.size #attribute the uploaded filesize to variable filesize
    if filesize > 10000000: #If less than 10MB...
        raise ValidationError("The maximum file size that can be uploaded is 10MB") #Return an error

def pfp(value):
    filesize = value.size
    if filesize > 250000:
        raise ValidationError("The maximum file size that can be uploaded is 250KB")