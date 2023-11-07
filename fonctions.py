def authors_name(fileName: str):
    """
    Return the name of the text's author
    
    fileName : the name of the file, using this format : TextTitle_[author's name][number].txt
    """
    name = ""
    endIndex = len(fileName) - 5                                                       # the index of the last digit of [number]
    while ord(fileName[endIndex - 1]) < 58 and ord(fileName[endIndex - 1]) > 47:
        endIndex -= 1
    beginningIndex = endIndex
    while fileName[beginningIndex - 1] != '_':
        beginningIndex -= 1
    return fileName[beginningIndex : endIndex]