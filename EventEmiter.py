"""
Create-an-event-emitting system that we can use:
1. To register listeners-for-a-specific-
event.
2.-To-emit-events. Emitting an event-should-run- the corresponding event listeners-we- registered.
Example:
// Creates an instance of an event emitter. keyboard = new EventEmitter()
//-Registers-an-event-specific-listener. keyboard.addListener(eventName: string, listener: callback)-> void
//-Runs all-registered event listeners for the specific event.
keyboard.emit (eventName: string)-->-void

Q2: -Removes the given listener-from-the-
given event
keyboard.removeListener(eventName: string, listener: callback)--> void
"""

class EventEmitter:
    def __init__(self):
        self.event_listeners = {}

    def add_listener(self, event_name, listener):
        if event_name not in self.event_listeners:
            self.event_listeners[event_name] = []
        self.event_listeners[event_name].append(listener)

    def emit(self, event_name):
        listeners = self.event_listeners.get(event_name,[])
        for listener in listeners:
            listener()

    def remove_listener(self,event_name, listener):
        listners = self.event_listeners.get(event_name,[])

        if listener in listners:
            listners.remove(listener)



def event_listener1():
    print("Event listener 1 executed")

def event_listener2():
    print("Event listener 2 executed")



# Create an instance of the event emitter
keyboard = EventEmitter()

# Register event listeners
keyboard.add_listener("keypress", event_listener1)
keyboard.add_listener("keypress", event_listener2)

print("List of listners:")
print(keyboard.event_listeners)

# Emit events
keyboard.emit("keypress1")
keyboard.remove_listener("keypress", event_listener2)

print("List of listners after removal:")
print(keyboard.event_listeners)

"""In this example, we define a class EventEmitter that has an event_listeners dictionary to store the registered listeners for each event. The add_listener method is used to register a listener for a specific event. It checks if the event name is already in the event_listeners dictionary, and if not, it creates a new empty list for that event name. Then it appends the listener to the list.

The emit method is used to emit an event. It retrieves the list of listeners for the specified event name and iterates over each listener, calling it.

In the example usage, we create an instance of EventEmitter called keyboard. We register two event listeners event_listener1 and event_listener2 for the "keypress" event using the add_listener method. Finally, we emit the "keypress" event using the emit method, which triggers the execution of all the registered event listeners for that event. The output will be:

Event listener 1 executed
Event listener 2 executed
"""




