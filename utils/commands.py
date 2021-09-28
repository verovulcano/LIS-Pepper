import numpy as np
import time

def degToRad(dAngle):

    rAngle = dAngle * np.pi / 180

    return rAngle

# List of commands - one hand

def acqua(pepper, finger_name, finger_velocity):

    finger_value = []

    for i in range(len(finger_name)):
        finger_value.append(degToRad(180))

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(0), degToRad(-80), degToRad(-30), degToRad(0)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity
    
    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["LElbowRoll"], [degToRad(-60)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowRoll"], [degToRad(-80)], [0.8])
        time.sleep(0.2)

def bagno(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(0)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(0), degToRad(-80), degToRad(-90), degToRad(90)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["LElbowYaw"], [degToRad(-70)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowYaw"], [degToRad(-90)], [0.8])
        time.sleep(0.2)

def bere(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(10), degToRad(0), degToRad(-70), degToRad(-60), degToRad(30)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)
    
    for i in range(2):
        pepper.setAngles(["LElbowRoll"], [degToRad(-80)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowRoll"], [degToRad(-70)], [0.8])
        time.sleep(0.2)

def bicchiere(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(180), degToRad(180)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(-10), degToRad(10), degToRad(-80), degToRad(-30), degToRad(-90)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)
    
    for i in range(3):
        pepper.setAngles(["LWristYaw"], [degToRad(90)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LWristYaw"], [degToRad(-90)], [0.8])
        time.sleep(0.2)

def caffe(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(180)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(10), degToRad(0), degToRad(-70), degToRad(-60), degToRad(0)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)
    
    for i in range(2):
        pepper.setAngles(["LWristYaw"], [degToRad(50)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LWristYaw"], [degToRad(0)], [0.8])
        time.sleep(0.2)

def cocacola(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(90), degToRad(60), degToRad(30), degToRad(180), degToRad(90)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(10), degToRad(0), degToRad(-80), degToRad(-60), degToRad(30)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

    pepper.setAngles(["LShoulderRoll"], [degToRad(15)], [0.2])
    time.sleep(1)

def gomma(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(180), degToRad(180), degToRad(180), degToRad(160), degToRad(180), degToRad(180), degToRad(140), degToRad(180), degToRad(180), degToRad(0), degToRad(180), degToRad(180), degToRad(90), degToRad(180)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(5), degToRad(0), degToRad(-70), degToRad(-50), degToRad(-30)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)
    
    for i in range(2):
        pepper.setAngles(["LElbowRoll"], [degToRad(-50)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowRoll"], [degToRad(-70)], [0.8])
        time.sleep(0.2)

def grazie(pepper, finger_name, finger_velocity):
    
    finger_value = []

    for i in range(len(finger_name)):
        finger_value.append(degToRad(180))
    
    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(0), degToRad(-80), degToRad(-60), degToRad(-90)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

    pepper.setAngles(["LShoulderPitch"], [degToRad(30)], [0.2])
    time.sleep(1)

def mangiare(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(15), degToRad(0), degToRad(-80), degToRad(-50), degToRad(-90)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)
    
    for i in range(3):
        pepper.setAngles(["LElbowRoll"], [degToRad(-90)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowRoll"], [degToRad(-80)], [0.8])
        time.sleep(0.2)

def pagare(pepper, finger_name, finger_velocity):
    
    finger_value = []

    for i in range(len(finger_name)):
        finger_value.append(degToRad(0))
    
    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(20), degToRad(-60), degToRad(-50), degToRad(-50)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)
    
    for i in range(2):
        pepper.setAngles(["LElbowYaw"], [degToRad(-30)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowYaw"], [degToRad(-50)], [0.8])
        time.sleep(0.2)

def vino(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(0)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(0), degToRad(-80), degToRad(-80), degToRad(0)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(2):
        pepper.setAngles(["LElbowRoll"], [degToRad(-88)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowRoll"], [degToRad(-80)], [0.8])
        time.sleep(0.2)

def tu(pepper, finger_name, finger_velocity):

    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(0)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(10), degToRad(0), degToRad(-40), degToRad(-30), degToRad(-20)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

def io(pepper, finger_name, finger_velocity):

    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(0)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(30), degToRad(0), degToRad(-90), degToRad(-30), degToRad(-90)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

def non(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(0)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(30), degToRad(0), degToRad(-80), degToRad(-90), degToRad(90)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["LElbowYaw"], [degToRad(-70)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowYaw"], [degToRad(-90)], [0.8])
        time.sleep(0.2)

def dire(pepper, finger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(0)]
    
    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(0), degToRad(-80), degToRad(-50), degToRad(-90)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

    pepper.setAngles(["LShoulderPitch"], [degToRad(40)], [0.4])
    time.sleep(1)

def portare(pepper, finger_name, finger_velocity):

    finger_value = []

    for i in range(len(finger_name)):
        finger_value.append(degToRad(0))

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(10), degToRad(-30), degToRad(-40), degToRad(40)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

    pepper.setAngles(["LElbowRoll"], [degToRad(-60)], [0.8])
    time.sleep(1)

def dove(pepper, finger_name, finger_velocity):

    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(0), degToRad(0)]

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(20), degToRad(30), degToRad(-80), degToRad(-30), degToRad(0)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["LElbowRoll"], [degToRad(-60)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowRoll"], [degToRad(-80)], [0.8])
        time.sleep(0.2)

def perfavore(pepper, finger_name, finger_velocity):

    finger_value = []

    for i in range(len(finger_name)):
        finger_value.append(degToRad(180))

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(10), degToRad(0), degToRad(-88), degToRad(-70), degToRad(0)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

    pepper.setAngles(["LShoulderPitch", "LElbowYaw"], [degToRad(30), degToRad(-60)], [0.2, 0.2])
    time.sleep(1)

def volere(pepper, finger_name, finger_velocity):

    finger_value1 = []

    for i in range(len(finger_name)):
        finger_value1.append(degToRad(180))

    # base configuration
    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(30), degToRad(0), degToRad(-90), degToRad(-50), degToRad(-90)] + finger_value1
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

    finger_value2 = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180)]

    pepper.setAngles(finger_name, finger_value2, finger_velocity)
    time.sleep(1)

def essere(pepper, finger_name, finger_velocity):

    finger_value = [degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(0), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180), degToRad(180)]

    joints = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"] + finger_name
    values = [degToRad(10), degToRad(10), degToRad(-80), degToRad(0), degToRad(-100)] + finger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + finger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["LElbowRoll"], [degToRad(-88)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowRoll"], [degToRad(-80)], [0.8])
        time.sleep(0.2)

# List of commands - two hands

def bar(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    finger_value = []

    for i in range(len(Lfinger_name)):
        finger_value.append(degToRad(0))

    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value = finger_value + finger_value

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(20), degToRad(0), degToRad(-80), degToRad(-60), degToRad(0)]
    Rarm_value = [degToRad(0), degToRad(0), degToRad(80), degToRad(60), degToRad(0)]
    LRarm_value = Larm_value + Rarm_value
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    joints = LRarm_name + LRfinger_name
    values = LRarm_value + LRfinger_value
    velocities = LRarm_velocity + LRfinger_velocity

    # base configuration
    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["LShoulderPitch", "RShoulderPitch"], [degToRad(0), degToRad(20)], [0.8, 0.8])
        time.sleep(0.2)
        pepper.setAngles(["LShoulderPitch", "RShoulderPitch"], [degToRad(20), degToRad(0)], [0.8, 0.8])
        time.sleep(0.2)

def birra(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    Lfinger_value = []

    for i in range(len(Lfinger_name)):
        Lfinger_value.append(degToRad(0))

    Rfinger_value = [degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(20), degToRad(180), degToRad(180)]

    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value = Lfinger_value + Rfinger_value

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(0), degToRad(0), degToRad(-80), degToRad(-60), degToRad(0)]
    Rarm_value = [degToRad(40), degToRad(0), degToRad(60), degToRad(60), degToRad(20)]
    LRarm_value = Larm_value + Rarm_value
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    joints = LRarm_name + LRfinger_name
    values = LRarm_value + LRfinger_value
    velocities = LRarm_velocity + LRfinger_velocity

    # base configuration
    pepper.setAngles(joints, values, velocities)
    time.sleep(1)

    pepper.setAngles(["LShoulderPitch"], [degToRad(30)], [0.8])
    time.sleep(1)

def panino(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    finger_value = [degToRad(0), degToRad(180), degToRad(180), degToRad(0), degToRad(180), degToRad(180), degToRad(0), degToRad(180), degToRad(180), degToRad(0), degToRad(180), degToRad(180), degToRad(90), degToRad(180)]
    
    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value = finger_value + finger_value

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(10), degToRad(0), degToRad(-80), degToRad(-40), degToRad(-20)]
    Rarm_value = [degToRad(30), degToRad(-20), degToRad(80), degToRad(60), degToRad(-10)]
    LRarm_value = Larm_value + Rarm_value
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    joints = LRarm_name + LRfinger_name
    values = LRarm_value + LRfinger_value
    velocities = LRarm_velocity + LRfinger_velocity

    # base configuration
    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(2):
        pepper.setAngles(["LElbowYaw", "RElbowRoll"], [degToRad(-60), degToRad(120)], [0.8, 0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowYaw", "RElbowRoll"], [degToRad(-40), degToRad(80)], [0.8, 0.8])
        time.sleep(0.2)

def tavolo(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    finger_value = []

    for i in range(len(Lfinger_name)):
        finger_value.append(degToRad(180))

    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value = finger_value + finger_value

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(20), degToRad(10), degToRad(-90), degToRad(0), degToRad(0)]
    Rarm_value = [degToRad(30), degToRad(-10), degToRad(90), degToRad(0), degToRad(0)]
    LRarm_value = Larm_value + Rarm_value
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    joints = LRarm_name + LRfinger_name
    values = LRarm_value + LRfinger_value
    velocities = LRarm_velocity + LRfinger_velocity

    # base configuration
    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    pepper.setAngles(["LElbowRoll", "RElbowRoll"], [degToRad(0), degToRad(0)], [0.8, 0.8])
    time.sleep(1)

def cosa(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    finger_value1 = []

    for i in range(len(Lfinger_name)):
        finger_value1.append(degToRad(180))

    finger_value2 = [degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120)]

    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value1 = finger_value1 + finger_value1
    LRfinger_value2 = finger_value2 + finger_value2

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(20), degToRad(10), degToRad(-60), degToRad(-40), degToRad(40)]
    Rarm_value = [degToRad(20), degToRad(-10), degToRad(60), degToRad(40), degToRad(-40)]
    LRarm_value = Larm_value + Rarm_value
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    # base configuration
    pepper.setAngles(LRarm_name, LRarm_value, LRarm_velocity)
    time.sleep(0.2)
    # finger configuration
    pepper.setAngles(LRfinger_name, LRfinger_value1, LRfinger_velocity)
    time.sleep(0.2)

    pepper.setAngles(LRfinger_name, LRfinger_value2, LRfinger_velocity)
    time.sleep(0.2)

    joints = ["LElbowRoll", "RElbowRoll"] + LRfinger_name
    values = [degToRad(-30), degToRad(30)] + LRfinger_value1
    velocities = [0.2, 0.2] + LRfinger_velocity

    pepper.setAngles(joints, values, velocities)
    time.sleep(0.2)

    pepper.setAngles(LRfinger_name, LRfinger_value2, LRfinger_velocity)
    time.sleep(1)

def sinistra(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    finger_value = []

    for i in range(len(Lfinger_name)):
        finger_value.append(degToRad(180))

    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value = finger_value + finger_value

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(-10), degToRad(10), degToRad(-40), degToRad(0), degToRad(90)]
    Rarm_value = [degToRad(10), degToRad(-10), degToRad(80), degToRad(40), degToRad(-40)]
    LRarm_value = Larm_value + Rarm_value
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    joints = LRarm_name + LRfinger_name
    values = LRarm_value + LRfinger_value
    velocities = LRarm_velocity + LRfinger_velocity

    # base configuration
    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["RElbowYaw"], [degToRad(20)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["RElbowYaw"], [degToRad(40)], [0.8])
        time.sleep(0.2)

def destra(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    finger_value = []

    for i in range(len(Lfinger_name)):
        finger_value.append(degToRad(180))

    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value = finger_value + finger_value

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(10), degToRad(10), degToRad(-80), degToRad(-40), degToRad(40)]
    Rarm_value = [degToRad(-10), degToRad(-10), degToRad(40), degToRad(0), degToRad(-90)]
    LRarm_value = Larm_value + Rarm_value
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    joints = LRarm_name + LRfinger_name
    values = LRarm_value + LRfinger_value
    velocities = LRarm_velocity + LRfinger_velocity

    # base configuration
    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    for i in range(3):
        pepper.setAngles(["LElbowYaw"], [degToRad(-20)], [0.8])
        time.sleep(0.2)
        pepper.setAngles(["LElbowYaw"], [degToRad(-40)], [0.8])
        time.sleep(0.2)

def buongiorno(pepper, Lfinger_name, Rfinger_name, finger_velocity):
    
    finger_value1 = [degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120), degToRad(120), degToRad(0), degToRad(120)]

    finger_value2 = []

    for i in range(len(Lfinger_name)):
        finger_value2.append(degToRad(180))

    LRfinger_name = Lfinger_name + Rfinger_name
    LRfinger_velocity = finger_velocity + finger_velocity
    LRfinger_value = finger_value2 + finger_value2

    Larm_name = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw"]
    Rarm_name = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    LRarm_name = Larm_name + Rarm_name

    Larm_value = [degToRad(15), degToRad(0), degToRad(-80), degToRad(-50), degToRad(-90)]
    Rarm_value = [degToRad(20), degToRad(0), degToRad(70), degToRad(50), degToRad(90)]
    
    LRarm_velocity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

    # base configuration
    pepper.setAngles(Larm_name, Larm_value, [0.4, 0.4, 0.4, 0.4, 0.4])
    time.sleep(0.2)
    # finger configuration
    pepper.setAngles(Lfinger_name, finger_value1, finger_velocity)
    time.sleep(0.2)

    joints = Rarm_name + LRfinger_name
    values = Rarm_value + LRfinger_value
    velocities = [0.4, 0.4, 0.4, 0.4, 0.4] + LRfinger_velocity
    pepper.setAngles(joints, values, velocities)
    time.sleep(0.5)

    pepper.setAngles(["LElbowYaw", "RElbowYaw"], [degToRad(-80), degToRad(80)], [0.4, 0.4])
    time.sleep(1)

# Handle the command

def action(x, pepper, Lfinger_name, Rfinger_name, finger_velocity):

    if x == 'acqua':
        acqua(pepper, Lfinger_name, finger_velocity)
        
    elif x == 'bagno':
        bagno(pepper, Lfinger_name, finger_velocity)

    elif x == 'bar':
        bar(pepper, Lfinger_name, Rfinger_name, finger_velocity)

    elif x == 'bere':
        bere(pepper, Lfinger_name, finger_velocity)

    elif x == 'bicchiere':
        bicchiere(pepper, Lfinger_name, finger_velocity)

    elif x == 'birra':
        birra(pepper, Lfinger_name, Rfinger_name, finger_velocity)
    
    elif x == 'caffè':
        caffe(pepper, Lfinger_name, finger_velocity)

    elif x == 'coca-cola':
        cocacola(pepper, Lfinger_name, finger_velocity)

    elif x == 'gomma da masticare':
        gomma(pepper, Lfinger_name, finger_velocity)

    elif x == 'grazie':
        grazie(pepper, Lfinger_name, finger_velocity)

    elif x == 'mangiare':
        mangiare(pepper, Lfinger_name, finger_velocity)

    elif x == 'pagare':
        pagare(pepper, Lfinger_name, finger_velocity)

    elif x == 'panino':
        panino(pepper, Lfinger_name, Rfinger_name, finger_velocity)

    elif x == 'tavolo':
        tavolo(pepper, Lfinger_name, Rfinger_name, finger_velocity)

    elif x == 'vino':
        vino(pepper, Lfinger_name, finger_velocity)

    elif x == 'io':
        io(pepper, Lfinger_name, finger_velocity)

    elif x == 'tu':
        tu(pepper, Lfinger_name, finger_velocity)

    elif x == 'non':
        non(pepper, Lfinger_name, finger_velocity)

    elif x == 'dire':
        dire(pepper, Lfinger_name, finger_velocity)

    elif x == 'cosa':
        cosa(pepper, Lfinger_name, Rfinger_name, finger_velocity)

    elif x == 'portare':
        portare(pepper, Lfinger_name, finger_velocity)

    elif x == 'dove':
        dove(pepper, Lfinger_name, finger_velocity)

    elif x == 'sinistra':
        sinistra(pepper, Lfinger_name, Rfinger_name, finger_velocity)
    
    elif x == 'destra':
        destra(pepper, Lfinger_name, Rfinger_name, finger_velocity)

    elif x == 'perfavore':
        perfavore(pepper, Lfinger_name, finger_velocity)

    elif x == 'volere':
        volere(pepper, Lfinger_name, finger_velocity)

    elif x == 'essere':
        essere(pepper, Lfinger_name, finger_velocity)

    elif x == 'buongiorno':
        buongiorno(pepper, Lfinger_name, Rfinger_name, finger_velocity)

    else:
        print("Pepper: Mi dispiace ma ancora non conosco questa parola!")