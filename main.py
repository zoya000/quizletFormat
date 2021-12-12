from quizlet import QuizletFormatter
import pyperclip as pc
#spanishClassroomPhrases = QuizletFormatter('classvocabspanishdef.txt', "classvocabspanishans.txt")
#spanishClassroomPhrases.format('*', '@')

bioUnitFour = QuizletFormatter('bioUnit5q.txt', "bioUnit5a.txt")
bioUnitFour.format('*', '@')
pc.copy(bioUnitFour)
# would the weathering part of erosion count as weathering or erosion 