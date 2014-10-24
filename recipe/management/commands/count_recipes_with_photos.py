#!/usr/bin/env python
# -*- coding: utf-8 -*-


from recipe.models import Recipe
import shutil, os, re, hashlib

root_dir = "/Users/Fred/www/mg2/mg2/recipe/static/"
count = 0

for recipe in Recipe.objects.all():
    if recipe.image_slug and recipe.image_name:
        if os.path.exists(os.path.join(root_dir, recipe.get_image_url())):
            count +=1
            print "http://127.0.0.1:8000/static/" + recipe.get_image_url()


print "Nb de photos trouvées: ", count




#
#
#for src_dir, dirs, files in os.walk(root_src_dir):
#    #if count > 100:
#    #    break
#    for file in files:
#        # Copy images only:
#        if re.search('.jpeg|.png|.jpg', file):
#            src_file = os.path.join(src_dir, file)
#
#            # Destination dir = first letter of the hash of the file name
#            dst_dir = os.path.join(root_dst_dir, hashlib.md5(file).hexdigest()[:1])
#            if not os.path.exists(dst_dir):
#                os.mkdir(dst_dir)
#
#            #Slugify the name of the file
#            slug = file.split(".")
#            slug = slugify(slug[0]) + "." + slugify(slug[1])
#
#            dst_file = os.path.join(dst_dir, slug)
#            # Prevents duplicates:
#            if os.path.exists(os.path.join(root_dst_dir, dst_file)):
#                continue
#            else:
#                count += 1
#                #print count
#                #if count > 100:
#                #    break
#                #print "Copying", dst_file
#                shutil.copy(src_file, os.path.join(root_dst_dir, dst_file))
#print "Nb files copied: ", count