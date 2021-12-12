class QuizletFormatter:
  def __init__(self, definitiontxt, answerstxt):
    with open(definitiontxt) as def_raw:
      def_string = def_raw.read()
      def_lines = def_string.split('\n')
    with open(answerstxt) as ans_raw:
      ans_string = ans_raw.read()
      ans_lines = ans_string.split('\n')
    self.definitions = def_lines
    self.answers = ans_lines

  def format(self, charSepQA, charNewline):
    finished = []
    for i in range(len(self.definitions)):
      temp = self.definitions[i]
      self.definitions[i] = charNewline + temp
    
    for i in range(len(self.answers)):
      temp = self.answers[i]
      finished.append(self.definitions[i] + charSepQA + temp)
      
    for i in finished:
      print(i)


