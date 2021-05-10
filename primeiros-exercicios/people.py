import area

PEOPLE_PER_SQUARE = 2
FIELD_LENGTH = 240
FIELD_WIDTH = 45
PEOPLE_AT_AREA_TOTAL = area.rectangle(
    FIELD_LENGTH, FIELD_WIDTH) // PEOPLE_PER_SQUARE

print("O número aproximadas de pessoas no espaço é de:", PEOPLE_AT_AREA_TOTAL)
