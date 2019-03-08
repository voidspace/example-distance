FROM python:3.6
COPY binaries/location/location-0.1.0-py3-none-any.whl /
COPY dist/distance-0.1.0-py3-none-any.whl /
COPY requirements.txt /
COPY manage.py /
RUN pip install -r requirements.txt
RUN pip install location-0.1.0-py3-none-any.whl
ENV DJANGO_SETTINGS_MODULE=distance.settings
CMD [ "django-admin", "migrate" ]
CMD [ "django-admin", "runserver", "0.0.0.0:8000" ]