from print2 import pprint
import emoji
# Print2 requires `termcolor` to be installed to run, so that is my third dependancy
pprint(emoji.emojize(":thumbs_up:"), prefix="Python is: ", indent="\t", color="blue", level=1)