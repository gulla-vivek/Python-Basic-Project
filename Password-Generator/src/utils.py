def get_yes_no_input(message) :
    while True :
        choice = input(message).strip().lower()
        if choice in ['y','yes']:
            return  True
        if choice in ['n', 'No']:
            return False
        print('Please enter Y or N')