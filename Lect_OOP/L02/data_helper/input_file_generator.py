# -*- coding: utf8 -*-

from random import randint

N_MAXKEY = 25
MULT = 4

Pets = {"Dog": 2,    # Собака
        "Cat": 2,    # Кіт
        "Parrot": 2, # Папуга
        }

petNames = list(Pets.keys())

def generate(fname, figures_number):
    PET_COUNT = len(petNames)

    with open(fname, "w", encoding='utf-8') as f_out:
        for i in range(figures_number):

            figure = petNames[randint(0, PET_COUNT - 1)]
            print("%30s" % figure, file=f_out, end=" ")

            val_num = Pets[figure]
            for i in range(val_num):
                val = randint(0, N_MAXKEY)
                print("%4d" % val, file=f_out, end=" ")

            print(file=f_out)



if __name__ == "__main__":
    generate("input01.txt", 100)

