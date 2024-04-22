def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()


if __name__ == '__main__':
    print(get_formatted_name('Chen', 'Shi', 'Lei'))
