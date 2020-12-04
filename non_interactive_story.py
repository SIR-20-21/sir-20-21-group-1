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
        self.conversation = Conversation(self.sic, robot_present=True, animation=False)
        self.story = Story(interactive=False)

    def run(self) -> None:
        """
        Start the social interaction cloud and a conversation.
        :return:
        """
        self.sic.start()
        self.conversation.introduce(interaction=False)
        self.sic.subscribe_touch_listener(
            'MiddleTactilTouched', self.conversation.detect_stop)


        # START STORY
        part = None
        branch_option = None
        while True:
            if self.conversation.stop:
                break

            part = self.story.getFollowUp(part, branch_option)
            if (part is None):
                break

            storypart = part.content
            self.conversation.tell_story_part(Storypart.format(
                storypart, self.conversation.user_model, part.id), movement=part.movement, movement_type=part.movement_type, eye_color=part.eye_color, soundfile=part.soundfile)


        self.conversation.end_conversation()
        self.sic.stop()


if __name__ == "__main__":
    storyteller = Storyteller('127.0.0.1',
                              'newagent-tfdt-2585f6cb1ae5.json',
                              'newagent-tfdt')
    storyteller.run()
