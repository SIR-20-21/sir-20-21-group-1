from conversation import Motion, MOVEMENT_TYPE
from social_interaction_cloud.basic_connector import RobotPosture

class Story:
    """
    Represents an possibly interaction story including parts, that are only told by the robots and parts that require the human to give answers.
    """

    def __init__(self, interactive : bool = True):
        """https://github.com/SIR-20-21/sir-20-21-group-1
        :return:
        """
        # allows you to directly jump to a storypart
        self.initial_id = "d1"

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

        if interactive:
            self.story = {
                # ENDING OPTION
                "s1": Storypart(id="s1", content_type="storypart", content="Thank you for helping me!"),
                #
                "d1": Storypart(id="d1", content_type="storypart", content="Hi, my name is Nao Holmes and it is really nice to meet you, {0}.", follow_id="d2"),
                "d2": Storypart(id="d2", content_type="storypart", content="I’m going to solve a very interesting mystery today. Would you like to join me?", follow_id='d2a'),
                "d2a": Storypart(id="d2a", content_type="choice", content="Touch my left for yes, and my right for no.", movement=Motion().right_left ,movement_type=MOVEMENT_TYPE.MOTION,follow_id={0: "s1", 1: "d3"}),
                #EXPLAIN THE HAND MOVEMENT
                "d3": Storypart(id="d3", content_type="storypart", content="Okay cool, from now on you will be my personal detective!", follow_id="d4"),
                "d4": Storypart(id="d4", content_type="storypart", content="This story is called the Banana mystery. So the following happened this morning: 'By 7 a.m. I rolled out of bed straight to the kitchen to make myself a breakfast. Suddenly, I noticed something very odd: all the bananas that I bought yesterday were gone. I ran to the hallway when suddenly I slipped on a peeled banana. Before I knew it was laying on the floor like this", follow_id="d4a"),
                "d4a": Storypart(id="d4a", content_type="storypart", content="", movement=RobotPosture.LYINGBACK, movement_type=MOVEMENT_TYPE.POSTURE, follow_id="d5"),
                "d5": Storypart(id="d5", content_type="storypart", content="Ouch! I certainly did not put this banana here.", follow_id="d5a"),
                "d5a": Storypart(id="d5a", content_type="storypart", content="", movement=RobotPosture.STAND, movement_type=MOVEMENT_TYPE.POSTURE, follow_id="d6"),
                "d6": Storypart(id="d6", content_type="storypart", content="I slipped on my detective trench coat over my blue striped pyjamas, put on my fedora, and began my investigation.", soundfile='sounds/detective.wav', follow_id="d7"),
                
                "d7": Storypart(id="d7", content_type="storypart", content="First, I wanted to check the rooms upstairs. I flew up the stairs", movement=Motion().walking, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d7a"),
                "d7a": Storypart(id="d7a", content_type="question", content=("{0} How many steps does my staircase have in total?", "answer_math_question", "24"), follow_id={0: "d8a", 1: "d8b"}),
                "d8a": Storypart(id="d8a", content_type="storypart", content="Sorry, it was 24 steps. But good try, though!", follow_id="d9"),
                "d8b": Storypart(id="d8b", content_type="storypart", content="Well done! 24 steps indeed!", follow_id="d10a"),

                # "d9": Storypart(id="d9", content_type="highfive", content="Give me a high five!", follow_id="d10a"),
                "d10a": Storypart(id="d10a", content_type="storypart", content="Back to the top of the stairs. Standing there in the corridor, I needed to take action.", follow_id="d10b"),
                "d10b": Storypart(id="d10b", content_type="storypart", content="On my right I heard something that sounded like a trumpet", soundfile="sounds/trumpet.wav", follow_id="d13"),

                "d13": Storypart(id="d13", content_type="storypart", content="Leaning close to the floor, I could see enormous footprints going all the way to my bathroom. Curious. I made my way to the bathroom, where I thought I heard water continuously dripping on the bathroom tiles.", soundfile="sounds/water.wav", follow_id="d14"),
                "d14": Storypart(id="d14", content_type="storypart", content="I crept quietly towards the bathroom door, trying not to make a sound.", soundfile="sounds/tiptoe.wav", follow_id="d15"),

                "d15": Storypart(id="d15", content_type="storypart", content="", soundfile="sounds/sssshh.wav", follow_id="d16"),
                "d16": Storypart(id="d16", content_type="storypart", content="I opened the door in one movement and looked inside.", follow_id="d17"),

                "d16a": Storypart(id="d16a", content_type="storypart", content="", soundfile="sounds/scary.wav", follow_id="d17"),
                
                "d17": Storypart(id="d17", content_type="storypart", content="The bathroom was empty, so I walked in.", movement=Motion().walking, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d18"),
                "d18": Storypart(id="d18", content_type="storypart", content="Maybe I just imagined the sounds.", follow_id="d20"),

                #BATHROOM SCENE STARTS HERE
                "d20": Storypart(id="d20", content_type="storypart", content="While I was looking in the mirror I noticed that there was an elephant standing in the shower.", movement="elephant_motion-4d89bf/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d21"),
                "d21": Storypart(id="d21", content_type="storypart", content="The elephant could be the one that ate all my bananas, but then I remembered that elephants don’t eat bananas.", follow_id="d22"),
                "d22": Storypart(id="d22", content_type="question", content=("{0}, {1}","{0}", "{0}"), follow_id= {0: "d23a", 1: "d23b"}),

                "d23a": Storypart(id="d23a", content_type="storypart", content="No, unfortunately {0} is not correct. {1}", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d24"),
                "d23b": Storypart(id="d23b", content_type="storypart", content="Yes, very good! {0}", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d24"),
                "d24": Storypart(id="d24", content_type="storypart", content="Just to be sure, I asked the elephant if he wanted to have a banana, but he kindly refused", movement='animations/Stand/Gestures/No_8', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d25"),
                "d25": Storypart(id="d25", content_type="storypart", content="Where shall we go now?", follow_id="d26"),
                "d26": Storypart(id="d26", content_type="choice", content="Do you want to keep looking inside in some other rooms or go outside to investigate there?", follow_id={0: "d38", 1: "d62"}), 
                #BATHROOM SCENE ENDS HERE, GO TO D27(ROOM) OR D38(GARDEN)
                
                
                #GARDEN SCENE STARTS HERE, insert birds sounds
                "d38": Storypart(id="d38", content_type="storypart", content="When I stepped into the garden I heard a lot of birds.", soundfile="sounds/birds.wav", follow_id="d39"),
                "d39": Storypart(id="d39", content_type="storypart", content="In the middle of the garden there was a tree full of 40 parakeets", movement="flying-be9ea3/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d40"),            
                "d40": Storypart(id="d40", content_type="storypart", content="Half of the parakeets were green and the other half was red.", follow_id="d41"),
                "d41": Storypart(id="d41", content_type="question", content=("{0}, {1}", "answer_math_question", "{0}"), follow_id={0: "d42a", 1: "d42b"}),
                "d42a": Storypart(id="d42a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. {0}", follow_id="d43"),
                "d42b": Storypart(id="d42b", content_type="storypart", content="Excellent! The correct answer is indeed {0}.", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d43"),

                "d43": Storypart(id="d43", content_type="storypart", content="After looking around in the garden I saw that the backdoor was unlocked with dirty footprints on the door.", follow_id="d44"),
                "d44": Storypart(id="d44", content_type="storypart", content="I decided to follow the footprints, but the track continued on the roof.", follow_id="d45"),
                "d45": Storypart(id="d45", content_type="question", content=("{0}, what item could I use to get on the roof?","answer_roof_question", "ladder"), follow_id= {0: "d46a", 1: "d46b"}),
                "d46a": Storypart(id="d46a", content_type="storypart", content="No, unfortunately that is not correct, but still a very good try. We will be using a ladder.", follow_id="d47"),
                "d46b": Storypart(id="d46b", content_type="storypart", content="Smart thinking, we will indeed use a ladder.", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d47"),
                
                "d47": Storypart(id="d47", content_type="storypart", content="I climbed the ladder and got on the roof.", movement="climbing-db5359/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d48"),
                "d48": Storypart(id="d48", content_type="storypart", content="I noticed that the window of my room was standing wide open.", follow_id="d49"),            
                "d49": Storypart(id="d49", content_type="storypart", content="That must be the reason why it was so cold tonight.", movement="shivering-f5eafc/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d52"),            
                # "d50": Storypart(id="d50", content_type="storypart", content="where do we go now?", follow_id="d51"),            
                # "d51": Storypart(id="d51", content_type="choice", content="Do we get back off the roof, or do we climb into the room?", follow_id={0: "d52", 1: "d53"}), 
                #back of the roof (d52) leads to room with 1 extra storypart
                "d52": Storypart(id="d52", content_type="storypart", content="I climbed off the ladder and quickly entered my house and went upstairs to my room.", movement="climbing-db5359/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d62"),
                #END OF GARDEN SCENE 


                #START ATTIC SCENE 

                "d62": Storypart(id="d62", content_type="storypart", content="Back in my room, I looked up and saw the rope that leads to the attic, also known as my secret hiding spot and investigation headquarters", movement="point_up-d42859/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d63"),
                "d63": Storypart(id="d63", content_type="storypart", content="Pulling on the rope, the stairs to the attic flipped out", movement="pulling-c35961/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d64"),
                "d64": Storypart(id="d64", content_type="storypart", content="On the stairs to the attic I found again a banana peel, but this time I was more careful.", follow_id="d65"),
                "d65": Storypart(id="d65", content_type="storypart", content="When I arrived at the attic, I smelled something weird, so I entered carefully", movement=Motion().looking_around_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d68"),

                "d68": Storypart(id="d68", content_type="storypart", content="I turned on the lights and in front of me I saw a very big and hairy monkey with some bright disco trousers on.", soundfile="sounds/monkey.wav", movement='gorilla_motion-3ce914/behavior_1', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d69"),
                "d69": Storypart(id="d69", content_type="storypart", content="The monkey was dancing, while juggling with three bananas.", movement="juggling-7a4d8b/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d70"),
                "d70": Storypart(id="d70", content_type="storypart", content="{0}, I think we found the thief who stole my breakfast!", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d71"),
            
                #CLOSING SCENE 
                "d71": Storypart(id="d71", content_type="storypart", content="Then it came to me", follow_id="d72"),           
                "d72": Storypart(id="d72", content_type="question", content=("What place has monkeys, elephants and parakeets and could have been in town this whole week?","answer_circus_question", "circus"), follow_id={0: "d73a", 1: "d73b"}), 
                "d73a": Storypart(id="d73a", content_type="storypart", content="Yes the circus is in town!", soundfile="sounds/circus.wav", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d74"),
                "d73b": Storypart(id="d73b", content_type="storypart", content="No, the circus is in town!", soundfile="sounds/circus.wav", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d74"),
                "d74": Storypart(id="d74", content_type="storypart", content="Would you like to do a funky monkey dance with me?", follow_id="d74a"), 
                "d74a": Storypart(id="d74a", content_type="choice", content="Touch my left arm to dance with me or my right arm to quit.", follow_id={0: "d75a", 1: "d76"}),
                
                #YES
                # TODO insert disco sound
                "d76": Storypart(id="d76", content_type="storypart", content="Disco time!", soundfile="sounds/disco.wav", movement='disco_dance-eb402b/behavior_1', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d75a"),

                #NO
                "d75a": Storypart(id="d75a", content_type="storypart", content="Alright, thank you for participating and being my help detective for today", follow_id="d75b"),           
                "d75b": Storypart(id="d75b", content_type="storypart", content="See you next time, detective {0}", movement='animations/Stand/Gestures/Hey_1', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="s1"),
            }
        
        else:

            self.story = {            
                "d1": Storypart(id="d1", content_type="storypart", content="Hi, my name is Nao Holmes", follow_id="d2"),
                "d2": Storypart(id="d2", content_type="storypart", content="I’m going to solve a very interesting mystery today", follow_id="d3"),
                "d3": Storypart(id="d3", content_type="storypart", content="So the following happened this morning: 'By 7 a.m. I rolled out of bed straight to the kitchen to make myself breakfast, because I was hungry as a bear. Suddenly, I noticed something very odd: all the bananas that I bought yesterday and were placed in the bowl on my wooden table were gone. While in a hurry, I ran to the hallway when suddenly I slipped on a peeled banana. Before I knew it was laying on the ground", follow_id="d4"),
                "d4": Storypart(id="d4", content_type="storypart", content="I looked around in shock, I certainly did not put this banana here.", follow_id="d5"),
                "d5": Storypart(id="d5", content_type="storypart", content="I slipped on my detective trench coat over my blue striped pyjamas, put on my fedora, and began my investigation.", follow_id="d6"),
                "d6": Storypart(id="d6", content_type="storypart", content="First, I wanted to check the rooms upstairs. So I flew up the stairs", follow_id="d7"),
                "d7": Storypart(id="d7", content_type="storypart", content="On the top of the stairs I had to make a very difficult choice. On my left I heard a strange thumping sound.", follow_id="d8"),
                "d8": Storypart(id="d8", content_type="storypart", content="and on my right I heard something that sounded like a trumpet", follow_id="d9"),
                "d9": Storypart(id="d9", content_type="storypart", content="I chose to go to the right and investigate the trumpet sounds.", follow_id="d10"),
                "d10": Storypart(id="d10", content_type="storypart", content="I took out my magnifying glass, which I always have in my pocket for such occasions. Leaning close to the floor, I could see enormous footprints going all the way to my bathroom. Curious. I made my way to the bathroom, where I thought I heard rustling and water continuously dripping on the bathroom tiles.", follow_id="d11"),
                "d11": Storypart(id="d11", content_type="storypart", content="I crept quietly towards the bathroom door, trying not to make a sound.", follow_id="d12"),
                "d12": Storypart(id="d12", content_type="storypart", content="I opened the door in one movement and looked inside.", follow_id="d13"),
                "d13": Storypart(id="d13", content_type="storypart", content="The bathroom was empty, so I casually walked in.", follow_id="d14"),
                "d14": Storypart(id="d14", content_type="storypart", content="Maybe I just imagined the sounds.", follow_id="d15"),
                "d15": Storypart(id="d15", content_type="storypart", content="In the bathroom I threw some water in my face to refresh myself.", follow_id="d16"),
                "d16": Storypart(id="d16", content_type="storypart", content="While I was looking in the mirror I noticed that there was an elephant standing in the shower.", follow_id="d17"),
                "d17": Storypart(id="d17", content_type="storypart", content="The elephant could be the one that ate all my bananas, but then I remembered that elephants don’t eat bananas.", follow_id="d18"),
                "d18": Storypart(id="d18", content_type="storypart", content="Just to be sure, I asked the elephant if he wanted to have a banana, but he kindly refused", follow_id="d19"),
                "d19": Storypart(id="d19", content_type="storypart", content="I had enough information, so I went to another room to continue my investigation.", follow_id="d20"),
                "d20": Storypart(id="d20", content_type="choice", content="I strode to the walk-in closet since I saw that the door was ajar", follow_id="d21"),
                "d21": Storypart(id="d21", content_type="storypart", content="So, after a quick investigation inside my favorite hiding place, I decided to go outside to investigate there.", follow_id="d22"),
                "d22": Storypart(id="d22", content_type="storypart", content="I was in desperate need of some fresh air.", follow_id="d23"),
                "d23": Storypart(id="d23", content_type="storypart", content="When I stepped into the garden I heard a lot of birds.", follow_id="d24"),
                "d24": Storypart(id="d24", content_type="storypart", content="In the middle of the garden there was a tree full of 40 parakeets", follow_id="d25"),
                "d25": Storypart(id="d25", content_type="storypart", content="Half of the parakeets were green and the other half was red.", follow_id="d26"),
                "d26": Storypart(id="d26", content_type="storypart", content="After looking around in the garden I saw that the backdoor was unlocked with dirty footprints on the door, which reminded me of a human, but a little bit different", follow_id="d27"),
                "d27": Storypart(id="d27", content_type="storypart", content="I decided to follow the footprints, but the track continued on the roof.", follow_id="d28"),
                "d28": Storypart(id="d28", content_type="storypart", content="I climbed the ladder and got on the roof.", follow_id="d29"),
                "d29": Storypart(id="d29", content_type="storypart", content="I noticed that the window of my room was standing wide open", follow_id="d30"),
                "d30": Storypart(id="d30", content_type="storypart", content="That must be the reason why it was so cold tonight", follow_id="d31"),
                "d31": Storypart(id="d31", content_type="storypart", content="I entered my own room, where I was sleeping just an hour ago", follow_id="d32"),
                "d32": Storypart(id="d32", content_type="storypart", content="I walked straight to my hamsters cage to see how Hamtaro was doing", follow_id="d33"),
                "d33": Storypart(id="d33", content_type="storypart", content="I opened the cage and I looked directly into the feeding bowl of my very old hamster, was it possible that he ate my bananas?", follow_id="d34"),
                "d34": Storypart(id="d34", content_type="storypart", content="I hadn’t fed him for 2 days, maybe he was extremely hungry", follow_id="d35"),
                "d35": Storypart(id="d35", content_type="storypart", content="I grabbed my hamster Hamtaro and looked at him", follow_id="d36"),
                "d36": Storypart(id="d36", content_type="storypart", content="Hamtaro was half the size of an actual banana, he couldn’t be the one who ate all my bananas", follow_id="d37"),
                "d37": Storypart(id="d37", content_type="storypart", content="Also the cage was closed when I arrived", follow_id="d38"),
                "d38": Storypart(id="d38", content_type="storypart", content="I gave Hamtaro something to eat and after looking further around in my room I detected nothing suspicious", follow_id="d39"),
                "d39": Storypart(id="d39", content_type="storypart", content="Then all the sudden a freshly peeled banana felt on my head", follow_id="d40"),
                "d40": Storypart(id="d40", content_type="storypart", content="I looked up and saw another banana dangling on the rope that leads to the attic, also known as my secret hiding spot and investigation headquarters", follow_id="d41"),
                "d41": Storypart(id="d41", content_type="storypart", content="Pulling on the rope, the stairs to the attic flipped out", follow_id="d42"),
                "d42": Storypart(id="d42", content_type="storypart", content="On the stairs to the attic I found again a banana peel, but this time I was more careful.", follow_id="d43"),
                "d43": Storypart(id="d43", content_type="storypart", content="When I arrived at the attic, I smelled something weird, so I entered carefully", follow_id="d44"),
                "d44": Storypart(id="d44", content_type="storypart", content="The first thing I had to do was to find the light switch, since the attic was completely dark and I didn’t want to slip on a banana again", follow_id="d45"),
                "d45": Storypart(id="d45", content_type="storypart", content="I turned on the lights with my right hand",  follow_id="d46"),
                "d46": Storypart(id="d46", content_type="storypart", content="And in front of me I saw a very big, hairy and funky looking monkey with some bright disco trousers on.", follow_id="d47"),
                "d47": Storypart(id="d47", content_type="storypart", content="The monkey was dancing, while juggling with three bananas.", follow_id="d48"),
                "d48": Storypart(id="d48", content_type="storypart", content="I think I found the thief who stole my breakfast!", follow_id="d49"),
                "d49": Storypart(id="d49", content_type="storypart", content="Then it came to me", follow_id="d50"),
                "d50": Storypart(id="d50", content_type="storypart", content="The circus is in town!", follow_id="d51"),
                "d51": Storypart(id="d51", content_type="storypart", content="That was the end of the story, thankyou for listening"),            
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
                    if branch_option is None:
                        branch_option = 0
                    return self.story[self.story[storypart.id].follow_id[branch_option]]

        else:
            return self.story[self.initial_id]

        return None



class Storypart:
    """
    Represents a part of a story (e.g. a question or just text) that can include, text or gestures and can require human feedback.
    """

    def __init__(self, id: str, content_type: str, content, movement: str = None, movement_type: MOVEMENT_TYPE = None, eye_color: str = None, soundfile: str = None, follow_id=None):
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
        self.eye_color = eye_color
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
        elif story_part_id == "d1":
            if user_model["name"] == '':
                return text.format("My friend")
            return text.format(user_model["name"])

        elif story_part_id == "d7a":
            if user_model["age"] < 9:
                return text.format("taking two steps at a time. In total, I had to take 12 steps.")
            else:
                return text.format("and had to take 3 steps times 8 to get to the first floor.")

        elif story_part_id == "d22":
            if user_model["age"] < 9:
                return text.format(user_model["name"] if user_model["name"] != '' else "My friend", "what is the favourite food of an elephant: chocolate or peanuts?")
            else:
                return text.format(user_model["name"] if user_model["name"] != '' else "My friend", "How much grass and leaves does an elephant consume every day: 150 kilograms or 15 kilograms?")
        
        elif story_part_id == "answer_d22":
            if user_model["age"] < 9:
                return text.format("peanuts")
            else:
                return text.format("150")

        elif story_part_id == "intent_d22":
            if user_model["age"] < 9:
                return text.format("answer_food_question")
            else:
                return text.format("answer_food_question_hard")       

        elif story_part_id == "d23a":
            if user_model["age"] < 9:
                return text.format("chocolate", "Elephants eat a lot of peanuts!")
            else:
                return text.format("15 kilograms", "An elephants can eat 150 kilograms of gras and leaves per day!")

        elif story_part_id == "d23b":
            if user_model["age"] < 9:
                return text.format("Elephants eat a lot of peanuts!")
            else:
                return text.format("An elephants can eat 150 kilograms of gras and leaves per day!")

        elif story_part_id == "d30":
            if user_model["age"] < 9:
                return text.format(user_model["name"] if user_model["name"] != '' else "My friend", "what color do you get when you mix the colors blue and yellow?")
            else:
                return text.format(user_model["name"] if user_model["name"] != '' else "My friend", "what is the opposite color of the color red?")

        elif story_part_id == "d31a":
            if user_model["age"] < 9:
                return text.format("When you mix the colors blue and red you will get green.")
            else:
                return text.format("The opposite color of red, which is called a complementary color, is the color green.")

        elif story_part_id == "d32":
            if user_model["age"] < 9:
                return text.format("And what happens if you mix the colors yellow and red?")
            else:
                return text.format("And what is the opposite color of the color blue?")

        elif story_part_id == "d33a":
            if user_model["age"] < 9:
                return text.format("When you mix the colors yellow and red you will get orange.")
            else:
                return text.format("The complementary color of blue, is the color orange.")

        elif story_part_id == "d41":
            if user_model["age"] < 9:
                return text.format(user_model["name"], "How many red parakeets were in the tree?")
            else:
                return text.format(user_model["name"], "how many green parakeets were left in the tree, if a quarter of the green parakeets flew away?")

        elif story_part_id == "answer_d41":
            if user_model["age"] < 9:
                return text.format("20")
            else:
                return text.format("15")

        elif story_part_id == "d42a":
            if user_model["age"] < 9:
                return text.format("There were 20 red parakeets in the tree.")
            else:
                return text.format("there were 15 green parakeets in the tree left.")
        
        elif story_part_id == "d42b":
            if user_model["age"] < 9:
                return text.format("20")
            else:
                return text.format("15")

        elif story_part_id == "d45":
            if user_model["name"] == '':
                return text.format("My friend")
            return text.format(user_model["name"])

        elif story_part_id == "d56":
            if user_model["age"] < 9:
                return text.format("My hamster is 10 years older than you " + user_model["name"] + ", how old is my hamster?")
            else:
                return text.format("My hamster is 3 times older than you " + user_model["name"] + ", how old is my hamster?")

        elif story_part_id == "answer_d56":
            if user_model["age"] < 9:
                return text.format(str(int(user_model["age"] + 10)))
            else:
                return text.format(str(int(user_model["age"] * 3)))

        elif story_part_id == "d57a":
            if user_model["age"] < 9:
                return text.format(str(int(user_model["age"] + 10)))
            else:
                return text.format(str(int(user_model["age"] * 3)))
        
        elif story_part_id == "d70":
            if user_model["name"] == '':
                return text.format("My friend")
            return text.format(user_model["name"])

        elif story_part_id == "d75b":
            if user_model["name"] == '':
                return text.format("My friend")
            return text.format(user_model["name"])
            
        else:
            return text
