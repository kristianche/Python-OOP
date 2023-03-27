class Task:

    def __init__(self, name: str, due_date: str, ):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name == self.name:
            return "Name cannot be the same."

        self.name = new_name
        return f"{new_name}"

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        try:
            self.comments[comment_number] = new_comment
            return f"{', '.join(self.comments)}"
        except IndexError:
            return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
