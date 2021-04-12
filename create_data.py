from random import choice, uniform

def main(qof=10000):
    action_choices = ['1', '2', '3']
    for _ in range(qof):
        action_number = choice(action_choices)
        number_1 = uniform(-1000000.0, 1000000.0)
        number_2 = uniform(-1000000.0, 1000000.0)
        with open(f'./data/in_{_}.dat', 'w') as file_:
            file_.write(action_number+'\n')
            file_.write(str(number_1)+' '+str(number_2)+'\n')

if __name__ == '__main__': 
    main()

