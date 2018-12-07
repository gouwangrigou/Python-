current_users=['xu','zhang','yang','liu','wu']
new_users=['xu','yang','xin','Xu','tom',]
for new_user in new_users:
    if new_user.upper() in current_users or new_user.lower() in current_users:
        print(new_user+" used")
    else:
        print(new_user+" not used")