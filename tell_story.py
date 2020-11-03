from conversation import Conversation
from story import Story
from social_interaction_cloud.abstract_connector import AbstractSICConnector
from social_interaction_cloud.action import ActionRunner
from social_interaction_cloud.basic_connector import BasicSICConnector
from social_interaction_cloud.detection_result_pb2 import DetectionResult

class Storyteller:
    def __init__(self, server_ip, dialogflow_key_file, dialogflow_agent_id):
        self.sic = BasicSICConnector(server_ip, 'en-US', dialogflow_key_file, dialogflow_agent_id)
        self.conversation = Conversation(self.sic)
        self.story = Story()

    def run(self):
        self.sic.start()
        self.conversation.introduce()        

        for part in self.story:
            if part["type"] == "question":
                question, intent = part["content"]
                res = self.conversation.ask_question(question, intent)
                if res == -1:
                    break
            elif part["type"] == "storypart":
                storypart = part["content"]
                self.conversation.tell_story_part(self.story.format(storypart, self.conversation.user_model, part["id"]))

        self.conversation.end_conversation()
        self.sic.stop()

    

storyteller = Storyteller('127.0.0.1',
                  'newagent-tfdt-2585f6cb1ae5.json',
                  'newagent-tfdt')
storyteller.run()