class AnonymousSurvey:
    """收集调查文件答案"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey Results: ")
        for response in self.responses:
            print('- ', response)
