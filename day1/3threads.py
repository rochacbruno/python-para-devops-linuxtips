import concurrent.futures
import time


USERS = ["bruno", "guido", "linus"]


def get_github_user_data(username):
    # request on github API
    time.sleep(300)
    print(f"trhead {username} finished.")


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(get_github_user_data, name) for name in USERS]
    concurrent.futures.wait(futures)


print("All threads finished")
    



