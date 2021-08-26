import requests


class PageData:
    total_users = 0
    users_list = []

    # getting data from all 12 pages.
    def get_api_data(self):
        for i in range(1, 13):
            response = requests.get('https://reqres.in/api/users?page='+str(i))
            print(response.status_code)
            self.users_list.append(response.json())

    # counting users of each page
    def all_users(self):
        for i in range(len(self.users_list)):
            self.total_users += len((self.users_list[i]['data']))
        return self.total_users


pd = PageData()
pd.get_api_data()
users = pd.all_users()
print(users)
