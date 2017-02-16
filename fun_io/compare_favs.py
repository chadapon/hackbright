favs_file = open('yenny_fav_foods.txt')
yenny_fav = favs_file.readlines()
# print yenny_fav
favs_file.close()

favs_file = open('mod.txt')
mod_fav = favs_file.readlines()
# print mod_fav
favs_file.close()

def compare_fav(fav1,fav2):
    for i in range(len(yenny_fav)):
        print fav1[i]
        print fav2[i]
        if fav1[i] == fav2[i]:
            print "Our favorite foods are the same!"
        else:
            print "Our favorite foods are different"
compare_fav(yenny_fav,mod_fav)        
