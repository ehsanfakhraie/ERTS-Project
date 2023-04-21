RUNNING   = 0   # Currently executing on the processor
READY     = 1   # Ready to run but task of higher or equal priority is currently running
BLOCKED   = 2   # Task is waiting for some condition to be met to move to READY state
SUSPENDED = 3   # Task is waiting for some other task to unsuspend

INTERRUPT =0  # Task type is interrupt
PERIODIC  =1  # Task type is periodic
APERIODIC =2  # Task type is aperiodic
SPORADIC  =3  # Task type is sporadic


class Task (object):
    
    def __init__(self,priority=255,name=None,state=SUSPENDED,type=None,act_time=0,period=0,wcet=0) ->None:
        self.priority = priority
        self.name = name
        self.state = state
        self.type = type
        self.act_time = act_time
        self.period = period
        self.wcet = wcet
        # you can add more attributes if you need
        
    
    def change_state(self,state):
        self.state = state

    def change_priority(self,priority):
        self.priority = priority
        
    
        
        
    