FILE=slides.tex
BUILD=./build

OUT=$(BUILD)/$(FILE:.tex=.pdf)

COMPILE=pdflatex -output-directory=$(BUILD) $(FILE)


all: $(OUT) Makefile


$(OUT):	$(FILE)
	@mkdir -p $(BUILD)
	$(COMPILE) 
	$(COMPILE) #twice, because... latex!


clean:
	rm -rf $(BUILD)
