FROM python:3.6
RUN mkdir /code
COPY binaries/location/location-0.1.0-py3-none-any.whl /code
#COPY dist/distance-0.1.0-py3-none-any.whl /code
COPY requirements.txt /code
COPY manage.py /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install location-0.1.0-py3-none-any.whl
#RUN pip install distance-0.1.0-py3-none-any.whl
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/code
ENV DJANGO_SETTINGS_MODULE=distance.settings
CMD [ "django-admin", "runserver", "0.0.0.0:8000" ]