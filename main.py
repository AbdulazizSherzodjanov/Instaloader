import instaloader
ins = instaloader.Instaloader()
user = input("Username : ")
ins.download_profile(user,profile_pic_only=True)
