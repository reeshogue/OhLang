#This is my terrible attempt at creating a natural language transpiler using tools from textgenrnn...
#Through this, I realized that natural language makes for an awful programming language... Too much vagueness... 
#I realize that I could have done a Transformer model in Pytorch, but this is about as out of the box as possible without dealing with all that...

from textgenrnn import textgenrnn
oh_model = textgenrnn()

oh_model.train_from_file("./syntax_corpora.txt", num_epochs=10, batch_size=16)
while True:
    outp = oh_model.generate(return_as_list=True, prefix="ohint> "+input("oh> ")+"\n")
    outp = outp[0]
    print(outp)