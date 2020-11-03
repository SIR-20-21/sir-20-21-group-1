class Story:

    def __init__(self):
        self.story = [
            {"id": "q1", "type": "question", "content": ("What is your name?", "answer_name")}, 
            {"id": "q2", "type": "question", "content": ("How old are you?", "answer_age")}, 
            {"id": "q3", "type": "question", "content": ("Do you want to hear a cool story?", "answer_decision")},
            {"id": "p1", "type": "storypart", "content": "Cool {0}, since you are {1} years older than me, you probably know more than I do."}
        ]


    def __iter__(self):
        return StoryIterator(self.story)

    def format(self, text, user_model, story_part):
        if story_part == "p1":
            return text.format(user_model["name"], str(int(user_model["age"] - 5)))
        else:
            return ""

class StoryIterator():
    '''
    Iterator class
    '''
    def __init__(self, story):
        self.story = story
        self._index = 0

    def __next__(self):
        if self._index < len(self.story):
            current_part = self.story[self._index]
            self._index += 1

            return current_part
        
        raise StopIteration

    