import random

classes = ("KNIGHT", "PAGE", "MAGE", "SEER", "MAID", "HEIR", "WITCH", "SYLPH", "PRINCE", "BARD", "THIEF", "ROGUE")
aspectos = ("TIME", "SPACE", "LIFE", "DOOM", "BREATH", "BLOOD", "LIGHT", "VOID", "HEART", "MIND", "RAGE", "HOPE")


def fazer_classpect(nome1, nome2):
    fusaoca = f"{classes[(random.randint(0, 11))]} of {aspectos[(random.randint(0, 11))]}"
    return f"{nome1} {nome2} é {fusaoca}"
