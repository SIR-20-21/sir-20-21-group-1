class Story:
    """
    Represents an possibly interaction story including parts, that are only told by the robots and parts that require the human to give answers.
    """

    def __init__(self):
        """
        :return:
        """
        # allows you to directly jump to a storypart
        self.initial_id = "q1"

        # This is the actual story
        # Each Storypart needs an ID, a content_type and the content.
        # The ID is for unique identification and is used to indicate the following storypart.
        # The content_type can be one of (question, choice, storypart)
        # The content depends on the content_type:
        #   question    -> (text/question, intent_name)
        #   choice      -> text/question
        #   storypart   -> text
        # Optionally, there can be a follow_id. If none is provided, the story ends after this part.
        #   If the follow_id is a string, then this determines the next storypart
        #   If the follow_id is a dictionary, the values represent the possible options for the following part depending on the users choice

        self.story = {
            "q1": Storypart(id="q1", content_type="question", content=("What is your name?", "answer_name"), follow_id="q2"),
            "q4": Storypart(id="q4", content_type="choice", content="Do you want to go left or right?", follow_id={0: "q2", 1: "q3"}),
            "q2": Storypart(id="q2", content_type="question", content=("How old are you?", "answer_age"), follow_id="q3"),
            "q3": Storypart(id="q3", content_type="question", content=("Do you want to hear a cool story?", "answer_decision"), follow_id="p1"),
            "p1": Storypart(id="p1", content_type="storypart", content="Cool {0}, since you are {1} years older than me, you probably know more than I do.", follow_id="q4")
        }

    def getFollowUp(self, storypart=None, branch_option: str = None):
        """
        Get the next part of the story depending on the current part and the user's choice.
        :param storypart: The current part of the story that has already been processed
        :param branch_option: the branching option chosen by the user
        :return: The next storypart to be processed 
        """

        if storypart is not None:
            if self.story[storypart.id].follow_id is not None:
                if type(self.story[storypart.id].follow_id) is str:
                    return self.story[self.story[storypart.id].follow_id]
                elif type(self.story[storypart.id].follow_id) is dict:
                    return self.story[self.story[storypart.id].follow_id[branch_option]]

            return None
        else:
            return self.story[self.initial_id]

        return None


class Storypart:
    """
    Represents a part of a story (e.g. a question or just text) that can include, text or gestures and can require human feedback.
    """

    def __init__(self, id: str, content_type: str, content, gesture: str = None, follow_id=None):
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
        self.follow_id = follow_id

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
            return text


class StoryIterator():
    '''
    Iterator class for a story
    '''

    def __init__(self, story):
        self.story = story
        self._index = "q1"

    def __next__(self):
        if self.story[self._index] is not None:
            if type(self.story[self._index]) is str:
                current_part = self.story[self._index]
                self._index = self.story[self._index].follow_id
                return current_part
            # elif type(self.story[self._index]) is dict:

        raise StopIteration
