import sys
import os

class Logger():
  stdout = sys.stdout
  logs = []

  def start(self): 
    sys.stdout = self

  def stop(self): 
    sys.stdout = self.stdout

  def write(self, log): 
    self.logs.append(log)

def retConsole(code, *args):
  globs = ""
  if (args):
    options = args[0]
    
    if ("save" in options):
      if (options["save"]):
        for var in list(globals().keys()):
          globs += "global "+var+"\n"

  log = Logger()
  log.start()
  exec(globs+code)
  log.stop()
  console = ""
  for output in log.logs:
    if (output) == "\n": continue
    console += output
  return console

def runScript(filePath):
  os.execv(sys.executable, ['python', filePath])