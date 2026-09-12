"""In this code we are implementing the code for the logging and string method like split"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("Demo Logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

print("Shree Gneshay Namah")
a = 3
cname = "Talent Sketchers"

logger.debug("cname = %s ", cname)
print(type(cname))

# cname = list(cname)
# logger.info("")
# print(f"type of the cname = {type(cname)} , {cname}")
# print()

logger.info("we are starting the splitting of %s", cname)
print(cname.split(sep=" "))

logger.info("String is split successfully...")
