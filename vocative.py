import textwrap


with open('O.txt', 'r') as f1:
    lines = f1.readlines()
    lines = [line.rstrip() for line in lines]

counter = 0

with open('novel.txt', 'w') as f2:
    i = 1
    output = "" 
    for line in lines:
        if counter < 50500:
            output = output + " " + line
            if i % 5 == 0:
                my_wrap = textwrap.TextWrapper(
                    width=80, initial_indent="\n     "
                ) 
                f2.write(my_wrap.fill(output))
                output = ""
            i += 1
        counter += len(line.split())

