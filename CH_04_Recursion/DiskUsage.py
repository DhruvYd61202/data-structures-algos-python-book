import os
def diskUsage(path):
    """Return the number of bytes used by a file/folder and its contents."""
    total = os.path.getsize(path)
    # print(total, path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += diskUsage(childpath)
    print('{0:<7}'.format(total), path)
    return total

total_space = diskUsage("P:\\ImagePrint")
# print(os.path.getsize("P:\\ImagePrint"))
print(total_space)