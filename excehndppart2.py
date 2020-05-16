class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle(self):
        print("Accident occured take detour: ",self.msg)



try:
    raise Accident('crash between two cars')
except Accident as e:
   e.handle()
finally:
    print("Cleaning up going on !!:)")