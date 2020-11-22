# -*- coding: utf-8 -*-
"""
TIES481: Simulation, assignment 3

Created on Fri Nov 13 11:31:51 2020

@author: Janne Heikkinen, Aapo Peiponen ja Liisa Petäinen

"""

import simpy
import random
import pandas as pd
import numpy as np
    
class Hospital:
        """
        Hospital class that runs the actual simulation
        """

        i = 0  
        info = False
        simulation_length = 100        
        patient_count = 0
        NUM_PREP = 3
        NUM_RECOVERY = 3
        NUM_SURGERY = 1        
        prep_time = 40
        recovery_time = 60
        surgery_time = 20        
        patients_waiting = 0
        total_time_spent = 0
        total_patients_done = 0        
        queue_time = 0
        queue_time_prep = 0
        queue_time_op = 0
        queue_time_rec = 0        
        max_queue = 0
        max_queue_time = 0        
        operating_room_idle = 0
        priority = 0

        preparation_room_queue = [] #Contains the length of preparation room queue for each time unit (such as time = 1, 2, 3, 4...)

        patient_priority = pd.Series([0,0,0] , index = ['priority 1','priority 2','priority 3'])
        prep_queue_length = pd.Series([0])
        prep_queue_time = pd.Series([0])        
        operation_queuetime = pd.Series(0)
        operation_queue_patientid = pd.Series(0)        
        recovery_queuetime = pd.Series(0)
        recovery_queue_patientid = pd.Series(0)
        
        times_recovery_blocked = 0
                             
        def __init__(self, preparation_rooms, recovery_rooms, length, seed, print_info):
                self.env = simpy.Environment() 
                self.NUM_PREP = preparation_rooms
                self.NUM_RECOVERY = recovery_rooms
                self.simulation_length = length
                self.info = print_info
                random.seed(seed)                 
                self.prep_time = random.normalvariate(40, 2)
                self.recovery_time = random.normalvariate(40, 2)
                self.surgery_time = random.normalvariate(20, 1)              
                
        
        # Define the recources and start the process    
        def run(self):                
                self.preparation = simpy.Resource(self.env,capacity = self.NUM_PREP)
                self.surgery =simpy.Resource(self.env,capacity = self.NUM_SURGERY)
                self.recovery = simpy.Resource(self.env,capacity = self.NUM_RECOVERY)
                self.env.process(self.go_queue_and_prepare())
                self.env.process(operating_room_idle(self.env, self.surgery, self))
                self.env.process(monitor_queue_length(self.env, self))
                self.env.run(self.simulation_length)
        
        # Queue for patients going to preparation
        def go_queue_and_prepare(self):
                while True:
                        #TODO: tarviiko tää satunnaisuutta?
                        yield self.env.timeout(10) 
                        p=Patient(self.env, self)
                        self.queue_time = self.env.now
                        self.env.process(self.flow(p))                       
                        

        # Patient flow: queue for preparation, preparation, surgery, recovery
        def flow(self,patient):
                
                self.i+=1
                self.patients_waiting+=1
                
                request = self.preparation.request()
                
                yield request
                
                if(self.info) : print('patient queue: ', self.patients_waiting)
                if(self.info) : print('patient number %s enters the preparation at %.2f.' % (patient.id, self.env.now))
                
                self.queue_time_prep = self.env.now - self.queue_time
                self.prep_queue_time[self.i]=self.queue_time_prep
                self.prep_queue_length[self.i]=self.patients_waiting
        
                self.patients_waiting-=1
                
                if(self.info) : print('patient queue: ', self.patients_waiting)
                if(self.info) : print('patient number %s enters the preparation at %.2f.' % (patient.id, self.env.now))
                
                yield self.env.timeout(self.prep_time)
                patient.total_time_spent = self.env.now - self.queue_time
                preparation_end_time = self.env.now
            
                request2 = self.surgery.request()
                yield request2
                
                self.preparation.release(request)
                operation_start_time =self.env.now
                
                # Count the time patient had to wait for operation room to be free
                self.queue_time_op = operation_start_time - preparation_end_time
                self.operation_queue_patientid[self.i] = patient.id
                self.operation_queuetime[self.i] = self.queue_time_op
                
                
                if(self.info) : print('patient number %s enters the surgery at %.2f.' % (patient.id, self.env.now))
                yield self.env.timeout(self.surgery_time)
                surgery_end_time = self.env.now
                
                request3 = self.recovery.request()
                yield request3
                self.surgery.release(request2)
                recovery_start_time = self.env.now
                
                # Count the time patient had to wait after the surgery, if recovery is full
                self.queue_time_rec = recovery_start_time - surgery_end_time
                self.recovery_queue_patientid[self.i] = patient.id
                self.recovery_queuetime[self.i] = self.queue_time_rec
                
                
                if (self.recovery_queuetime[self.i] > 1) : self.times_recovery_blocked += 1        
                
                if(self.info) : print('patient number %s enters the recovery at %.2f.' % (patient.id, self.env.now))
                
                yield self.env.timeout(self.recovery_time)
                
                if(self.info) : print('patient number %s leaves the recovery at %.2f.' % (patient.id, self.env.now))
                
                self.recovery.release(request3)

               

                self.total_time_spent += self.env.now-patient.time_in
                self.total_patients_done += 1

