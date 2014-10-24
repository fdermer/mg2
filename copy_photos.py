import shutil, os, re, hashlib
from slugify import slugify
#----------------------------------------------------------#
#---- This time, I want to slugify the name of the file ---#
#----------------------------------------------------------#


root_src_dir = "/Users/Fred/www/mg2/mg2/recipe/static/recettes/"
# root_dst_dir needs to be created before launching the procedure
root_dst_dir = "/Users/Fred/www/mg2/mg2/recipe/static/recettes2/"
count = 0

for src_dir, dirs, files in os.walk(root_src_dir):
    #if count > 100:
    #    break
    for file in files:
        # Copy images only:
        if re.search('.jpeg|.png|.jpg', file):
            src_file = os.path.join(src_dir, file)

            # Destination dir = first letter of the hash of the file name
            dst_dir = os.path.join(root_dst_dir, hashlib.md5(file).hexdigest()[:1])
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)

            #Slugify the name of the file
            slug = file.split(".")
            slug = slugify(slug[0]) + "." + slugify(slug[1])

            dst_file = os.path.join(dst_dir, slug)
            # Prevents duplicates:
            if os.path.exists(os.path.join(root_dst_dir, dst_file)):
                continue
            else:
                count += 1
                #print count
                #if count > 100:
                #    break
                #print "Copying", dst_file
                shutil.copy(src_file, os.path.join(root_dst_dir, dst_file))
print "Nb files copied: ", count