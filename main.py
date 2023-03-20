import instaloader
ins = instaloader.Instaloader()
print("Github : https://github.com/AbdulazizSherzodjanov")
user = input("Enter a instagram username : ")
ins.download_profile(user,profile_pic_only=True)
print(user," Instagram data of profile  succesfully  downloaded !")