class Patient:
        """
        Class for new patients
        """
        def __init__(self,env,hospital):
                hospital.patient_count+=1
                self.queue_time = 0
                self.time_in = env.now
                self.id=hospital.patient_count
                self.priority = random.randint(1, 3)
                hospital.patient_priority[self.priority-1] += 1
                


def operating_room_idle(env, operatingRoom, hospital):
        """
        Measures the time operating room remains idle
        """
        while True:
                if operatingRoom.count == 0:
                        hospital.operating_room_idle += 1
                yield env.timeout(1)    

def monitor_queue_length(env, hospital):
        """
        Records the preparation room queue length.
        """            
        while True:
                hospital.preparation_room_queue = hospital.preparation_room_queue + [hospital.patients_waiting]
                yield env.timeout(1)

def run_simulation(preparation_rooms, recovery_rooms, length, seed, print_info):
        """
        Runs a hospital simulation with given parameters.

        Arguments:\n
        preparation_rooms -- number of preparation rooms in the hospital\n
        recovery_rooms    -- number of recovery rooms in the hospital\n
        length            -- the desired runtime of the simulation\n
        seed              -- seed for the random numbers in the simulation\n
        print_info        -- true/false, whether to print extra info during the simulation or not to\n
        """
        hospital = Hospital(preparation_rooms, recovery_rooms, length, seed, print_info)
        hospital.run()
        #TODO: return other useful values
        #print(hospital.recovery_queuetime)
        return [hospital.preparation_room_queue, hospital.operating_room_idle, hospital.times_recovery_blocked, hospital.total_patients_done]        

        #print("Simulation finished.")
        #print("There were %.0f preparation rooms, and %.0f recovery rooms." % (preparation_rooms, recovery_rooms))
        #print("Length of this simulation was %.0f." % (length))
        #print("Average preparation queue is %.2f with a 95%% confidence interval of [%.2f,%.2f]." % ())
        #print('Total number of patients released is %.2f with %.2f being the average time.' % (hospital.total_patients_done, hospital.total_time_spent/hospital.total_patients_done))
        #print('Total idle time for operating room is %.2f.' % (hospital.operating_room_idle),'\n')
        #queue = pd.DataFrame({'Preparation queue length': hospital.prep_queue_length, 'prep_queue_time': hospital.prep_queue_time})
        #queue_operation = pd.DataFrame({'Patient id': hospital.operation_queue_patientid, 'Waiting time for operation': hospital.operation_queuetime})
        #queue_recovery = pd.DataFrame({'Patient id': hospital.recovery_queue_patientid, 'Waiting time for recovery': hospital.recovery_queuetime})
        #print(queue)
        #for index, row in queue.iterrows():
                #print(row['Preparation queue length'], row['prep_queue_time'])
        #print(queue_operation)
        #print(queue_recovery)
        #o = 0
        #for prep in hospital.prep_queue_time:
                #print(prep)
                #print("%.2f, %.2f" % (hospital.prep_queue_length[o],hospital.prep_queue_time[o]))
                #o+=1
        