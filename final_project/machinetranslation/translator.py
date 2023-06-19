from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    text = englishText
    frenchText = MyMemoryTranslator(source='english', target='french').translate(text)
    return frenchText

def frenchToEnglish(frenchText):
    text = frenchText
    englishText = MyMemoryTranslator(source='french', target='english').translate(text)
    return englishText