from conversation import Conversation, ReturnType
from social_interaction_cloud.basic_connector import BasicSICConnector
from story import Story, Storypart
# from naoqi import ALProxy


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
        self.conversation = Conversation(self.sic, robot_present=False)
        self.story = Story()

        # self.tts = ALProxy("ALTextToSpeech", server_ip, 9559)
        # self.tts.setParameter("speed", 200)

    def run(self) -> None:
        """
        Start the social interaction cloud and a conversation.
        :return:
        """
        self.sic.start()
        self.conversation.introduce()

        # TODO implement decision between story and jokes here

        part = None
        branch_option = None
        while True:
            part = self.story.getFollowUp(part, branch_option)
            if (part is None):
                break

            if part.type == "question":
                question, intent, expected_answer = part.content
                res = self.conversation.ask_question(question=Storypart.format(question, user_model=self.conversation.user_model, id=part.id),
                                                     intent=Storypart.format(
                                                         intent, user_model=self.conversation.user_model, story_part_id="intent_" + part.id),
                                                     expected_answer=Storypart.format(expected_answer, user_model=self.conversation.user_model,
                                                                                      id="answer_" + part.id))
                if res == ReturnType.STOP:
                    break
                elif res == ReturnType.MAX_ATTEMPTS:
                    self.conversation.tell_story_part(
                        "Sorry, I did not understand your answer.")
                    # TODO ask for repetetion or ending through fist bump
                    # res = self.conversation.ask_question(question, intent)
                    last_choice = self.conversation.current_choice
                    self.sic.subscribe_touch_listener(
                        'HandRightBackTouched', lambda: self.conversation.set_current_choice(0))
                    self.sic.subscribe_touch_listener(
                        'HandLeftBackTouched', lambda: self.conversation.set_current_choice(1))
                    self.conversation.request_choice(
                        "To repeat the last part fistbump my right fist. To stop fistbump my left fist.")
                    while (last_choice == self.conversation.current_choice):
                        pass
                    if last_choice == 0:
                        # TODO implement repetition
                        pass
                    elif last_choice == 1:
                        break
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
                    storypart, self.conversation.user_model, part.id), movement=part.movement, movement_type=part.movement_type, soundfile=part.soundfile)

            elif part.type == "choice":
                last_choice = self.conversation.current_choice
                storypart = part.content

                self.sic.subscribe_touch_listener(
                    'HandRightBackTouched', lambda: self.conversation.set_current_choice(0))
                self.sic.subscribe_touch_listener(
                    'HandLeftBackTouched', lambda: self.conversation.set_current_choice(1))
                self.conversation.request_choice(question=Storypart.format(
                    storypart, self.conversation.user_model, part.id))
                while (last_choice == self.conversation.current_choice):
                    pass
                choice = self.conversation.current_choice

            elif part.type == "highfive":
                self.conversation.request_hivefive(part.content)
                
                self.sic.subscribe_touch_listener(
                    'HandLeftLeftTouched', self.conversation.detect_highfive)
                self.sic.subscribe_touch_listener(
                    'HandLeftRightTouched', self.conversation.detect_highfive)

                while (self.conversation.current_choice != 1):
                    pass



        self.conversation.end_conversation()
        self.sic.stop()


if __name__ == "__main__":
    storyteller = Storyteller('127.0.0.1',
                              'newagent-tfdt-2585f6cb1ae5.json',
                              'newagent-tfdt')
    storyteller.run()
