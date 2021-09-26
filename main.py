from qibullet import SimulationManager
from qibullet import PepperVirtual
from utils.commands import *
from utils.listener import Listener
from utils.nlp import text_processing

listener = Listener()

LFinger_name = ['LFinger41', 'LFinger42', 'LFinger43', 'LFinger31', 'LFinger32', 'LFinger33', 'LFinger21', 'LFinger22', 'LFinger23', 'LFinger11', 'LFinger12', 'LFinger13', 'LThumb1', 'LThumb2']
RFinger_name = ['RFinger41', 'RFinger42', 'RFinger43', 'RFinger31', 'RFinger32', 'RFinger33', 'RFinger21', 'RFinger22', 'RFinger23', 'RFinger11', 'RFinger12', 'RFinger13', 'RThumb1', 'RThumb2']
LRFinger_velocity = []

for i in range(len(LFinger_name)):
	LRFinger_velocity.append(0.4)

if __name__ == "__main__":

	simulation_manager = SimulationManager()
	client_id = simulation_manager.launchSimulation(gui=True)
	pepper = simulation_manager.spawnPepper(client_id, spawn_ground_plane=True)

	pepper.goToPosture("Stand", 0.6)
	time.sleep(0.5)
	pepper.moveTo(0.5, -0.5, degToRad(-38), frame=PepperVirtual.FRAME_ROBOT)
	time.sleep(0.5)

	flag = True

	while flag:

		command, taken = listener.listen()
		
		if command == 'arrivederci':
			
			print("Pepper: Ciao, è stato un piacere!")
			break

		if taken == False:
			
			print("Pepper: Non ho capito, puoi ripetere?")
			
		else:
			
			sentence = text_processing(command)

			for word in sentence:

				action(word, pepper, LFinger_name, RFinger_name, LRFinger_velocity)
				pepper.goToPosture("Stand", 0.6)
				time.sleep(1)