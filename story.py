from conversation import Motion, MOVEMENT_TYPE
from social_interaction_cloud.basic_connector import RobotPosture

class Story:
    """
    Represents an possibly interaction story including parts, that are only told by the robots and parts that require the human to give answers.
    """

    def __init__(self):
        """https://github.com/SIR-20-21/sir-20-21-group-1
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
            
            
            #EASY STORY

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
            
            #insert thrilling detective sound
            
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

            #insert scary sounds
            
            #Should complete soundeffects also be a storypart?
            "d17": Storypart(id="d17", content_type="storypart", content="There was no one or nothing inside the bathroom, so I casually walked in.", follow_id="d18"),
            "d18": Storypart(id="d18", content_type="storypart", content="Maybe I just imagined the sounds.", follow_id="d19"),

            #BATHROOM SCENE STARTS HERE
            "d19": Storypart(id="d19", content_type="storypart", content="In the bathroom I threw some water in my face to refresh myself.", movement=Motion().face_wash_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d20"),
            "d20": Storypart(id="d20", content_type="storypart", content="While I was looking in the mirror I noticed that there was an elephant standing in the shower.", movement=Motion().elephant_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d21"),
            "d21": Storypart(id="d21", content_type="storypart", content="The elephant could be the one that ate all my bananas, but then I remembered that elephants don’t eat bananas.", follow_id="d22"),
            "d22": Storypart(id="d22", content_type="question", content=("{0}, what is the favourite food of an elephant: chocolate or peanuts?","answer_food_question", "peanuts"), follow_id= {0: "d23a", 1: "d23b"}),
            
            #maybe add interaction momement with touching NAO's hands?
            
            "d23a": Storypart(id="d23a", content_type="storypart", content="No, unfortunately chocolate is not correct. Elephants eat a lot of peanuts!", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="24"),
            "d23b": Storypart(id="d23b", content_type="storypart", content="Yes, very good! ELephants eat a lot of peanuts!", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="24"),
            "d24": Storypart(id="d24", content_type="storypart", content="Just to be sure, I asked the elephant if he wanted to have a banana, but he kindly refused", movement=Motion().refusing_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d25"),
            "d25": Storypart(id="d25", content_type="storypart", content=" I had enough information, so I went to another room to continue my investigation. Where shall we go now?", follow_id="d26"),
            "d26": Storypart(id="d26", content_type="choice", content="Do you want to keep looking inside in some other rooms or go outside to investigate there?", follow_id={0: "d27", 1: "d28"}), 
            #BATHROOM SCENE ENDS HERE, GO TO D27(WALK-IN CLOSET) OR D38(GARDEN)
            
            #WALK-IN CLOSET SCENE STARTS HERE
            "d27": Storypart(id="d27", content_type="storypart", content="The closet is my favorite hiding spot for playing hide and seek.", follow_id="d28"),
            "d28": Storypart(id="d28", content_type="storypart", content="I was looking on the top shelves and behind the clothes for some useful clues.", movement=Motion().pointing_high_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d29"),
            "d29": Storypart(id="d29", content_type="storypart", content="The only things I saw were shirts and pants in the primary colors: red, blue and yellow.", follow_id="d30"),
            "d30": Storypart(id="d30", content_type="question", content=("{0}, what color do you get when you mix the colors blue and red?", "answer_easy_color_question_one", "purple"), movement=Motion().mixing_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id={0: "d31a", 1: "d31b"}),
            "d31a": Storypart(id="d31a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. When you mix the colors blue and red you will get purple.", follow_id="d32"),
            "d31b": Storypart(id="d31b", content_type="storypart", content="Very good!! The correct answer is indeed purple.", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d32"),
            "d32": Storypart(id="d32", content_type="question", content=("And what happens if you mix the colors yellow and red?", "answer_easy_color_question_two", "orange"), movement=Motion().mixing_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id={0: "d33a", 1: "d33b"}),
            "d33a": Storypart(id="d33a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. When you mix the colors yellow and red you will get orange.", follow_id="d34"),
            "d33b": Storypart(id="d33b", content_type="storypart", content="Very good!! The correct answer is indeed orange.", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d34")

            "d34": Storypart(id="d34", content_type="storypart", content="This is fun, I'm really happy that you are helping me!", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d35"),
            "d35": Storypart(id="d35", content_type="storypart", content="Okay back to the story.", follow_id="d36"),
            "d36": Storypart(id="d36", content_type="storypart", content="So, after a quick investigation inside my favorite hiding place, I decided to go back to my room for a quick nap.", follow_id="d37"),
            "d37": Storypart(id="d37", content_type="storypart", content="How exciting this investigation may seem, I was getting tired.", movement=Motion().yawning_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d53"), 
            #WALK-IN CLOSET SCENE ENDS HERE, GO TO ROOM SCENE D53
            
            #GARDEN SCENE STARTS HERE, insert birds sounds
            "d38": Storypart(id="d38", content_type="storypart", content="When I stepped into the garden I heard a lot of birds.", follow_id="d39"),
            "d39": Storypart(id="d39", content_type="storypart", content="In the middle of the garden there was a tree full of 40 parakeets", movement=Motion().flying_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d40"),            
            "d40": Storypart(id="d40", content_type="storypart", content="Half of the parakeets were green and the other half was red.", follow_id="d41"),
            "d41": Storypart(id="d41", content_type="question", content=("{0} how many red parakeets were in the tree?", "answer_easy_parakeets", "20"), follow_id={0: "d42a", 1: "d42b"}),
            "d42a": Storypart(id="d42a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. There were 20 red parakeets in the tree.", follow_id="d43"),
            "d42b": Storypart(id="d42b", content_type="storypart", content="Excellent!! The correct answer is indeed 20.", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d43"),
            "d43": Storypart(id="d43", content_type="storypart", content="After looking around in the garden I saw that the backdoor was unlocked with dirty footprints on the door, which reminded me of a human, but a little bit different", follow_id="d44"),
            "d44": Storypart(id="d44", content_type="storypart", content="I decided to follow the footprints, but the track continued on the roof.", follow_id="d45"),
            "d45": Storypart(id="d45", content_type="question", content=("{0}, what item could I use to get on the roof?","answer_roof_question", "ladder"), follow_id= {0: "d46a", 1: "d46b"}),
            "d46a": Storypart(id="d46a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. We will be using a ladder.", follow_id="d47"),
            "d46b": Storypart(id="d46b", content_type="storypart", content="Smart thinking, we will indeed use a ladder.", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d47"),
            
            "d47": Storypart(id="d47", content_type="storypart", content="I climbed the ladder and got on the roof.", movement=Motion().climbing_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d48"),
            "d48": Storypart(id="d48", content_type="storypart", content=" I noticed that the room of my window was standing wide open", follow_id="d49"),            
            "d49": Storypart(id="d49", content_type="storypart", content=" That must be the reason why it was so cold tonight", movement=Motion().shivering_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d50"),            
            "d50": Storypart(id="d50", content_type="storypart", content=" where do we go now?", follow_id="d51"),            
            "d51": Storypart(id="d51", content_type="choice", content="Do we get back off the roof, or do we climb into the room?", follow_id={0: "d52", 1: "d53"}), 
            #back of the roof (d52) leads to room with 1 extra storypart
            "d52": Storypart(id="d52", content_type="storypart", content="I climbed off the ladder and quickly entered my house and went upstairs to my room.", movement=Motion().climbing_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d53"),
            #END OF GARDEN SCENE 
            
            #START ROOM SCENE 
            "d53": Storypart(id="d53", content_type="storypart", content=" I entered my own room, where I was sleeping just an hour ago", follow_id="d54"),            
            "d54": Storypart(id="d54", content_type="storypart", content=" I walked straight to my hamsters cage to see how Hamtaro was doing", follow_id="d55"), 
            #Insert MOUSE SOUNDS
            "d55": Storypart(id="d55", content_type="storypart", content=" I opened the cage and I looked directly into the feeding bowl of my very old hamster, was it possible that he ate my bananas?", movement=Motion().mouse_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d56"),  
            "d56": Storypart(id="d56", content_type="question", content=" My hamster is 10 years older than you {0}, how old is my hamster?","answer_hamster_question", "answer_age + 10", follow_id={0: "d57a", 1: "d57b"}), 
            "d57a": Storypart(id="d57a", content_type="storypart", content="Nope, my hamster is actually ({1}+10) years old.", follow_id="d58"),
            "d57b": Storypart(id="d57b", content_type="storypart", content="That’s correct!", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d58"),
            "d58": Storypart(id="d58", content_type="storypart", content=" I hadn’t fed him for 2 days, maybe he was extremely hungry", follow_id="d59"),            
            "d59": Storypart(id="d59", content_type="storypart", content=" I grabbed my hamster Hamtaro and looked at him",movement=Motion().grabbing_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d60"),            
            "d60": Storypart(id="d60", content_type="storypart", content=" Hamtaro was half the size of an actual banana, he couldn’t be the one who ate all my bananas", follow_id="d61"),            
            "d60": Storypart(id="d60", content_type="storypart", content=" Also the cage was closed when I arrived", follow_id="d61"),            
            "d60": Storypart(id="d60", content_type="storypart", content=" I gave Hamtaro something to eat and after looking further around in my room I detected nothing suspicious", follow_id="d61"),            
            #END ROOM SCENE
        
            #START ATTIC SCENE 
            "d61": Storypart(id="d61", content_type="storypart", content="Then all the sudden a freshly peeled banana felt on my head", follow_id="d62"), #INSERT THUMPING SOUND           
            "d62": Storypart(id="d62", content_type="storypart", content="I looked up and saw another banana dangling on the rope that leads to the attic, also known as my secret hiding spot and investigation headquarters", movement=Motion().looking_up_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d63"),
            "d63": Storypart(id="d63", content_type="storypart", content="Pulling on the rope, the stairs to the attic flipped out", movement=Motion().pulling_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d64"),
            "d64": Storypart(id="d64", content_type="storypart", content="On the stairs to the attic I found again a banana peel, but this time I was more careful.", follow_id="d65"),
            "d65": Storypart(id="d65", content_type="storypart", content="When I arrived at the attic, I smelled something weird, so I entered carefully", movement=Motion().looking_around_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d66"),
            "d66": Storypart(id="d66", content_type="storypart", content="The first thing I had to do was to find the light switch, since the attic was completely dark and I didn’t want to slip on a banana again", follow_id="d67"),
            "d67": Storypart(id="d67", content_type="storypart", content="I turned on the lights with my right hand", movement=Motion().right_arm_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d68"),
            #insert monkey sounds
            "d68": Storypart(id="d68", content_type="storypart", content="And in front of me I saw a very big, hairy and funky looking monkey with some weird disco trousers on.", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d69"),
            "d69": Storypart(id="d69", content_type="storypart", content="The monkey was dancing, while juggling with three bananas.", movement=Motion().jugling_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d70"),
            "d70": Storypart(id="d70", content_type="storypart", content="{0} I think we found the thief who stole my breakfast!", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d71"),
          
            #CLOSING SCENE 
            "d71": Storypart(id="d71", content_type="storypart", content="Then it came to me", follow_id="d72"),           
            "d72": Storypart(id="d72", content_type="question", content="What place has monkeys, elephants and parakeets and could have been in town this whole week?","answer_circus_question", "circus", follow_id={0: "d73a", 1: "d73b"}), 
            "d73a": Storypart(id="d73a", content_type="storypart", content="Yes the circus is in town!", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d74"),
            "d73b": Storypart(id="d73b", content_type="storypart", content="No, the circus is in town!", movement=Motion().clapping_hands_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d74"),
            #insert circus tune tutututututtuutututututututu
            "d74": Storypart(id="d74", content_type="question", content="Would you like to do a funky monkey dance with me?", follow_id={0: "d75a", 1: "d76"}), 
            
            #NO
            "d75a": Storypart(id="d75a", content_type="storypart", content="Alright, thank you for participating and being my help detectictive for today", follow_id="d75b"),           
            "d75b": Storypart(id="d75b", content_type="storypart", content="See you next time”", movement=Motion().waving_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d75c"),           
            "d75c": NAO OUT
            #YES
            "d76": Storypart(id="d76", content_type="storypart", content="Disco time!", movement=Motion().disco_dance, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d77"),
            #START DISCO TUNE
            "d77": Storypart(id="d77", content_type="storypart", content="Thank you for participating and being my help detectictive for today", follow_id="d78"),           
            "d78": Storypart(id="d78", content_type="storypart", content="See you next time”", movement=Motion().waving_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d79"),            
            "d79": NAO OUT
           
        
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
