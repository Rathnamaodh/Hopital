def validate_file_extension_image(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.JPG','.JPEG','.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose jpg format onlt...')


def validate_file_extension_xls(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose xls formate only.')