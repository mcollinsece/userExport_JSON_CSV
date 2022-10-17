import pwd

def fetch_users():
    # init user array
    users = []
    #Loop through all users
    for user in pwd.getpwall():
    #Determine if user is a system user
        if user.pw_uid >= 1000 and 'home' in user.pw_dir:
            #If true, append user
            users.append({
                'name': user.pw_name,
                'id': user.pw_uid,
                'home': user.pw_dir,
                'shell': user.pw_shell,
            })
        return users
