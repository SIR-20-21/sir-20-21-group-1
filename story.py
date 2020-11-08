class Story:
    """
    Represents an possibly interaction story including parts, that are only told by the robots and parts that require the human to give answers.
    """
    def __init__(self):
        """
        :return:
        """
        self.story = [
            Storypart("q1", "question", ("What is your name?", "answer_name")), 
            Storypart("q2", "question", ("How old are you?", "answer_age")),
            Storypart("q3", "question", ("Do you want to hear a cool story?", "answer_decision")),
            Storypart("p1", "storypart", "Cool {0}, since you are {1} years older than me, you probably know more than I do.")
        ]

    def __iter__(self) -> StoryIterator:
        """
        :return: Interator object
        """
        return StoryIterator(self.story)
    
class Storypart:
    """
    Represents a part of a story (e.g. a question or just text) that can include, text or gestures and can require human feedback.
    """
    def __init__(self, id: str, content_type: str, content, gesture: str = None):
        """
        :param id: Identification of storypart (str)
        :param content_type: Determines whether human feedback is needed or not. (str)
        :param content: Contains text and depending on the content_type also the dialogflow intent
        :param gesture: Gesture to be executed during speech (str)
        """
        self.id = id
        self.type = content_type
        self.content = content
        self.gesture = gesture

    def hasGesture(self) -> bool:
        """
        Check whether a gesture is registered with this storypart.
        :return: True, if a gesture has been registered (bool)
        """
        return self.gesture is not None

    @staticmethod
    def format(text, user_model, story_part_id) -> str:
        """
        Formats a given text for the specified storypart and fills it with information from the user model.
        :param text: Text to be formatted (str)
        :param user_model: Model of the current user to retrieve the information from.
        :param story_part_id: ID of the storypart, used to determine which information need to be filled in.
        :return: Formatted string (str)
        """
        if story_part_id == "p1":
            return text.format(user_model["name"], str(int(user_model["age"] - 5)))
        else:
            return ""

class StoryIterator():
    '''
    Iterator class for a story
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

    