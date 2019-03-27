def sorted_list(file_name):
    """
    Read text file, convert its content to list and returns it
    :param file_name: the name of the text file from which you read information
    :return: sorted list
    """
    with open(file_name):
        rt = sorted(open(file_name).read().split())
    return rt

def write_to_input(filename, output_file):
    """
    Write elements from the list in the file, each element on the new line, deletes duplicates
    and counts how many times it encounters in the list.
    :param filename: the name of the text file in which you want to write
    :return: list from which you take information
    """
    with open(filename, "w") as readf:
        list_with_duplicates = []
        for elem in output_file:
            n = str(output_file.count(elem))
            a = elem + "- " + n
            list_with_duplicates.append(a)
        pure = set(sorted(list_with_duplicates))
        for i in sorted(list(pure)):
            print(i, file=readf, end="\n")


if __name__ == "__main__":
    output_file = sorted_list("myfile1.txt")
    write_to_input("myfile4.txt", output_file)

