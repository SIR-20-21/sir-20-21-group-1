from conversation import Conversation, ReturnType
from social_interaction_cloud.basic_connector import BasicSICConnector
from story import Story, Storypart


class Storyteller:
    """
    Represents the logic guiding conversations between a robot and a human.
    """

    def __init__(self, server_ip, dialogflow_key_file, dialogflow_agent_id):
        """
        :param server_ip: IP address of Social Interaction Cloud server
        :param dialogflow_key_file: path to Google's Dialogflow key file (JSON)
        :param dialogflow_agent_id: ID number of Dialogflow agent to be used (project ID)
        """
        self.sic = BasicSICConnector(
            server_ip, 'en-US', dialogflow_key_file, dialogflow_agent_id)
        self.conversation = Conversation(self.sic, robot_present=True, animation=True)
        self.story = Story(interactive=True)

    def run(self) -> None:
        """
        Start the social interaction cloud and a conversation.
        :return:
        """
        self.sic.start()
        self.conversation.introduce(interaction=True)
        self.sic.subscribe_touch_listener(
            'MiddleTactilTouched', self.conversation.detect_stop)

        path = self.conversation.ask_question(
            "Do you want to hear a story or a joke?", intent="joke_path")
        while path == ReturnType.SUCCESS and self.conversation.current_choice == "joke":
            # tell joke
            joke = self.conversation.get_joke()
            for joke_part in joke:
                self.conversation.tell_story_part(text=joke_part)
            path = self.conversation.ask_question(
                "Do you want to hear a story or another joke?", intent="joke_path")
            pass

        # START STORY
        part = None
        branch_option = None
        while True:
            if self.conversation.stop:
                break

            part = self.story.getFollowUp(part, branch_option)
            if (part is None):
                break

            if part.type == "question":
                question, intent, expected_answer = part.content
                res = self.conversation.ask_question(question=Storypart.format(question, user_model=self.conversation.user_model, story_part_id=part.id),
                                                     intent=Storypart.format(
                                                         intent, user_model=self.conversation.user_model, story_part_id="intent_" + part.id),
                                                     expected_answer=Storypart.format(expected_answer, user_model=self.conversation.user_model,
                                                                                      story_part_id="answer_" + part.id))
                if res == ReturnType.STOP:
                    break
                elif res == ReturnType.MAX_ATTEMPTS:
                    self.conversation.tell_story_part(
                        "Sorry, I did not understand your answer.")

                    # TODO ask for repetetion or ending through fist bump
                    # res = self.conversation.ask_question(question, intent)
                    # last_choice = self.conversation.current_choice
                    # self.sic.subscribe_touch_listener(
                    #     'HandRightBackTouched', lambda: self.conversation.set_current_choice(0))
                    # self.sic.subscribe_touch_listener(
                    #     'HandLeftBackTouched', lambda: self.conversation.set_current_choice(1))
                    # self.conversation.request_choice(
                    #     "To repeat the last part fistbump my right fist. To stop fistbump my left fist.")
                    # while (last_choice == self.conversation.current_choice):
                    #     pass
                    # if last_choice == 0:
                    #     # TODO implement repetition
                    #     pass
                    # elif last_choice == 1:
                    #     break
                elif res == ReturnType.WRONG_ANSWER:
                    branch_option = 0
                elif res == ReturnType.SUCCESS:
                    if expected_answer is not None:
                        branch_option = 1
                    else:
                        branch_option = None

            elif part.type == "storypart":
                storypart = part.content
                self.conversation.tell_story_part(Storypart.format(
                    storypart, self.conversation.user_model, part.id), movement=part.movement, movement_type=part.movement_type, eye_color=part.eye_color, soundfile=part.soundfile)

            elif part.type == "choice":
                self.conversation.current_choice = None
                storypart = part.content

                if self.conversation.robot_present:
                    self.sic.subscribe_touch_listener(
                        'HandRightBackTouched', lambda: self.conversation.set_current_choice(0))
                    self.sic.subscribe_touch_listener(
                        'HandLeftBackTouched', lambda: self.conversation.set_current_choice(1))
                else:
                    self.conversation.current_choice = 1
                    
                self.conversation.request_choice(question=Storypart.format(
                    storypart, self.conversation.user_model, part.id))
                while (self.conversation.current_choice is None):
                    pass
                branch_option = self.conversation.current_choice

            elif part.type == "highfive":
                self.sic.subscribe_touch_listener(
                    'HandLeftLeftTouched', self.conversation.detect_highfive)
                self.sic.subscribe_touch_listener(
                    'HandLeftRightTouched', self.conversation.detect_highfive)

                self.conversation.request_highfive(part.content)


                while (self.conversation.current_choice != 1):
                    pass

        if not self.conversation.stop:
            path = self.conversation.ask_question(
                "Do you want to hear another joke or stop?", intent="joke_path")
            while path == ReturnType.SUCCESS and self.conversation.current_choice == "joke":
                # tell joke
                joke = self.conversation.get_joke()
                for joke_part in joke:
                    self.conversation.tell_story_part(text=joke_part)
                path = self.conversation.ask_question(
                    "Do you want to hear another joke or stop?", intent="joke_path")
                pass

        self.conversation.end_conversation()
        self.sic.stop()


if __name__ == "__main__":
    storyteller = Storyteller('127.0.0.1',
                              'newagent-tfdt-2585f6cb1ae5.json',
                              'newagent-tfdt')
    storyteller.run()
