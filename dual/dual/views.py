#import libraries
from pyramid.view import (
    view_config,
    view_defaults
    )
import logging
from jaeger_client import Config
from gpiozero import OutputDevice, Servo, PWMOutputDevice, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from os import getenv

# Define the factories
factory = PiGPIOFactory(host='192.168.0.24')
factory2 = PiGPIOFactory(host='192.168.0.23')

# Define both robots
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

#Define the eyes
linus_eye = LED(16, pin_factory=factory)
torvalds_eye = LED(25, pin_factory=factory2)

# Define the servo
servo = Servo(22, pin_factory=factory)
servo2 = Servo(23, pin_factory=factory)

# Define the jaeger host
JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')

#Set up Jaeger function
def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'local_agent': {'reporting_host': JAEGER_HOST},
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('eye-service')


@view_defaults(renderer='dual.pt')
class DualViews:
    def __init__(self, request):
        self.request = request
    @view_config(route_name='home')
    def home(self):
        return {}
    @view_config(route_name='forward')
    def forward(self):
        motor_in1.on()
        motor_in2.off()
        motor_in3.on()
        motor_in4.off()
        return {}
    @view_config(route_name='backward')
    def backward(self):
        motor_in1.off()
        motor_in2.on()
        motor_in3.off()
        motor_in4.on()
        return {}
    @view_config(route_name='left')
    def left(self):
        motor_in1.off()
        motor_in2.on()
        motor_in3.on()
        motor_in4.off()
        return {}
    @view_config(route_name='right')
    def right(self):
        motor_in1.on()
        motor_in2.off()
        motor_in3.off()
        motor_in4.on()
        return {}
    @view_config(route_name='stop')
    def stop(self):
        motor_in1.off()
        motor_in2.off()
        motor_in3.off()
        motor_in4.off()
        return {}
    @view_config(route_name='north')
    def north(self):
        pin1.off()
        pin2.on()
        pin3.on()
        pin4.off()
        return {}
    @view_config(route_name='south')
    def south(self):
        pin1.on()
        pin2.off()
        pin3.off()
        pin4.on()
        return {}
    @view_config(route_name='west')
    def west(self):
        pin1.on()
        pin2.off()
        pin3.on()
        pin4.off()
        return {}
    @view_config(route_name='east')
    def east(self):
        pin1.off()
        pin2.on()
        pin3.off()
        pin4.on()
        return {}
    @view_config(route_name='stoptwo')
    def stoptwo(self):
        pin1.off()
        pin2.off()
        pin3.off()
        pin4.off()
        return {}
    @view_config(route_name='servomin')
    def servomin(self):
        servo.min()
        return {}
    @view_config(route_name='servomid')
    def servomid(self):
        servo.mid()
        return {}
    @view_config(route_name='servomax')
    def servomax(self):
        servo.max()
        return {}
    @view_config(route_name='servomin2')
    def servomin2(self):
        servo2.min()
        return {}
    @view_config(route_name='servomid2')
    def servomid2(self):
        servo2.mid()
        return {}
    @view_config(route_name='servomax2')
    def servomax2(self):
        servo2.max()
        return {}
    @view_config(route_name='thirty')
    def thirty(self):
        en_1.value = .3
        en_2.value = .3
        return {}
    @view_config(route_name='fifty')
    def fifty(self):
        en_1.value = .5
        en_2.value = .5
        return {}
    @view_config(route_name='full')
    def full(self):
        en_1.value = 1
        en_2.value = 1
        return {}
    @view_config(route_name='linuson')
    def linuson(self):
        with tracer.start_span('linus-eye'):
            linus_eye.on()
        return {}
    @view_config(route_name='linusoff')
    def linusoff(self):
        linus_eye.off()
        return {}
    @view_config(route_name='torvaldson')
    def torvaldson(self):
        with tracer.start_span('torvalds-eye'):
            torvalds_eye.on()
        return {}
    @view_config(route_name='torvaldsoff')
    def torvaldsoff(self):
        torvalds_eye.off()
        return {}




















