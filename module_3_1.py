calls = 0
def count_calls():
    global calls
    calls +=1
def string_info(string_):
    si_tuple = (len(string_), string_.upper(), string_.lower())
    count_calls()
    return si_tuple
def is_contains(string_, list_to_search):
    count_calls()
    string_ = string_.lower()
    list_to_search = [s.lower() for s in list_to_search]
    if string_ in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)