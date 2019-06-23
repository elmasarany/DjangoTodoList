from rest_framework.test import APITestCase, APIClient

from todolist.models import TodoItem


class TodoLIstApi(APITestCase):
    def testCreateTodo(self):
        self.client = APIClient()
        response = self.client.post("api/v1/createTodo", {"title": "todo item title"})
        self.assertEqual("201", response.status_code)
        todo_item = TodoItem.objects.get(title="todo item title")
        self.assertEquals("todo item title", todo_item.title)
