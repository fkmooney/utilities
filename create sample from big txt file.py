### This can be used to open big json files one line at a time. 
### It can be used to open other big .txt files.


f = 'extended_dma_sansnb_201830.txt'  # extended dma file name

with open(f) as myfile:
    head = [next(myfile) for x in range(2000)]
print(head)


with open("Output.txt", "w") as text_file:
    print(head, file=text_file)
