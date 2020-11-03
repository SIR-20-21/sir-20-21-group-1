from time import sleep
from social_interaction_cloud.abstract_connector import AbstractSICConnector
from social_interaction_cloud.action import ActionRunner
from social_interaction_cloud.basic_connector import BasicSICConnector
from social_interaction_cloud.detection_result_pb2 import DetectionResult

class Example:
    """Example that uses speech recognition. Prerequisites are the availability of a dialogflow_key_file,
    a dialogflow_agent_id, and a running Dialogflow service. For help meeting these Prerequisites see
    https://socialrobotics.atlassian.net/wiki/spaces/CBSR/pages/260276225/The+Social+Interaction+Cloud+Manual"""

    def __init__(self, server_ip: str, dialogflow_key_file: str, dialogflow_agent_id: str):
        self.sic = BasicSICConnector(server_ip, 'en-US', dialogflow_key_file, dialogflow_agent_id)
        self.action_runner = ActionRunner(self.sic)

        self.user_model = {}
        self.recognition_manager = {'attempt_success': False, 'attempt_number': 0}

    def run(self) -> None:
        self.sic.start()
        if (self.introduce()):
            print('here')
            self.action_runner.run_waiting_action('set_language', 'en-US')

            while not self.recognition_manager['attempt_success'] and self.recognition_manager['attempt_number'] < 2:
                self.action_runner.run_waiting_action('say', 'Hello, world! Tell me your name.')
                self.action_runner.run_waiting_action('speech_recognition', 'answer_name', 0, additional_callback=self.on_intent)

            self.reset_recognition_management()


            if 'name' in self.user_model:
                self.action_runner.run_waiting_action('say', 'Thank you!')

            while not self.recognition_manager['attempt_success'] and self.recognition_manager['attempt_number'] < 2:
                self.action_runner.run_waiting_action('say', 'How old are you?')
                self.action_runner.run_waiting_action('speech_recognition', 'answer_age', 0, additional_callback=self.on_intent)
        else:
            self.action_runner.run_waiting_action('say', 'Bye bye!')
            # self.action_runner.run_waiting_action('rest')

        self.sic.stop()

    def introduce(self) -> None:
        # self.action_runner.load_waiting_action('wake_up')
        self.action_runner.run_waiting_action('set_language', 'en-US')
        # self.action_runner.run_loaded_actions()
        while not self.recognition_manager['attempt_success'] and self.recognition_manager['attempt_number'] < 2:
            self.action_runner.run_waiting_action('say', 'Hello! I am Nao! Do you want to hear a story?')
            self.action_runner.run_waiting_action('speech_recognition', 'answer_tell_story', 0, additional_callback=self.on_intent)

        self.reset_recognition_management()

        if 'decision' in self.user_model and self.user_model['decision'] == "Yes":
            return True
        
        return False


    def on_intent(self, detection_result: DetectionResult) -> None:
        if detection_result and len(detection_result.parameters) > 0:

            if detection_result.intent == 'answer_name':
                self.user_model['name'] = detection_result.parameters['name'].struct_value['name']
                self.recognition_manager['attempt_success'] = True

            elif detection_result.intent == 'answer_age':
                self.user_model['age'] = detection_result.parameters['age'].struct_value['amount']
                self.recognition_manager['attempt_success'] = True

            elif detection_result.intent == 'answer_tell_story':
                print(detection_result.parameters['decision'].string_value)
                self.user_model['decision'] = detection_result.parameters['decision'].string_value
                self.recognition_manager['attempt_success'] = True
            else:
                self.recognition_manager['attempt_number'] += 1

        else:
            self.recognition_manager['attempt_number'] += 1

    def reset_recognition_management(self) -> None:
        self.recognition_manager.update({'attempt_success': False, 'attempt_number': 0})


example = Example('127.0.0.1',
                  'newagent-tfdt-2585f6cb1ae5.json',
                  'newagent-tfdt')
example.run()

