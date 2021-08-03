def agree(torf):
    if torf.lower() == 'y':
        return 'Great'
    else:
        return 'Sad Face'

answer = input('Agree or disagree? Y/N...')
reply = agree(answer)

print(reply)



