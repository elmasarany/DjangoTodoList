from django.db.models import Model, CharField


class TodoItem(Model):
    title = CharField(max_length=200)

