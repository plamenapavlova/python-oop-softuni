class Smartphone:
    def __init__(self, memory:int):
        self.memory = memory
        self.apps:list = []
        self.is_on:bool = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, memory):
        if self.memory >= memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= memory
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
