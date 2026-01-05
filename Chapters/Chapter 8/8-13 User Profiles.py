def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

print(build_profile("james", "cavanaugh", location="kennesaw", college="nc state", email="james.arr.cavanaugh@gmail.com"))