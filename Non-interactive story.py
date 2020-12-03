from conversation import Motion, MOVEMENT_TYPE
from social_interaction_cloud.basic_connector import RobotPosture

class Story:

    def __init__(non_story):
        """https://github.com/SIR-20-21/sir-20-21-group-1
        :return:
        """
        # allows you to directly jump to a storypart
        self.initial_id = "d1"

        # This is the actual story
        # Each Storypart needs an ID, a content_type and the content.
        # The ID is for unique identification and is used to indicate the following storypart.
        # The content_type is a storypart
        #   storypart   -> text
        # Optionally, there can be a follow_id. If none is provided, the story ends after this part.
        #   If the follow_id is a string, then this determines the next storypart

        non_story.story = {            
            
            
            "d1": Storypart(id="d1", content_type="storypart", content="Hi, my name is NAO Holmes, follow_id="d2"),
            "d2": Storypart(id="d2", content_type="storypart", content="I’m going to solve a very interesting mystery today", follow_id=""d3"),
            "d3": Storypart(id="d3", content_type="storypart", content="So the following happened this morning: 'By 7 a.m. I rolled out of bed straight to the kitchen to make myself a major breakfast, because I was hungry as a bear. Suddenly, I noticed something very odd: all the bananas that I bought yesterday and were placed in the bowl on my wooden table were gone. While in a hurry, I ran to the hallway when suddenly I slipped on a peeled banana. Before I knew it was laying on the ground", follow_id="d4"),
            "d4": Storypart(id="d4", content_type="storypart", content="I looked around in shock, I certainly did not put this banana here.", follow_id="d5"),
            "d5": Storypart(id="d5", content_type="storypart", content="I slipped on my detective trench coat over my blue striped pyjamas, put on my fedora, and began my investigation.", follow_id="d6"),
            "d6": Storypart(id="d6", content_type="storypart", content="First, I wanted to check the rooms upstairs. So I flew up the stairs", follow_id="d7"),
            "d7": Storypart(id="d7", content_type="storypart", content="On the top of the stairs I had to make a very very difficult choice. On my left I heard a strange thumping sound.", follow_id="d8"),
            "d8": Storypart(id="d8", content_type="storypart", content="and on my right I heard something that sounded like a trumpet", follow_id="d9"),
            "d9": Storypart(id="d9", content_type="storypart", content="I chose to go to the right and investigate the trumpet sounds.", follow_id="d10"),
            "d10": Storypart(id="d10", content_type="storypart", content="“I took out my magnifying glass, which I always have in my pocket for such occasions. Leaning close to the floor, I could see enormous footprints going all the way to my bathroom. Curious. I made my way to the bathroom, where I thought I heard rustling and water continuously dripping on the bathroom tiles.", follow_id="d11"),
            "d11": Storypart(id="d11", content_type="storypart", content="I crept quietly towards the bathroom door, trying not to make a sound.", follow_id="d12"),
            "d12": Storypart(id="d12", content_type="storypart", content="I opened the door in one movement and looked inside.", follow_id="d13"),
            "d13": Storypart(id="d13", content_type="storypart", content="The bathroom was empty, so I casually walked in.", follow_id="d14"),
            "d14": Storypart(id="d14", content_type="storypart", content="Maybe I just imagined the sounds.", follow_id="d15"),
            "d15": Storypart(id="d15", content_type="storypart", content="In the bathroom I threw some water in my face to refresh myself.", follow_id="d16"),
            "d16": Storypart(id="d16", content_type="storypart", content="While I was looking in the mirror I noticed that there was an elephant standing in the shower.", follow_id="d17"),
            "d17": Storypart(id="d17", content_type="storypart", content="The elephant could be the one that ate all my bananas, but then I remembered that elephants don’t eat bananas.", follow_id="d18"),
            "d18": Storypart(id="d18", content_type="storypart", content="Just to be sure, I asked the elephant if he wanted to have a banana, but he kindly refused", follow_id="d19"),
            "d19": Storypart(id="d19", content_type="storypart", content=" I had enough information, so I went to another room to continue my investigation.", follow_id="d20"),
            "d20": Storypart(id="d20", content_type="choice", content="I strode to the walk-in closet since I saw that the door was ajar", follow_id="21"),
            "d21": Storypart(id="d21", content_type="storypart", content="So, after a quick investigation inside my favorite hiding place, I decided to go outside to investigate there.", follow_id="d22"),
            "d22": Storypart(id="d22", content_type="storypart", content="I was in desperate need of some fresh air.", follow_id="d23")
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
            "d54": Storypart(id="d45", content_type="storypart", content="I turned on the lights with my right hand",  follow_id="d46"),
            "d46": Storypart(id="d46", content_type="storypart", content="And in front of me I saw a very big, hairy and funky looking monkey with some weird disco trousers on.", follow_id="d47"),
            "d47": Storypart(id="d47", content_type="storypart", content="The monkey was dancing, while juggling with three bananas.", follow_id="d48"),
            "d48": Storypart(id="d48", content_type="storypart", content="I think I found the thief who stole my breakfast!", follow_id="d49"),
            "d49": Storypart(id="d49", content_type="storypart", content="Then it came to me", follow_id="d50"),
            "d50": Storypart(id="d50", content_type="storypart", content="The circus is in town!!", follow_id="d51"),
            "d51": Storypart(id="d51", content_type="storypart", content="That was the end of the story, thankyou for listening",            
        }
