import sys
import asyncio

PIPE = asyncio.subprocess.PIPE

# scale pdf
# cpdf -scale-to-fit <to> <source> -o <target>
async def scale(source, target, to="a5portrait"):
    cmd = "cpdf"
    args = " ".join(("-scale-to-fit", to, source, "-o", target))
    proc = await asyncio.create_subprocess_shell(cmd + " " + args, stdout=PIPE, stderr=PIPE)

    _, _= await proc.communicate() # stdout, stderr
    return proc.returncode

def quote(text):
    return "'" + text + "'"

# add text to pdf
# cpdf -add-text "Test: Room no: 112" <position> -font <font> -font-size <font_size> <source> -o <target>
# use %Page for page number
async def addText(
        source,
        target,
        text="",
        position="-bottomright 10",
        font="Courier",
        font_size=10
):
    cmd = "cpdf"
    args = " ".join(("-add-text", quote(text), position, "-font", quote(font), "-font-size", str(font_size), source, "-o", target))
    print("Command: ", cmd + " " + args)
    proc = await asyncio.create_subprocess_shell(cmd + " " + args, stdout=PIPE, stderr=PIPE)

    _, _= await proc.communicate() # stdout, stderr
    return proc.returncode

# merge pdf
# cpdf -merge *<sources> -o <target>
# sources is an array of filenames
async def merge(sources, target):
    cmd = "cpdf"
    args = " ".join(("-merge", *sources, "-o", target))
    proc = await asyncio.create_subprocess_shell(cmd + " " + args, stdout=PIPE, stderr=PIPE)

    _, _= await proc.communicate() # stdout, stderr
    return proc.returncode

async def main():
    pass

# import asyncio
# from pprint import pprint

# import random


# async def coro(tag):
#     print(">", tag)
#     await asyncio.sleep(random.uniform(1, 3))
#     print("<", tag)
#     return tag


# loop = asyncio.get_event_loop()

# group1 = asyncio.gather(*[coro("group 1.{}".format(i)) for i in range(1, 6)])
# group2 = asyncio.gather(*[coro("group 2.{}".format(i)) for i in range(1, 4)])
# group3 = asyncio.gather(*[coro("group 3.{}".format(i)) for i in range(1, 10)])

# all_groups = asyncio.gather(group1, group2, group3)

# results = loop.run_until_complete(all_groups)

# loop.close()

# pprint(results)


# Directory containing all the pdfs
# dir = sys.argv[1]
# dataFile = sys.argv[2]
# target = sys.argv[3] or "untitled.pdf"

# Add Page numbers to all the pdfs at bottom center
# Add Room number and time to all pdfs
# Add the abstract type at the top to all the pdfs
# Merge all the pdfs into a single one

# Scale the final pdf to A5
# asyncio.run(scale(sys.argv[1], sys.argv[2]))
asyncio.run(addText(sys.argv[1], sys.argv[2], "Hi", "-bottomleft 10"))
asyncio.run(addText(sys.argv[2], sys.argv[2], "Bye", "-bottomright 10"))


