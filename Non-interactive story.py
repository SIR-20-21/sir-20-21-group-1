"d1": Storypart(id="d1", content_type="storypart", content="Hi, my name is NAO Holmes and it is really nice to meet you, {0}.", follow_id="d2"),
            "d2": Storypart(id="d2", content_type="storypart", content="I’m going to solve a very interesting mystery today. Would you like to join me?", follow_id='d2a'),
            "d2a": Storypart(id="d2a", content_type="choice", content="Touch my right for yes, and my left for no", movement=Motion().right_left ,movement_type=MOVEMENT_TYPE.MOTION,follow_id={0: "s1", 1: "d3"}),
            #EXPLAIN THE HAND MOVEMENT
            "d3": Storypart(id="d3", content_type="storypart", content="Okay cool, from now on you will be my personal detective!", follow_id="d4"),
            "d4": Storypart(id="d4", content_type="storypart", content="So the following happened this morning: 'By 7 a.m. I rolled out of bed straight to the kitchen to make myself a major breakfast, because I was hungry as a bear. Suddenly, I noticed something very odd: all the bananas that I bought yesterday and were placed in the bowl on my wooden table were gone. While in a hurry, I ran to the hallway when suddenly I slipped on a peeled banana. Before I knew it was laying on the ground like this", follow_id="d4a"),
            "d4a": Storypart(id="d4a", content_type="storypart", content="", movement=RobotPosture.LYINGBACK, movement_type=MOVEMENT_TYPE.POSTURE, follow_id="d5"),
            "d5": Storypart(id="d5", content_type="storypart", content="Ouch! I looked around in chock, I certainly did not put this banana here.", follow_id="d5a"),
            "d5a": Storypart(id="d5a", content_type="storypart", content="", movement=RobotPosture.STAND, movement_type=MOVEMENT_TYPE.POSTURE, follow_id="d6"),
            "d6": Storypart(id="d6", content_type="storypart", content="I slipped on my detective trench coat over my blue striped pyjamas, put on my fedora, and began my investigation.", soundfile='sounds/detective.wav', follow_id="d7"),
            
            "d7": Storypart(id="d7", content_type="storypart", content="First, I wanted to check the rooms upstairs. I flew up the stairs", movement=Motion().walking, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d7a"),
            "d7a": Storypart(id="d7a", content_type="question", content=("{0} How many steps does my staircase have in total?", "answer_math_question", "24"), follow_id={0: "d8a", 1: "d8b"}),
            "d8a": Storypart(id="d8a", content_type="storypart", content="Sorry, it was 24 steps. But good try, though!", follow_id="d9"),
            "d8b": Storypart(id="d8b", content_type="storypart", content="Well done! 24 steps indeed!", follow_id="d9"),

            "d9": Storypart(id="d9", content_type="highfive", content="Give me a high five!", follow_id="d10a"),
            "d10a": Storypart(id="d10a", content_type="storypart", content="Back to the top of the stairs. Standing there in the corridor I had to make a very very difficult choice. On my left I heard a strange thumping sound.", soundfile='sounds/thumping.wav', follow_id="d10b"),
            "d10b": Storypart(id="d10b", content_type="storypart", content="and on my right I heard something that sounded like a trumpet", soundfile="sounds/trumpet.wav", follow_id="d11"),

            "d11": Storypart(id="d11", content_type="choice", content="Where would you have gone? Left or right?", follow_id={0: "d12a", 1: "d12b"}),
            "d12a": Storypart(id="d12a", content_type="storypart", content="Yes very good, that is where I went as well!", follow_id="d13"),
            "d12b": Storypart(id="d12b", content_type="storypart", content="Very good thinking, but I chose to go to the right and investigate the trumpet sounds.", follow_id="d13"),
            # TODO insert TIPTOE movement? (is this even possible?)
            "d13": Storypart(id="d13", content_type="storypart", content="“I took out my magnifying glass, which I always have in my pocket for such occasions. Leaning close to the floor, I could see enormous footprints going all the way to my bathroom. Curious. I made my way to the bathroom, where I thought I heard rustling and water continuously dripping on the bathroom tiles.", soundfile="sounds/water.wav", follow_id="d14"),
            "d14": Storypart(id="d14", content_type="storypart", content="I crept quietly towards the bathroom door, trying not to make a sound.", soundfile="sounds/tiptoe.wav", follow_id="d15"),

            "d15": Storypart(id="d15", content_type="storypart", content="", soundfile="sounds/sssshh.wav", follow_id="d16"),
            "d16": Storypart(id="d16", content_type="storypart", content="I opened the door in one movement and looked inside.", follow_id="d17"),

            "d16a": Storypart(id="d16a", content_type="storypart", content="", soundfile="sounds/scary.wav", follow_id="d17"),
            
            "d17": Storypart(id="d17", content_type="storypart", content="The bathroom was empty, so I casually walked in.", movement=Motion().walking, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d18"),
            "d18": Storypart(id="d18", content_type="storypart", content="Maybe I just imagined the sounds.", follow_id="d19"),

            #BATHROOM SCENE STARTS HERE
            "d19": Storypart(id="d19", content_type="storypart", content="In the bathroom I threw some water in my face to refresh myself.", movement=Motion().face_wash, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d20"),
            "d20": Storypart(id="d20", content_type="storypart", content="While I was looking in the mirror I noticed that there was an elephant standing in the shower.", movement="elephant_motion-4d89bf/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d21"),
            "d21": Storypart(id="d21", content_type="storypart", content="The elephant could be the one that ate all my bananas, but then I remembered that elephants don’t eat bananas.", follow_id="d22"),
            "d22": Storypart(id="d22", content_type="question", content=("{0}, {1}","{0}", "{0}"), follow_id= {0: "d23a", 1: "d23b"}),

            "d23a": Storypart(id="d23a", content_type="storypart", content="No, unfortunately {0} is not correct. {0}", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d24"),
            "d23b": Storypart(id="d23b", content_type="storypart", content="Yes, very good! {0}", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d24"),
            "d24": Storypart(id="d24", content_type="storypart", content="Just to be sure, I asked the elephant if he wanted to have a banana, but he kindly refused", movement='animations/Stand/Gestures/No_8', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d25"),
            "d25": Storypart(id="d25", content_type="storypart", content=" I had enough information, so I went to another room to continue my investigation. Where shall we go now?", follow_id="d26"),
            # TODO maybe better say which arm is which option
            "d26": Storypart(id="d26", content_type="choice", content="Do you want to keep looking inside in some other rooms or go outside to investigate there?", follow_id={0: "d27", 1: "d28"}), 
            #BATHROOM SCENE ENDS HERE, GO TO D27(WALK-IN CLOSET) OR D38(GARDEN)
            
            #WALK-IN CLOSET SCENE STARTS HERE
            "d27": Storypart(id="d27", content_type="storypart", content="The closet is my favorite hiding spot for playing hide and seek.", follow_id="d28"),
            "d28": Storypart(id="d28", content_type="storypart", content="I was looking on the top shelves and behind the clothes for some useful clues.", movement="point_up/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d29"),
            "d29": Storypart(id="d29", content_type="storypart", content="The only things I saw were shirts and pants in the primary colors: red, blue and yellow.", follow_id="d30"),

            "d30": Storypart(id="d30", content_type="question", content=("{0}, {1}", "answer_color_question", "green"), movement=Motion().mixing_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id={0: "d31a", 1: "d31b"}),
            "d31a": Storypart(id="d31a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. {0}", follow_id="d32"),
            "d31b": Storypart(id="d31b", content_type="storypart", content="Very good!! The correct answer is indeed green.", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d32"),
            "d32": Storypart(id="d32", content_type="question", content=("{0}", "answer_color_question", "orange"), movement=Motion().mixing_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id={0: "d33a", 1: "d33b"}),
            "d33a": Storypart(id="d33a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. {0}", follow_id="d34"),
            "d33b": Storypart(id="d33b", content_type="storypart", content="Very good!! The correct answer is indeed orange.", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d34"),

            "d34": Storypart(id="d34", content_type="storypart", content="This is fun, I'm really happy that you are helping me!", movement=Motion().big_gesture, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d35"),
            "d35": Storypart(id="d35", content_type="storypart", content="Okay, back to the story.", follow_id="d36"),
            "d36": Storypart(id="d36", content_type="storypart", content="So, after a quick investigation inside my favorite hiding place, I decided to go back to my room for a quick nap.", follow_id="d37"),
            # below was yawning gesture, but removed because hard to imitate
            "d37": Storypart(id="d37", content_type="storypart", content="How exciting this investigation may seem, I was getting tired.", soundfile="sounds/sleep.wav", follow_id="d53"), 
            #WALK-IN CLOSET SCENE ENDS HERE, GO TO ROOM SCENE D53
            
            #GARDEN SCENE STARTS HERE, insert birds sounds
            "d38": Storypart(id="d38", content_type="storypart", content="When I stepped into the garden I heard a lot of birds.", soundfile="sounds/birds.wav", follow_id="d39"),
            "d39": Storypart(id="d39", content_type="storypart", content="In the middle of the garden there was a tree full of 40 parakeets", movement="flying-be9ea3/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d40"),            
            "d40": Storypart(id="d40", content_type="storypart", content="Half of the parakeets were green and the other half was red.", follow_id="d41"),
            "d41": Storypart(id="d41", content_type="question", content=("{0}, {1}", "answer_easy_parakeets", "{0}"), follow_id={0: "d42a", 1: "d42b"}),
            "d42a": Storypart(id="d42a", content_type="storypart", content="No unfortunately that is not correct, but still a very good try. {0}", follow_id="d43"),
            "d42b": Storypart(id="d42b", content_type="storypart", content="Excellent!! The correct answer is indeed {0}.", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d43"),

            "d43": Storypart(id="d43", content_type="storypart", content="After looking around in the garden I saw that the backdoor was unlocked with dirty footprints on the door, which reminded me of a human, but a little bit different", follow_id="d44"),
            "d44": Storypart(id="d44", content_type="storypart", content="I decided to follow the footprints, but the track continued on the roof.", follow_id="d45"),
            "d45": Storypart(id="d45", content_type="question", content=("{0}, what item could I use to get on the roof?","answer_roof_question", "ladder"), follow_id= {0: "d46a", 1: "d46b"}),
            "d46a": Storypart(id="d46a", content_type="storypart", content="No, unfortunately that is not correct, but still a very good try. We will be using a ladder.", follow_id="d47"),
            "d46b": Storypart(id="d46b", content_type="storypart", content="Smart thinking, we will indeed use a ladder.", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d47"),
            
            "d47": Storypart(id="d47", content_type="storypart", content="I climbed the ladder and got on the roof.", movement="climbing-db5359/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d48"),
            "d48": Storypart(id="d48", content_type="storypart", content="I noticed that the window of my room was standing wide open", follow_id="d49"),            
            "d49": Storypart(id="d49", content_type="storypart", content="That must be the reason why it was so cold tonight", movement="shivering-f5eafc/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d50"),            
            "d50": Storypart(id="d50", content_type="storypart", content="where do we go now?", follow_id="d51"),            
            "d51": Storypart(id="d51", content_type="choice", content="Do we get back off the roof, or do we climb into the room?", follow_id={0: "d52", 1: "d53"}), 
            #back of the roof (d52) leads to room with 1 extra storypart
            "d52": Storypart(id="d52", content_type="storypart", content="I climbed off the ladder and quickly entered my house and went upstairs to my room.", movement="climbing-db5359/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d53"),
            #END OF GARDEN SCENE 
            
            #START ROOM SCENE
            "d53": Storypart(id="d53", content_type="storypart", content="I entered my own room, where I was sleeping just an hour ago", soundfile="sounds/sleep.wav", follow_id="d54"),
            "d54": Storypart(id="d54", content_type="storypart", content="I walked straight to my hamsters cage to see how Hamtaro was doing", follow_id="d55"),
            "d55": Storypart(id="d55", content_type="storypart", content="I opened the cage and I looked directly into the feeding bowl of my very old hamster, was it possible that he ate my bananas?", soundfile="sounds/mouse.wav", movement="mouse_motion-3bf9b6/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d56"),
            "d56": Storypart(id="d56", content_type="question", content=("{0}","answer_hamster_question", "{0}"), follow_id={0: "d57a", 1: "d57b"}), 
            "d57a": Storypart(id="d57a", content_type="storypart", content="Nope, my hamster is actually {1} years old.", follow_id="d58"),
            "d57b": Storypart(id="d57b", content_type="storypart", content="That’s correct!", movement="animations/Stand/Exclamation/NAO/Right_Strong_EXC_03", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d58"),


            "d58": Storypart(id="d58", content_type="storypart", content="I hadn’t fed him for 2 days, maybe he was extremely hungry", follow_id="d59"),
            # grabbing movement below removed
            "d59": Storypart(id="d59", content_type="storypart", content="I grabbed my hamster Hamtaro and looked at him", follow_id="d60a"),
            "d60a": Storypart(id="d60a", content_type="storypart", content="Hamtaro was half the size of an actual banana, he couldn’t be the one who ate all my bananas", follow_id="d60b"),
            "d60b": Storypart(id="d60b", content_type="storypart", content="Also the cage was closed when I arrived", follow_id="d60c"),
            "d60c": Storypart(id="d60c", content_type="storypart", content="I gave Hamtaro something to eat and after looking further around in my room I detected nothing suspicious", follow_id="d61"),
            #END ROOM SCENE
        
            #START ATTIC SCENE 
            "d61": Storypart(id="d61", content_type="storypart", content="Then all the sudden a freshly peeled banana felt on my head", soundfile="sounds/thumping.wav", follow_id="d62"),         
            "d62": Storypart(id="d62", content_type="storypart", content="I looked up and saw another banana dangling on the rope that leads to the attic, also known as my secret hiding spot and investigation headquarters", movement="point_up-d4285/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d63"),
            "d63": Storypart(id="d63", content_type="storypart", content="Pulling on the rope, the stairs to the attic flipped out", movement="pulling-c35961/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d64"),
            "d64": Storypart(id="d64", content_type="storypart", content="On the stairs to the attic I found again a banana peel, but this time I was more careful.", follow_id="d65"),
            # "d65": Storypart(id="d65", content_type="storypart", content="When I arrived at the attic, I smelled something weird, so I entered carefully", movement=Motion().looking_around_movement, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d66"),
            "d66": Storypart(id="d66", content_type="storypart", content="The first thing I had to do was to find the light switch, since the attic was completely dark and I didn’t want to slip on a banana again", follow_id="d67"),
            "d67": Storypart(id="d67", content_type="storypart", content="I turned on the lights with my right hand", movement=Motion().backhand_right, movement_type=MOVEMENT_TYPE.MOTION, follow_id="d68"),
            "d68": Storypart(id="d68", content_type="storypart", content="And in front of me I saw a very big, hairy and funky looking monkey with some weird disco trousers on.", soundfile="sounds/monkey.wav", movement='gorilla_motion-3ce914/behavior_1', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d69"),
            "d69": Storypart(id="d69", content_type="storypart", content="The monkey was dancing, while juggling with three bananas.", movement="juggling-7a4d8b/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d70"),
            "d70": Storypart(id="d70", content_type="storypart", content="{0}, I think we found the thief who stole my breakfast!", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d71"),
          
            #CLOSING SCENE 
            "d71": Storypart(id="d71", content_type="storypart", content="Then it came to me", follow_id="d72"),           
            "d72": Storypart(id="d72", content_type="question", content=("What place has monkeys, elephants and parakeets and could have been in town this whole week?","answer_circus_question", "circus"), follow_id={0: "d73a", 1: "d73b"}), 
            "d73a": Storypart(id="d73a", content_type="storypart", content="Yes the circus is in town!!", soundfile="sounds/circus.wav", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d74"),
            "d73b": Storypart(id="d73b", content_type="storypart", content="No, the circus is in town!!", soundfile="sounds/circus.wav", movement="clapping-ed52d2/behavior_1", movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d74"),
            "d74": Storypart(id="d74", content_type="question", content="Would you like to do a funky monkey dance with me?", follow_id={0: "d75a", 1: "d76"}), 
            
            #YES
            # TODO insert disco sound
            "d76": Storypart(id="d76", content_type="storypart", content="Disco time!", soundfile=None, movement='disco_dance-eb402b/behavior_1', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="d75a"),

            #NO
            "d75a": Storypart(id="d75a", content_type="storypart", content="Alright, thank you for participating and being my help detectictive for today", follow_id="d75b"),           
            "d75b": Storypart(id="d75b", content_type="storypart", content="See you next time, detective {0}", movement='animations/Stand/Gestures/Hey_1', movement_type=MOVEMENT_TYPE.GESTURE, follow_id="s1"),
        }
