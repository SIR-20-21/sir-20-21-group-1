from conversation import Motion, MOVEMENT_TYPE
from social_interaction_cloud.basic_connector import RobotPosture

class Story:
    """
    Represents an possibly interaction story including parts, that are only told by the robots and parts that require the human to give answers.
    """

    def __init__(self):
        """
        :return:
        """
        # allows you to directly jump to a storypart
        self.initial_id = "d7"

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
            ########################## TEST PARTS ######################
            "d0": Storypart(id="d0", content_type="storypart", content="", movement=RobotPosture.STAND, movement_type=MOVEMENT_TYPE.POSTURE, follow_id="s1"),
            "q1": Storypart(id="q1", content_type="question", content=("What is your name?", "answer_name"), follow_id="q2"),
            "q4": Storypart(id="q4", content_type="choice", content="Do you want to go left or right?", follow_id={0: "q2", 1: "q3"}),
            "q2": Storypart(id="q2", content_type="question", content=("How old are you?", "answer_age"), follow_id="p1"),
            "q3": Storypart(id="q3", content_type="question", content=("Do you want to hear a cool story?", "answer_decision"), follow_id="d4"),
            "p1": Storypart(id="p1", content_type="storypart", content="Cool {0}, since you are {1} years older than me, you probably know more than I do.", follow_id="q4"),
            ############################################################

            # Maybe add an ending option?
            "s1": Storypart(id="s1", content_type="storypart", content="Thank you for helping me!"),
            #
            "d1": Storypart(id="d1", content_type="storypart", content="Hi, my name is NAO Holmes and it is really nice to meet you, {0}.", follow_id="d2"),
            "d2": Storypart(id="d2", content_type="choice", content="I’m going to solve a very interesting mystery today. Would you like to join me?", follow_id={0: "s1", 1: "d3"}),
            "d3": Storypart(id="d3", content_type="storypart", content="Okay cool, from now on you will be my personal detective!", follow_id="d4"),
            "d4": Storypart(id="d4", content_type="storypart", content="So the following happened this morning: 'By 7 a.m. this morning I rolled out of bed straight to the kitchen to make myself a royal breakfast, because I was hungry as a bear. Suddenly, I noticed something very odd: all the bananas that I bought yesterday and were placed in the ceramic bowl on my wooden table were gone. Hastily, I ran to the hallway when suddenly I slipped on a peeled banana. Before I knew it was laying on the ground like this", follow_id="d4a"),
            "d4a": Storypart(id="d4a", content_type="storypart", content="", movement=RobotPosture.LYINGBACK, movement_type=MOVEMENT_TYPE.POSTURE, follow_id="d5"),
            #Added line for inbetween falling and getting up
            "d5": Storypart(id="d5", content_type="storypart", content="Ouch! I looked around in chock, I certainly did not put this banana here.", follow_id="d5a"),
            "d5a": Storypart(id="d5a", content_type="storypart", content="", movement=RobotPosture.STAND, movement_type=MOVEMENT_TYPE.POSTURE, follow_id="d6"),
            "d6": Storypart(id="d6", content_type="storypart", content="I slipped on my detective trench coat over my blue striped pyjamas, put on my fedora, and began my investigation.", follow_id="d7"),

            #Edit this follow. Should this not possible be able to lead to multiple options? Correct and false? Maybe even can't understand you or should I repeat my question?
            # TODO insert stair gesture below
            "d7": Storypart(id="d7", content_type="storypart", content="First, I wanted to check the rooms upstairs. I flew up the stairs", movement=None, movement_type=None, follow_id="d7a"),
            "d7a": Storypart(id="d7a", content_type="question", content=("{0} How many steps does my staircase have in total?", "answer_math_question", "24"), follow_id={0: "d8a", 1: "d8b"}),
            "d8a": Storypart(id="d8a", content_type="storypart", content="Sorry, it was 24 steps. But good try, though!", follow_id="d9"),
            "d8b": Storypart(id="d8b", content_type="storypart", content="Well done! 24 steps indeed!", follow_id="d9"),

            #This will probably be an eventlistener or something, do we need to create an separate content_type for it?
            "d9": Storypart(id="d9", content_type="storypart", content="Give me a high five!", movement=Motion().left_arm_highfive, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d10"),
            "d10": Storypart(id="d10", content_type="storypart", content="Back to the top of the stairs. Standing there in the corridor I had to make a very very difficult choice. On my left I heard a strange thumping sound and on my right I heard something that sounded like a trumpet", follow_id="d11"),

            #Currently a fake choice, could change this later
            "d11": Storypart(id="d11", content_type="choice", content="Where would you have gone? Left or right?", follow_id={0: "d12a", 1: "d12b"}),
            "d12a": Storypart(id="d12a", content_type="storypart", content="Yes very good, that is where I went as well!", follow_id="d13"),
            "d12b": Storypart(id="d12b", content_type="storypart", content="Very good thinking, but I chose to go to the right and investigate the trumpet sounds.", follow_id="d13"),
            "d13": Storypart(id="d13", content_type="storypart", content="“I took out my magnifying glass, which I always have in my pocket for such occasions. Leaning close to the floor, I could see enormous footprints going all the way to my bathroom. Curious. I made my way to the bathroom, where I thought I heard rustling and water continuously dripping on the bathroom tiles.", follow_id="d14"),
            "d14": Storypart(id="d14", content_type="storypart", content="I crept quietly towards the bathroom door, trying not to make a sound.", follow_id="d15"),

            #This should be a sound effect
            "d15": Storypart(id="d15", content_type="storypart", content="Sssssssstttt", follow_id="d16"),
            "d16": Storypart(id="d16", content_type="storypart", content="I opened the door in one movement and looked inside.", follow_id="d17"),

            #Should complete soundeffects also be a storypart?
            "d17": Storypart(id="d17", content_type="storypart", content="There was no one or nothing inside the bathroom, so I casually walked in.", follow_id="d18"),
            "d18": Storypart(id="d18", content_type="storypart", content="Maybe I just imagined the sounds.", follow_id="d19"),

            #BATHROOM SCENE STARTS HERE
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

        else:
            return self.story[self.initial_id]

        return None



class Storypart:
    """
    Represents a part of a story (e.g. a question or just text) that can include, text or gestures and can require human feedback.
    """

    def __init__(self, id: str, content_type: str, content, movement: str = None, movement_type: MOVEMENT_TYPE = None, soundfile: str = None, follow_id=None):
        """
        :param id: Identification of storypart (str)
        :param content_type: Determines whether human feedback is needed or not. (str)
        :param content: Contains text and depending on the content_type also the dialogflow intent
        :param movement: movement to be executed during speech (str)
        """
        self.id = id
        self.type = content_type
        self.content = content
        self.movement = movement
        self.movement_type = movement_type
        self.soundfile = soundfile
        self.follow_id = follow_id

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
        ###########
        # LIST ALL STORYPARTS HERE THAT NEED INFORMATION FROM THE USER MODEL OR OTHER INFORMATION INSERTED
        ###########
        # example for math question depending on user age
        elif story_part_id == "d7a":
            if user_model["age"] < 9:
                return text.format("taking two steps at a time. In total, I had to take 12 steps.")
            else:
                return text.format("and had to take 3 steps times 8 to get to the first floor.")
        else:
            return text
