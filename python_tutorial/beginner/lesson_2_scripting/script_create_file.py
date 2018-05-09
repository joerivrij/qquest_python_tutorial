#!/usr/bin/env python


def create_random_file(file_name, file_text):
    file = open(file_name, "w")
    file.write(file_text)
    file.close()


create_random_file('joeri.txt', "My name is Joeri")
create_random_file('print_something.py', "#!/usr/bin/env python \n"
                                         "\n"
                                         "print('hello world')")



f = open("example_docker_file.yml", "r")
text = f.read()
print(text)
create_random_file("Dockerfile", text)